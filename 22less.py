import time
import random
import numpy as np

#1
# def build_polyline(points):
#     sorted_points = sorted(points, key = lambda item: (item[0], item[1]))
#     return sorted_points

# def generate_data(size, x_min= 0, x_max = 100, y_min = 0, y_max = 100):
#     return [(random.randint(x_min, x_max), random.randint(y_min, y_max)) for _ in range(size)]
    
# def measure_time(func, size, repeats = 10):
#     times = []
#     lst_of_tuple = generate_data(size)
#     res = None
#     for _ in range(repeats):
#         start_time = time.perf_counter()
#         res = func(lst_of_tuple.copy())
#         end_time = time.perf_counter()
#         times.append(end_time - start_time)
#     return np.mean(times), res

# n = 100
# times, res = measure_time(build_polyline, n)
# print(f'Ломаная из {n} точек: {res}')
# print(f'Время выполнения: {times:.6f} секунд')
        

#2
# def generate_segments(n):
#     k = n//2
#     segments = []

#     for i in range(k):
#         x = i/k
#         start = (x, 0.0)
#         end = (x, 1.0)
#         segments.append((start, end))

#     for j in range(k):
#         y = j/k
#         start = (0.0, y)
#         end = (1.0, y)
#         segments.append((start, end))

#     return segments

# def count_intersections(segments):
#     k = len(segments) // 2
#     return k * k 

# def measure_time(func, size, repeats=10):
#     times = []
#     res = None
#     for _ in range(repeats):
#         start_time = time.perf_counter()
#         res = func(size)
#         end_time = time.perf_counter()
#         times.append(end_time - start_time)
#     return np.mean(times), res

# sizes = [2, 4, 8, 16, 32, 64, 128]
# for size in sizes:
#     times, res = measure_time(generate_segments, size)
#     intersections = count_intersections(res)
#     print(f'Для {size} отрезков:')
#     print(f'Количество пересечений: {intersections}')
#     print(f'Ожидаемое по формуле (n/2)**2: {(size//2)**2}')
#     print(f'Время генерации: {times:.6f} секунд')
#     print()

#3
def check_circle_intersections(circles):
    events = []

    for i, (x, y, r) in enumerate(circles):
        events.append((x - r, 'start', i))
        events.append((x + r, 'end', i))

    events.sort(key = lambda x : x[0])

    active = []

    def find_insert_pos(y):
        left, right = 0, len(active)
        while left < right:
            mid = (left + right) // 2
            if active[mid][0] < y:
                left = mid + 1
            else:
                right = mid
        return left
    
    for x, typ, i in events:
        xi, yi, ri = circles[i]
        
        if typ == 'start':
            pos = find_insert_pos(yi)
            
            for j in [pos-1, pos]:
                if 0 <= j < len(active):
                    yj, circle_j = active[j]
                    xj, _, rj = circles[circle_j]
                    
                    if abs(yi - yj) > ri + rj:
                        continue
                    
                    dx = xi - xj
                    dy = yi - yj
                    d_sq = dx*dx + dy*dy
                    if d_sq <= (ri + rj)**2:
                        return True
            
            active.insert(pos, (yi, i))
            
        else:
            pos = find_insert_pos(yi)
            active.pop(pos)
        
    
    return False

def measure_time(func, lst, repeats=10):
    times = []
    res = None
    for _ in range(repeats):
        start_time = time.perf_counter()
        res = func(lst.copy())
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    return np.mean(times), res

circles1 = [(0, 0, 1), (3, 0, 1)]
times1, res1 = measure_time(check_circle_intersections, circles1)
print(f'Есть ли пересекающиеся круги: {res1}')
print(f'Время выполнения: {times1:.6f} секунд')
print()

circles2 = [(0, 0, 2), (1, 1, 1.5)]
times2, res2 = measure_time(check_circle_intersections, circles2)
print(f'Есть ли пересекающиеся круги: {res2}')
print(f'Время выполнения: {times2:.6f} секунд')
print()