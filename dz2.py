import time
import random 
import numpy as np
import matplotlib.pyplot as plt

#1
def factor(n):
    i = 2
    ans = []
    while i * i <= n:
        while n % i == 0:
            ans.append(i)
            n //= i
        i += 1
    if n > 1:
        ans.append(n)
    return ans

def gcd(a, b):
    while b != 0:
        if a < b:
            a, b = b, a
        a -= b
    return a

def gcd_soot(a, b):
    if b == 0:
        return a
    return gcd_soot(b, a % b)

def gcd_mn(a, b):
    a_mn = sorted(factor(a))
    b_mn = sorted(factor(b))

    common_factors = []
    i, j = 0, 0
    while i < len(a_mn) and j < len(b_mn):
        if a_mn[i] == b_mn[j]:
            common_factors.append(a_mn[i])
            i += 1
            j += 1
        elif a_mn[i] < b_mn[j]:
            i += 1
        else:
            j += 1

    total_gcd = 1
    for k in common_factors:
        total_gcd *= k
    return total_gcd

def binary_gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a

    shift = 0

    while (a & 1) == 0 and (b & 1) == 0:
        a >>= 1
        b >>= 1
        shift += 1

    while a != b:
        if a < b:
            a, b = b, a

        if (a & 1) == 0:
            a >>= 1
        elif (b & 1) == 0:
            b >>= 1
        else:
            a = (a - b) >> 1
    return a << shift

def measure_time(func, *args, repeats=10):
    times = []
    for _ in range(repeats):
        start_time = time.perf_counter()
        func(*args)
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    return np.mean(times), np.min(times), np.max(times)

sizes = [10 ** i for i in range(1, 7)]

time_gcd_mean = []
time_gcd_min = []
time_gcd_max = []

time_gcd_soot_mean = []
time_gcd_soot_min = []
time_gcd_soot_max = []

time_gcd_mn_mean = []
time_gcd_mn_min = []
time_gcd_mn_max = []

time_gcd_binary_mean = []
time_gcd_binary_min = []
time_gcd_binary_max = []

for size in sizes:
    a = random.randint(size, 10*size)
    b = 15

    mean_gcd, min_gcd, max_gcd = measure_time(gcd, a, b)
    time_gcd_mean.append(mean_gcd)
    time_gcd_min.append(min_gcd)
    time_gcd_max.append(max_gcd)

    mean_gcd_soot, min_gcd_soot, max_gcd_soot = measure_time(gcd_soot, a, b)
    time_gcd_soot_mean.append(mean_gcd_soot)
    time_gcd_soot_min.append(min_gcd_soot)
    time_gcd_soot_max.append(max_gcd_soot)

    mean_gcd_mn, min_gcd_mn, max_gcd_mn = measure_time(gcd_mn, a, b)
    time_gcd_mn_mean.append(mean_gcd_mn)
    time_gcd_mn_min.append(min_gcd_mn)
    time_gcd_mn_max.append(max_gcd_mn)

    mean_gcd_binary, min_gcd_binary, max_gcd_binary = measure_time(binary_gcd, a, b)
    time_gcd_binary_mean.append(mean_gcd_binary)
    time_gcd_binary_min.append(min_gcd_binary)
    time_gcd_binary_max.append(max_gcd_binary)

    print(f"Размер: {size}")
    print(f"GCD (вычитание): среднее={mean_gcd:.10f}, мин={min_gcd:.10f}, макс={max_gcd:.10f}")
    print(f"GCD2 (деление): среднее={mean_gcd_soot:.10f}, мин={min_gcd_soot:.10f}, макс={max_gcd_soot:.10f}")
    print(f"GCD3 (множетели): среднее={mean_gcd_mn:.10f}, мин={min_gcd_mn:.10f}, макс={max_gcd_mn:.10f}")
    print(f"GCD4 (битовое): среднее={mean_gcd_binary:.10f}, мин={min_gcd_binary:.10f}, макс={max_gcd_binary:.10f}")
    print("------")

plt.figure(figsize=(12, 6))

plt.plot(sizes, time_gcd_mean, label="GCD (вычитание)", marker='o', color='blue')
plt.fill_between(sizes, time_gcd_min, time_gcd_max, alpha=0.2, color='blue')

plt.plot(sizes, time_gcd_soot_mean, label="GCD2 (деление с остатком)", marker='o', color='orange')
plt.fill_between(sizes, time_gcd_soot_min, time_gcd_soot_max, alpha=0.2, color='orange')

plt.plot(sizes, time_gcd_mn_mean, label="GCD3 (множетели)", marker='o', color='pink')
plt.fill_between(sizes, time_gcd_mn_min, time_gcd_mn_max, alpha=0.2, color='pink')

plt.plot(sizes, time_gcd_binary_mean, label="GCD4 (битовое)", marker='o', color='green')
plt.fill_between(sizes, time_gcd_binary_min, time_gcd_binary_max, alpha=0.2, color='green')

plt.xscale("log")
plt.yscale("log")
plt.xlabel("Размер чисел")
plt.ylabel("Время выполнения (секунды)")
plt.title("Сравнение GCD, GCD2, GCD3, GCD4")
plt.legend()
plt.grid(True)
plt.show()

#2
# def del_dubl_set(lst):
#     return list(set(lst))

# def del_dubl_list(lst):
#     res = []
#     for item in lst:
#         if item not in res:
#             res.append(item)
#     return res

# def measure_time(func, lst, repeats = 10):
#     times = []
#     for _ in range(repeats):
#         start_time = time.perf_counter()
#         result = func(lst)
#         end_time = time.perf_counter()
#         times.append(end_time - start_time)
#     return  np.mean(times)

# sizes = [10, 100, 500, 1000, 2000, 5000]
# times_set = []
# times_naive = []

# for size in sizes:
#     arr = list(np.random.randint(0, size*2, size))

#     time_set = measure_time(del_dubl_set, arr)
#     times_set.append(time_set)

#     time_naive = measure_time(del_dubl_list, arr)
#     times_naive.append(time_naive)

#     print(f"Размер: {size:>6} | Множество: {time_set:.6f}s | Наивный метод: {time_naive:.6f}s")

# plt.figure(figsize=(12, 7))
# plt.plot(sizes, times_set, label="Множество (O(n))", marker="o", color="green")
# plt.plot(sizes, times_naive, label="Двойной цикл (O(n²))", marker="s", color="red")

# plt.title("Сравнение времени удаления всех дубликатов из списка")
# plt.xlabel("Размер списка")
# plt.ylabel("Время выполнения (секунды)")
# plt.xscale("log")
# plt.yscale("log")
# plt.grid(True, which="both", linestyle="--")
# plt.legend()
# plt.show()