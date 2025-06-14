from math import atan2
import random
import time

def cross(o, a, b):
    return (a[0] - o[0])*(b[1] - o[1]) - (a[1] - o[1])*(b[0] - o[0])

def graham_scan(points):
    if len(points) <= 1:
        return points
    
    start = min(points, key = lambda p: (p[1], p[0]))

    def polar_angle(p):
        return atan2(p[1] - start[1], p[0] - start[0])
    
    sorted_points = sorted(points, key = lambda p: (polar_angle(p), (p[0] - start[0])**2 + (p[1] - start[1])**2))

    stack = []
    for p in sorted_points:
        while len(stack) >= 2 and cross(stack[-2], stack[-1], p) <= 0:
            stack.pop()
        stack.append(p)

    return stack

def distance(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5

def find_farthest_points(points):
    if len(points) < 2:
        return None
    
    ch = graham_scan(points)

    max_dist = 0
    best_pair = (ch[0], ch[1])

    j = 1
    for i in range(len(ch)):
        while distance(ch[i], ch[(j+1) % len(ch)]) > distance(ch[i], ch[j]):
            j = (j + 1) % len(ch)

        d = distance(ch[i], ch[j])
        if d > max_dist:
            max_dist = d
            best_pair = (ch[i], ch[j])

    return best_pair

def generate_data(size, x_min= 0, x_max = 100, y_min = 0, y_max = 100):
    return [(random.randint(x_min, x_max), random.randint(y_min, y_max)) for _ in range(size)]

def measure_time(func, point_count = [10, 100, 1000], repeats = 10):
    for count in point_count:
        total_time = 0
        for _ in range(repeats):
            points = generate_data(count)

            start_time = time.perf_counter()
            func(points)
            end_time = time.perf_counter()

            total_time += end_time - start_time

        avg_time = total_time / repeats
        print(f'Среднее время для {count} точек: {avg_time:.6f} сек')

time_results = measure_time(find_farthest_points)

    