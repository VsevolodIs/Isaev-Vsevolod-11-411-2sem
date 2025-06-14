import time
import numpy as np
import random

#1
# def lis_length(x):
#     tails = []

#     for i in range(0, len(x)):
#         left = 0
#         right = len(tails)

#         while left < right:
#             mid = (left + right) // 2

#             if tails[mid] < x[i]:
#                 left = mid + 1
#             else:
#                 right = mid

#         if left == len(tails):
#             tails.append(x[i])
#         else:
#             tails[left] = x[i]
    
#     return len(tails)

# def generate_data(n): 
#     large_array = [random.randint(1, 1000) for _ in range(n)]
#     return large_array

# def measure_time(func, n, repeats=10):
#     x = generate_data(100)
#     times = []
#     result = None
#     for _ in range(repeats):
#         start_time = time.perf_counter()
#         result = func(x.copy())
#         end_time = time.perf_counter()
#         times.append(end_time - start_time)
#     return result, np.mean(times)

# sizes = [100, 1000, 10000, 100000]
# for n in sizes:
#     result, avg_time = measure_time(lis_length, n)
#     print(f"n = {n}, LIS length = {result}, avg time = {avg_time:.8f} сек")

#2
def radix_sort_bits(arr, k):
    for i in range(0, k):
        zeros = []
        ones = []

        for j in range(0, len(arr)):
            if (arr[j] >> i) & 1 == 0:
                zeros.append(arr[j])
            else:
                ones.append(arr[j])
        
        arr = zeros + ones

    return arr

def generate_data(n, k):
    return [random.randint(0, 2**k - 1) for _ in range(n)]

def measure_time(func, n, k,  repeats=10):
    x = generate_data(n, k)
    times = []
    result = None
    for _ in range(repeats):
        x_copy = x.copy()
        start_time = time.perf_counter()
        result = func(x_copy, k)
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    return result, np.mean(times)

n = 1000
k = 16
result, avg_time = measure_time(radix_sort_bits, n, k)

print(f"Размер массива: {n}, Битов: {k}")
print(f"Среднее время: {avg_time:.6f} сек")
print("Первые 10 элементов:", result[:10])



