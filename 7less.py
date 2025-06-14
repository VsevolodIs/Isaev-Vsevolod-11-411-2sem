import numpy as np
import time
import matplotlib.pyplot as plt

def factor(n, p):

    e = 0
    value = p
    while value <= n:
        e += n // value
        value *= p

    if e > 0:
        return 0
    
    res = 1
    while n > 0:
        q = n // p
        r = n % p

        if q % 2 == 1:
            res = (p - res) % p

        for i in range(2, r + 1):
            res = (res * i) % p

        n = q
    
    return res


def measure_time(func, n, p, repeats = 7):
    times = []
    res = None
    for _ in range(repeats):
        start_time = time.time()
        res = func(n, p)
        end_time = time.time()
        times.append(end_time - start_time)
    return res, np.mean(times)

numbers = [10, 30, 50, 100, 200, 500, 1000, 5000, 10000]
primes = [7, 13, 19, 23, 29]

plt.figure(figsize = (12, 7))

for p in primes:
    times_func = []
    for n in numbers:
        res, res_time = measure_time(factor, n, p)
        times_func.append(res_time)
        print(f'factor({n}, {p}) = {res}, время: {res_time:.2e} сек')

    plt.plot(numbers, times_func, label = f'p = {p}', marker = 'o')

plt.title('График зависимости времени выполнения функции factor(n, p)')
plt.xlabel('Число n')
plt.ylabel('Время выполнения (секунды)')
plt.xscale('linear')
plt.yscale('linear')
plt.grid(True, which="both", linestyle='--')
plt.legend()
plt.show()