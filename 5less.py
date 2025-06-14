import time
import random 

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
    if a == 0:
        return b
    if a < b:
        a, b = b, a
    return gcd_soot(b, a % b)

def gcd_mn(a, b):
    a_mn = factor(a)
    b_mn = factor(b)

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

def measure_time(func, a, b):
    start_time = time.time()
    func(a, b)
    end_time = time.time()
    return  end_time - start_time

numbers = [((random.randint(10, 1000000)), (random.randint(10, 1000000))) for _ in range(100)]

time_gcd = []
time_gcd_soot = []
time_gcd_mn = []

for a, b in numbers:
    time_gcd.append(measure_time(gcd, a, b))
    time_gcd_soot.append(measure_time(gcd_soot, a, b))
    time_gcd_mn.append(measure_time(gcd_mn, a, b))

avg_time_gcd = sum(time_gcd) / len(time_gcd)
avg_time_gcd_soot = sum(time_gcd_soot) / len(time_gcd_soot)
avg_time_gcd_mn = sum(time_gcd_mn) / len(time_gcd_mn)

print(f"Среднее время работы алгоритма Евклида с вычитанием: {avg_time_gcd:.6f} секунд")
print(f"Среднее время работы алгоритма Евклида с остатком: {avg_time_gcd_soot:.6f} секунд")
print(f"Среднее время работы алгоритма с разложением на множители: {avg_time_gcd_mn:.6f} секунд")

