import random
import time
import numpy as np

#1
# def generate_lst(n):
#     nums = list(range(n + 1))
#     nu = random.choice(nums)
#     nums.remove(nu)
#     random.shuffle(nums)
#     return nums

# def find_number(nums):
#     n = len(nums)
#     ex_sum = (n * (n+1)) // 2
#     act_sum = sum(nums)
#     return ex_sum - act_sum

# def measure_time(n, repeats = 7):
#     lst_of_num = generate_lst(n)
#     times = []
#     res = None
#     for _ in range(repeats):
#         start_time = time.perf_counter()
#         res = find_number(lst_of_num)
#         end_time = time.perf_counter()
#         times.append(end_time - start_time)
#     return np.mean(times), res

# n = 50
# times, res = measure_time(n)
# print(f'Массив длиной {n}, пропущенное число {res}')
# print(f'Среднее время выполнения {times:.8f}')

#2
def generate_lst(n):
    j = random.randint(1, n-2) 
    ub = sorted([random.randint(1, 1000) for _ in range(j+1)], reverse=True)
    vos = sorted([random.randint(ub[-1]+1, 2000) for _ in range(n-j-1)])
    return ub + vos

def find_point(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] > arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    
    return left

def measure_time(n, repeats=7):
    arr = generate_lst(n)
    times = []
    results = set()
    
    for _ in range(repeats):
        start_time = time.perf_counter()
        res = find_point(arr)
        end_time = time.perf_counter()
        times.append(end_time - start_time)
        results.add(res)

    avg_time = np.mean(times)
    return np.mean(times), res


n = 1000  
avg_time, found_j = measure_time(n)

print(f'Последовательность длиной {n}')
print(f'Найденная точка перелома: {found_j}')
print(f'Среднее время выполнения: {avg_time:.8f} секунд')



    