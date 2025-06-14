import math
import numpy as np
import time

def find_closest_pair(p):
    px = sorted(p, key=lambda x: (x[0], x[1]))
    py = sorted(p, key=lambda x: (x[1], x[0]))
    return closest_recursive(px, py)

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def closest_recursive(px, py):
    if len(px) <= 3:
        return brute_force(px)
    
    mid = len(px) // 2
    qx = px[0:mid]
    rx = px[mid:]
    mid_x = px[mid][0]

    qy = []
    ry = []
    for point in py:
        if point[0] <= mid_x:
            qy.append(point)
        else:
            ry.append(point)

    (a1, b1, d1) = closest_recursive(qx, qy)
    (a2, b2, d2) = closest_recursive(rx, ry)

    d = min(d1, d2)
    if d1 == d:
        best_pair = (a1, b1)
    else:
        best_pair = (a2, b2)

    sy = [point for point in py if abs(point[0] - mid_x) < d]

    for i in range(len(sy)):
        for j in range(i+1, min(i+7, len(sy))):
            if distance(sy[i], sy[j]) < d:
                d = distance(sy[i], sy[j])
                best_pair = (sy[i], sy[j])
    return (*best_pair, d)

def brute_force(p):
    min_dist = float('inf')
    best_pair = (None, None)

    for i in range(0, len(p)):
        for j in range(i+1, len(p)):
            d = distance(p[i], p[j])
            if d < min_dist:
                min_dist = d
                best_pair = (p[i], p[j])
    return (*best_pair, min_dist)

def measure_time(func, size, repeats=10):
    times = []
    p1, p2, dist = None, None, None
    for _ in range(repeats):
        start_time = time.perf_counter()
        p1, p2, dist = func(size)
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    return np.mean(times), p1, p2, dist

points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
times, p1, p2, dist = measure_time(find_closest_pair, points)
print(f'Ближайшие точки: {p1} и {p2}, расстояние: {dist:.4f}')
print(f'Время выполнения: {times:.6f} секунд')
