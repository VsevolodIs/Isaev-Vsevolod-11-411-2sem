import time
import matplotlib.pyplot as plt
import numpy as np
#1
def square(n):
    left = 0
    right = n

    while left <= right:
        mid = (left + right) // 2
        square_mid = mid * mid

        if square_mid == n:
            return True
        elif square_mid < n:
            left = mid + 1
        elif square_mid > n:
            right = mid - 1
    return False

def measure_time(func, n, repeats = 7):
    times = []
    result = None

    for _ in range(repeats):
        start_time = time.perf_counter()
        result = func(n)
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    return result, np.mean(times)

numbers = [4, 25, 120, 900, 2601, 4901, 6561, 8100, 10000, 123456789, 987654321, 2147483647]
times_func = []

for number in numbers:
    result, res_time = measure_time(square, number)
    times_func.append(res_time)

    print(f'Является ли число: {number} квадратом целого числа? : {result}.')
    print(f'Скорость выполнения алгоритма: {res_time:.2e}.')

plt.figure(figsize=(12, 7))
plt.plot(numbers, times_func, label = 'Алгортим', marker = "o", color = 'pink')

plt.title('График зависимости времени выполнения программы от входных данных')
plt.xlabel('Число')
plt.ylabel('Время выполнения (секунды)')
plt.xscale('log')
plt.yscale('log')
plt.grid(True, which = "both", linestyle = '--')
plt.legend()
plt.show()










