import time
import matplotlib.pyplot as plt
import numpy as np
import random

#1
# def is_square(x):
#     if x<0:
#         return False
    
#     left, right = 0, x
#     while left <= right:
#         mid = (left + right) // 2
#         square = mid*mid
        
#         if square == x:
#             return mid
#         elif square < x:
#             left = mid + 1
#         elif square > x:
#             right = mid - 1
#     return right

# def measure_time(func, x, repeats = 7):
#     times = []
#     result = None
#     for _ in range(repeats):
#         start_time = time.perf_counter()
#         result = func(x)
#         end_time = time.perf_counter()
#         times.append(end_time - start_time)
#     return np.mean(times), result

# numbers = [10, 30, 50, 100, 200, 500, 1000, 5000, 10000]
# times_func = []

# for number in numbers:
#     res_time, res = measure_time(is_square, number)
#     times_func.append(res_time)

#     print(f'Округленное вниз число {number} до ближайшего целого значения корня от {number}: {res}')
#     print(f'Время выполнения алгоритма: {res_time:.2e} сек')

# plt.figure(figsize=(12, 7))
# plt.plot(numbers, times_func, label = 'Алгортим', marker = "o", color = 'pink')

# plt.title('График зависимости времени выполнения программы от входных данных')
# plt.xlabel('Число')
# plt.ylabel('Время выполнения (секунды)')
# plt.xscale('log')
# plt.yscale('log')
# plt.grid(True, which = "both", linestyle = '--')
# plt.legend()
# plt.show()

#2
# def gcd(a, b):
#     while b != 0:
#         if a < b:
#             a, b = b, a
#         a -= b
#     return a

# def gamaged_tiles(n, m):
#     nod = gcd(n, m)
#     return n + m - nod

# def measure_time(func, n, m, repeats = 7):
#     times = []
#     result = None
#     for _ in range(repeats):
#         start_time = time.perf_counter()
#         result = func(n, m)
#         end_time = time.perf_counter()
#         times.append(end_time - start_time)
#     return np.mean(times), result

# pairs = []
# for _ in range(10):
#     N = random.randint(1, 1000)
#     M = random.randint(1, 1000)
#     pairs.append((N, M))

# times_func = []
# max_values = [] 

# for N, M in pairs:
#     res_time, res = measure_time(gamaged_tiles, N, M)
#     times_func.append(res_time)
#     max_values.append(max(N, M))

#     print(f'N = {N}, M = {M}, количество испорченных плиток = {res}')
#     print(f'Время выполнения алгоритма: {res_time:.2e} сек')

# plt.figure(figsize=(12, 7))

# sorted_data = sorted(zip(max_values, times_func), key=lambda x: x[0])
# x_values = [x[0] for x in sorted_data]
# y_values = [y[1] for y in sorted_data]

# plt.plot(x_values, y_values, label = 'Алгортим', marker = "o", color = 'pink')

# plt.title('График зависимости времени выполнения программы от max(N,M)')
# plt.xlabel('max(N,M)')
# plt.ylabel('Время выполнения')
# plt.xscale('log')
# plt.yscale('log')
# plt.grid(True, which="both", linestyle='--')
# plt.legend()
# plt.show() 



    


    


