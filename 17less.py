import time
import numpy as np

#1
# def sort_Dutch_flag(lst):
#     low = 0
#     mid = 0
#     high = len(lst) - 1
#     while mid <= high:
#         if lst[mid] == 0:
#             lst[low], lst[mid] = lst[mid], lst[low]
#             low += 1
#             mid += 1
#         elif lst[mid] == 1:
#             mid += 1
#         else:
#             lst[mid], lst[high] = lst[high], lst[mid]
#             high -= 1 
#     return lst

# def measure_time(func, a, repeats=10):
#     times = []
#     result = None
#     for _ in range(repeats):
#         start_time = time.perf_counter()
#         result = func(a.copy()) 
#         end_time = time.perf_counter()
#         times.append(end_time - start_time)
#     return result, np.mean(times)     


# a=[0,1,1,0,1,2,1,2,0,0,0,1]
# result, avg_time = measure_time(sort_Dutch_flag, a, repeats=1000)
# print('Отсортированный массив:', result)
# print('Среднее время (сек):', avg_time)

#2
# def msd_radix_sort(strings, d = 0):
#     if len(strings) <= 1:
#         return strings
#     buckets = {}
#     for s in strings:
#         if d < len(s):
#             char = s[d]
#         else:
#             char = ''

#         if char not in buckets:
#             buckets[char] = []
#         buckets[char].append(s)

#     sorted_chars = sorted(buckets.keys())

#     sorted_strings = []
#     for char in sorted_chars:
#         sorted_strings += msd_radix_sort(buckets[char], d+1)

#     return sorted_strings

# def measure_time(func, a, repeats=10):
#     times = []
#     result = None
#     for _ in range(repeats):
#         start_time = time.perf_counter()
#         result = func(a.copy())
#         end_time = time.perf_counter()
#         times.append(end_time - start_time)
#     return result, np.mean(times)

# strings = ['ba', 'abc', 'ab', 'b', 'a', 'cba', 'aa', '']
# print('Исходный массив:', strings)

# sorted_result, avg_time = measure_time(msd_radix_sort, strings, repeats=1000)

# print('Отсортированный массив:', sorted_result)
# print(f'Среднее время выполнения ({len(strings)} элементов, 1000 повторов): {avg_time:.8f} сек')

#3
def merge_sort(arr):
    if len(arr) <= 1:
        return arr.copy()
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged

def count_distinct(arr):
    sorted_arr = merge_sort(arr)

    distinct_count = 1
    for i in range(2, len(arr)):
        if sorted_arr[i] != sorted_arr[i-1]:
            distinct_count += 1
    
    return distinct_count

def measure_time(func, a, repeats=10):
    times = []
    result = None
    for _ in range(repeats):
        start_time = time.perf_counter()
        result = func(a.copy())
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    return result, np.mean(times)

x = [4, 2, 3, 2, 4, 4, 1, 5, 5, 0, 13, 3, 13, 2, 2 ]
print('Исходный массив:', x)

sorted_result, avg_time = measure_time(count_distinct, x, repeats=1000)

print('Количество уникальных чисел:', sorted_result)
print(f'Среднее время выполнения ({len(x)} элементов, 1000 повторов): {avg_time:.8f} сек')