import random
import time
import numpy as np

# 1
# def find_max(a, left, right):
#     if right == left:
#         return a[right]

#     mid = (left + right) // 2
#     max_left = find_max(a, left, mid)
#     max_right = find_max(a, mid + 1, right)

#     if max_left > max_right:
#         return max_left
#     else:
#         return max_right

# def generate_data(n):
#     return [random.randint(1, 100) for _ in range(n)]

# def measure_time(func, n, repeats = 10 ):
#     a = generate_data(n)
#     left = 0
#     right = len(a) - 1
#     res = None
#     times = []
#     for _ in range(repeats):
#         start_time = time.perf_counter()
#         res = func(a, left, right)
#         end_time = time.perf_counter()
#         times.append(end_time - start_time)
#     return np.mean(times), res

# sizes = [10, 50, 100, 500, 1000]
# for size in sizes:
#     times, res = measure_time(find_max, size)
#     print(f'Среднее время выполнения для массива размером {size}: {times:.8f} c')
#     print(f'Результат: {res}')
#     print( )

# 2
# def last_zero(n):
#     if n < 0:
#         raise ValueError('Число должно быть положительным')

#     if (n & 1) == 1:
#         return 0
#     else:
#         return 1 + last_zero(n//2)

# def measure_time(func, n, repeats = 10 ):
#     res = None
#     times = []
#     for _ in range(repeats):
#         start_time = time.perf_counter()
#         res = func(n)
#         end_time = time.perf_counter()
#         times.append(end_time - start_time)
#     return np.mean(times), res

# n = int(input())
# times, res = measure_time(last_zero, n)
# print(f'Среднее время выполнения для числа {n}: {times:.8f} c')
# print(f'Результат: {res}')


# 3
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right  = merge_sort(arr[mid:])

#     merged = []
#     i = j = 0
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             merged.append(left[i])
#             i += 1
#         else:
#             merged.append(right[j])
#             j += 1

#     merged.extend(left[i:])
#     merged.extend(right[j:])

#     return merged

# def del_dubl(a):
#     if len(a) <= 1:
#         return a

#     a = merge_sort(a)

#     res = [a[0]]
#     for i in range(1, len(a)):
#         if a[i] != a[i-1]:
#             res.append(a[i])
#     return res

# def measure_time(func, a, repeats = 10 ):
#     res = None
#     times = []
#     for _ in range(repeats):
#         start_time = time.perf_counter()
#         res = func(a)
#         end_time = time.perf_counter()
#         times.append(end_time - start_time)
#     return np.mean(times), res

# A = [4, 2, 7, 4, 2, 9]
# times, res = measure_time(del_dubl, A)
# print(f'До сортировки: {A}')
# print(f'Среднее время выполнения: {times:.8f} c')
# print(f'Результат: {res}')