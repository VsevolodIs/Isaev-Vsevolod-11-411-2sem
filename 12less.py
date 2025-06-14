import time
import random
import numpy as np
#1
# def find_lower_bound(arr, a):
#     left = 0
#     right = len(arr) - 1
#     lower_bound = -1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] < a:
#             left = mid + 1
#         elif arr[mid] > a:
#             right = mid - 1
#         else:
#             lower_bound = mid
#             right = mid - 1
#     return lower_bound

# def find_upper_bound(arr, a):
#     left = 0
#     right = len(arr) - 1
#     upper_bound = -1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] < a:
#             left = mid + 1
#         elif arr[mid] > a:
#             right = mid - 1
#         else:
#             upper_bound = mid
#             left = mid + 1
#     return upper_bound

# def find_bounds(arr, a):
#     low = find_lower_bound(arr, a)
#     up = find_upper_bound(arr, a)
#     if low == -1 and up == -1:
#         return (0, 0)
#     return (low, up)

# def measure_time(n, a, repeats = 10):
#     arr = sorted([random.randint(1, 100) for _ in range(n)])
#     times = []
#     result = None
#     for _ in range(repeats):
#         start_time = time.perf_counter()
#         result = find_bounds(arr, a)
#         end_time = time.perf_counter()
#         times.append(end_time - start_time)
#     return result, np.mean(times)

# n = int(input('Введите длину массива: '))
# a = int(input('Введите число для поиска: '))
# res, times = measure_time(n, a)
# print(f'Среднее время работы для массива длины {n}, найти {a}: {times:.8f} секунд')
# print(f'Результат: {res}')

#2
# def CLOSEST_SUM(x, y, q):
#     k = len(x)
#     l = len(y)
#     i = 0
#     j = l - 1
#     min_diff = float('inf')
#     closest_sum = 0
#     best_i, best_j = -1, -1

#     while i < k and j >= 0:
#         s = x[i] + y[j]
#         diff = abs(s - q)
        
#         if diff < min_diff:
#             min_diff = diff
#             closest_sum = s
#             best_i, best_j = i, j

#         if s < q:
#             i += 1
#         else:
#             j -= 1

#     return x[best_i], y[best_j], closest_sum

# def measure_time(k, l, q, repeats = 10):
#     x = sorted([random.randint(1, 100) for _ in range(k)])
#     y = sorted([random.randint(1, 100) for _ in range(l)])
#     times = []
#     res_best_i, res_best_j, res = None, None, None
#     for _ in range(repeats):
#         start_time = time.perf_counter()
#         res_best_i, res_best_j, res = CLOSEST_SUM(x, y, q)
#         end_time = time.perf_counter()
#         times.append(end_time - start_time)
#     return res_best_i, res_best_j, res, np.mean(times)

# k = int(input('Введите длину массива 1: '))
# l = int(input('Введите длину массива 2: '))
# q = int(input('Введите число для поиска: '))
# res_best_i, res_best_j, res, times = measure_time(k, l, q)
# print(f'Среднее время работы для массивов длины {k} и {l}, найти {q}: {times:.8f} секунд')
# print(f'Результат: {res_best_i, res_best_j, res}')



    





