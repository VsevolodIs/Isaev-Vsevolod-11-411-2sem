import numpy as np
import time
from functools import cmp_to_key

#1
# def count_common(x, y):
#     i, j, count = 0, 0, 0
#     k, l = len(x), len(y)
#     while i < k and j < l:
#         if x[i] < y[j]:
#             i += 1
#         elif x[i] > y[i]:
#             j += 1
#         else:
#             count += 1
#             i += 1
#             j += 1
#     return count

# def measure_time(func, x, y, repeats=10):
#     times = []
#     result = None
#     for _ in range(repeats):
#         start_time = time.perf_counter()
#         result = func(x, y)
#         end_time = time.perf_counter()
#         times.append(end_time - start_time)
#     return result, np.mean(times)

# x = np.array([1, 3, 5, 7, 9], dtype=np.int32)
# y = np.array([2, 3, 5, 8, 9], dtype=np.int32)

# result, times = measure_time(count_common, x, y)

# print(f"Количество общих элементов: {result}")
# print(f"Время работы: {times:.6f} сек")

#2
# def find_common_element(x, y, z):
#     i, j, k = 0, 0, 0
#     p, q, r = len(x), len(y), len(z)

#     while i < p and j < q and k < r:
#         if x[i] == y[j] and y[j] == z[k]:
#             return x[i]
        
#         m = min(x[i], y[j], z[k])

#         if x[i] == m:
#             i += 1
#         if y[j] == m:
#             j += 1
#         if z[k] == m:
#             k += 1
#     return None

# def measure_time(func, x, y, z, repeats=10):
#     times = []
#     result = None
#     for _ in range(repeats):
#         start_time = time.perf_counter()
#         result = func(x, y, z)
#         end_time = time.perf_counter()
#         times.append(end_time - start_time)
#     return result, np.mean(times)

# x = np.array([1, 4, 5, 6, 8], dtype=np.int32)
# y = np.array([2, 3, 6, 7, 8], dtype=np.int32)
# z = np.array([1, 6, 8, 9, 10], dtype=np.int32)

# result, times = measure_time(find_common_element, x, y, z)
# print(f"Общий элемент: {result}" if result is not None else "Общий элемент не найден")
# print(f"Время работы: {times:.6f} сек")

#3
# def compare(a, b):
#     if a + b > b + a:
#         return -1
#     elif a+b < b + a:
#         return 1
#     else:
#         return 0
    
# def max_number(arr):
#     str_arr = []
#     for num in arr:
#         str_arr.append(str(num))
    
#     str_arr.sort(key = cmp_to_key(compare))

#     result = ''
#     for s in str_arr:
#         result += s

#     if result[0] == '0':
#         return '0'
    
#     return result

# def measure_time(func, x, repeats=10):
#     times = []
#     result = None
#     for _ in range(repeats):
#         start_time = time.perf_counter()
#         result = func(x.copy())
#         end_time = time.perf_counter()
#         times.append(end_time - start_time)
#     return result, np.mean(times)

# arr = [3, 30, 34, 5, 9, 10, 321, 23, 33, 909]

# result, times = measure_time(max_number, arr)

# print(f"Самое большое возможное число: {result}")
# print(f"Время работы: {times:.6f} сек")

#4
def compute_prefix_sums(a, n):
    P = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            P[i][j] = a[i-1][j-1] + P[i-1][j] + P[i][j-1] - P[i-1][j-1]
    return P

def sum_squares(a, n, m):
    P = compute_prefix_sums(a, n)
    result = []
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            total = P[i + m][j + m] - P[i][j + m] - P[i + m][j] + P[i][j]
            result.append(total)
    return result

def measure_time(func, a, n, m, repeats=10):
    times = []
    result = None
    for _ in range(repeats):
        start_time = time.perf_counter()
        result = func(a, n, m)
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    return result, np.mean(times)

n = 4
m = 2
a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

result, avg_time = measure_time(sum_squares, a, n, m)

print("Суммы всех квадратов 2×2:", result)
print(f"Среднее время выполнения: {avg_time:.8f} секунд")
