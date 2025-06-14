import time
import numpy as np


def find_amount_of_ways(n, k):
    if n == 1:
        return 1
    elif n <= 0:
        return 0

    window = [1]
    current_sum = 1
    res = 0

    for i in range(1, n):
        dp_i = current_sum
        res = dp_i

        window.append(dp_i)
        current_sum += dp_i

        if len(window) > k:
            del_am = window.pop(0)
            current_sum -= del_am

    return res


def measure_time(func, *args, repeats=10):
    times = []
    res = None
    for _ in range(repeats):
        start_time = time.perf_counter()
        res = func(*args)
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    return np.mean(times), res


N = 5
K = 2

times, res = measure_time(find_amount_of_ways, N, K)
print(f'Среднее время выполнения: {times:.8f} c')
print(f'Число различных путей для N={N}, K={K}: {res}')