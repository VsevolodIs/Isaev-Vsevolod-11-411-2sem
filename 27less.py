import time
import numpy as np


# 1
def max_equal_sequence_DP(a):
    if len(a) == 0:
        return 0

    dp = [1] * len(a)
    max_len = 1

    for i in range(1, len(a)):
        if a[i] == a[i-1]:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = 1

        if dp[i] > max_len:
            max_len = dp[i]

    return max_len

def max_equal_sequence(a):
    if len(a) == 0:
        return 0

    current_len = 1
    max_len = 1

    for i in range(1, len(a)):
        if a[i] == a[i - 1]:
            current_len += 1
        else:
            current_len = 1

        if current_len > max_len:
            max_len = current_len
    return max_len

import random

def generate_sequence(length=20, max_value=5, min_repeats=1, max_repeats=5):
    sequence = []

    while length > 0:
        value = random.randint(0, max_value)
        repeats = random.randint(min_repeats, min(max_repeats, length))
        sequence.extend([value] * repeats)
        length -= repeats

    if random.choice([True, False]):
        random.shuffle(sequence)

    return sequence

def measure_time(func, size,  repeats=10):
    times = []
    a = generate_sequence(size)
    res = None
    for _ in range(repeats):
        start_time = time.perf_counter()
        res = func(a)
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    return np.mean(times), res

sizes = [10, 50, 100, 150, 500]

for size in sizes:
    times1, res1 = measure_time(max_equal_sequence_DP, size)
    times2, res2 = measure_time(max_equal_sequence, size)

    print()
    print(f'Размер последовательности: {size}')
    print(f'Среднее время выполнения алгоритма: {times1:.8f} c')
    print(f'Результат: {res1}')
    print(f'Среднее время выполнения оптимизированного алгоритма: {times2:.8f} c')
    print(f'Результат: {res2}')

# 2
# def count_paths_DAG(G, s, t):
#     dp = len(G) * [0]
#     dp[s] = 1
#
#     order = topological_sort(G)
#
#     for u in order:
#         for v in G[u]:
#             dp[v] += dp[u]
#
#     return dp[t]
#
#
# def topological_sort(G):
#     visited = len(G) * [False]
#     order = []
#
#     def dfs(u):
#         visited[u] = True
#         for v in G[u]:
#             if not visited[v]:
#                 dfs(v)
#         order.append(u)
#
#     for u in range(len(G)):
#         if not visited[u]:
#             dfs(u)
#
#     return order[::-1]
#
#
# def measure_time(func, *args, repeats=10):
#     times = []
#     res = None
#     for _ in range(repeats):
#         start_time = time.perf_counter()
#         res = func(*args)
#         end_time = time.perf_counter()
#         times.append(end_time - start_time)
#     return np.mean(times), res
#
#
# G = [
#     [],
#     [2, 4],
#     [3],
#     [5],
#     [5],
#     []
# ]
# s, t = 1, 5
# times, res = measure_time(count_paths_DAG, G, s, t)
# print("Количество путей из", s, "в", t, ":", res)
# print(f'Примерное время работы: {times:.8f}')