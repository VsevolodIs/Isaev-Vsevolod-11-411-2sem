import numpy as np
import time
import matplotlib.pyplot as plt

#1
def counter_a(b, p, a):
    counter = 0
    for c in range(0, p):
        if (b * c) % p == a:
            counter += 1
    return counter

def measure_time(func, *args, repeats = 7):
    times = []
    for _ in range(repeats):
        start_time = time.perf_counter()
        func(*args)
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    return np.mean(times)

plt.figure(figsize=(15, 5))

p_values = np.linspace(100, 10000, 50, dtype=int)
time_p = [measure_time(counter_a, 2, p, 1) for p in p_values]

b_values = np.linspace(1, 1000, 50, dtype=int)
time_b = [measure_time(counter_a, b, 1000, 1) for b in b_values]

a_values = np.linspace(0, 999, 50, dtype=int)
time_a = [measure_time(counter_a, 2, 1000, a) for a in a_values]

plt.subplot(1, 3, 1)
plt.plot(p_values, time_p, 'o-', label='Время выполнения')
plt.xlabel('p')
plt.ylabel('Время (сек)')
plt.title('Зависимость времени от p (b=2, a=1)')
plt.grid(True, which="both", linestyle='--')
plt.legend()
plt.xscale('log')
plt.yscale('log')

plt.subplot(1, 3, 2)
plt.plot(b_values, time_b, 'o-', color='green', label='Время выполнения')
plt.xlabel('b')
plt.ylabel('Время (сек)')
plt.title('Зависимость времени от b (p=1000, a=1)')
plt.grid(True, which="both", linestyle='--')
plt.legend()
plt.xscale('log')
plt.yscale('log')

plt.subplot(1, 3, 3)
plt.plot(a_values, time_a, 'o-', color='red', label='Время выполнения')
plt.xlabel('a')
plt.ylabel('Время (сек)')
plt.title('Зависимость времени от a (b=2, p=1000)')
plt.grid(True, which="both", linestyle='--')
plt.legend()
plt.xscale('log')
plt.yscale('log')

plt.tight_layout()
plt.show()

#2
# def gray_code(n):
#     res = []

#     for i in range(2**n):
#         gray = i ^ (i >> 1)

#         res.append(format(gray, f'0{n}b'))
    
#     return res

# def measure_time(func, n, repeats = 7 ):
#     times = []
#     result = None
#     for _ in range(repeats):
#         start_time = time.perf_counter()
#         result = func(n)
#         end_time = time.perf_counter()
#         times.append(end_time - start_time)
#     return result, np.mean(times)

# numbers = [1, 2, 3, 4, 7, 8, 10, 12, 16, 20]
# times_func = []

# for number in numbers:
#     res, res_time = measure_time(gray_code, number)
#     times_func.append(res_time)

#     # print(f'Результат работы кода грея для длины {number}: {res}')
#     print(f'Время выполнения алгоритма для длины {number}: {res_time:.2e} сек')

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

#3
# def is_square(x):
#     left, right = 0, x
#     while left <= right:
#         mid = (left + right) // 2
#         square = mid*mid
#
#         if square == x:
#             return mid
#         elif square < x:
#             left = mid + 1
#         elif square > x:
#             right = mid - 1
#     return right
#
# def measure_time(func, x, repeats = 7):
#     times = []
#     result = None
#     for _ in range(repeats):
#         start_time = time.perf_counter()
#         result = func(x)
#         end_time = time.perf_counter()
#         times.append(end_time - start_time)
#     return np.mean(times), result
#
# numbers = [10, 30, 50, 100, 200, 500, 1000, 5000, 10000]
# times_func = []
#
# for number in numbers:
#     res_time, res = measure_time(is_square, number)
#     times_func.append(res_time)
#
#     print(f'Округленное вниз число {number} до ближайшего целого значения корня от {number}: {res}')
#     print(f'Время выполнения алгоритма: {res_time:.2e} сек')
#
# plt.figure(figsize=(12, 7))
# plt.plot(numbers, times_func, label = 'Алгортим', marker = "o", color = 'pink')
#
# plt.title('График зависимости времени выполнения программы от входных данных')
# plt.xlabel('Число')
# plt.ylabel('Время выполнения (секунды)')
# plt.xscale('log')
# plt.yscale('log')
# plt.grid(True, which = "both", linestyle = '--')
# plt.legend()
# plt.show()