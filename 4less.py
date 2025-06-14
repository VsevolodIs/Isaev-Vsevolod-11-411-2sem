import numpy as np
import time
import matplotlib.pyplot as plt

#1
# def has_duplicates_set(lst):
#     seen = set()
#     for item in lst:
#         if item in seen:
#             return True
#         seen.add(item)
#     return False


# def has_duplicates_naive(lst):
#     for i in range(len(lst)):
#         for j in range(i + 1, len(lst)):
#             if lst[i] == lst[j]:
#                 return True
#     return False


# def measure_time(func, lst, repeats=5):
#     times = []
#     result = None
#     for _ in range(repeats):
#         start_time = time.time()
#         result = func(lst)
#         end_time = time.time()
#         times.append(end_time - start_time)
#     return result, np.mean(times)


# sizes = [10, 100, 500, 1000, 2000, 5000, 10_000]
# times_set = []
# times_naive = []

# for size in sizes:
#     arr = list(np.random.randint(0, size * 2, size))
#     arr.append(arr[0])

#     # Замер для множества
#     result_set, time_set = measure_time(has_duplicates_set, arr)
#     times_set.append(time_set)

#     # Замер для двойного цикла (для всех размеров)
#     result_naive, time_naive = measure_time(has_duplicates_naive, arr)
#     times_naive.append(time_naive)

#     print(f"Размер: {size:>6} | Множество: {time_set:.6f}s | Наивный метод: {time_naive:.6f}s")

# plt.figure(figsize=(12, 7))
# plt.plot(sizes, times_set, label="Множество (O(n))", marker="o", color="green")
# plt.plot(sizes, times_naive, label="Двойной цикл (O(n²))", marker="s", color="red")

# plt.title("Сравнение времени проверки дубликатов")
# plt.xlabel("Размер списка")
# plt.ylabel("Время выполнения (секунды)")
# plt.xscale("log")
# plt.yscale("log")
# plt.grid(True, which="both", linestyle="--")
# plt.legend()
# plt.show()

#2
# def peresech_set(lst1, lst2):
#     set1 = set(lst1)
#     set2 = set(lst2)
#     return list(set1 & set2)

# def peresech_lst(lst1, lst2):
#     res = []
#     for item in lst1:
#         if item in lst2:
#             res.append(item)
#     return res

# def measure_time(func, lst1, lst2, repeats = 5):
#     times = []
#     result = None
#     for _ in range(repeats):
#         start_time = time.time()
#         result = func(lst1, lst2)
#         end_time = time.time()
#         times.append(end_time - start_time)
#     return result, np.mean(times)

# sizes = [10, 100, 500, 1000, 2000, 5000, 10000]
# times_set = []
# times_naive = []

# for size in sizes:
#     arr1 = list(np.random.randint(0, size*2, size))
#     arr2 = list(np.random.randint(0, size*2, size))

#     result_set, time_set = measure_time(peresech_set, arr1, arr2)
#     times_set.append(time_set)

#     result_naive, time_naive = measure_time(peresech_lst, arr1, arr2)
#     times_naive.append(time_naive)

#     print(f"Размер: {size:>6} | Множество: {time_set:.6f}s | Наивный метод: {time_naive:.6f}s")

# plt.figure(figsize=(12, 7))
# plt.plot(sizes, times_set, label="Множество (O(n))", marker="o", color="green")
# plt.plot(sizes, times_naive, label="Двойной цикл (O(n²))", marker="s", color="red")

# plt.title("Сравнение времени нахождения пересечения двух списков")
# plt.xlabel("Размер списка")
# plt.ylabel("Время выполнения (секунды)")
# plt.xscale("linear")
# plt.yscale("linear")
# plt.grid(True, which="both", linestyle="--")
# plt.legend()
# plt.show()

#3
def del_dubl_set(lst):
    set1 = set(lst)
    return list(set1)

def del_dubl_list(lst):
    res = []
    for item in lst:
        if item not in res:
            res.append(item)
    return res

def measure_time(func, lst, repeats = 5):
    times = []
    result = None
    for _ in range(repeats):
        start_time = time.time()
        result = func(lst)
        end_time = time.time()
        times.append(end_time - start_time)
    return result, np.mean(times)

sizes = [10, 100, 500, 1000, 2000, 5000, 10000]
times_set = []
times_naive = []

for size in sizes:
    arr = list(np.random.randint(0, size*2, size))

    result_set, time_set = measure_time(del_dubl_set, arr)
    times_set.append(time_set)

    result_naive, time_naive = measure_time(del_dubl_list, arr)
    times_naive.append(time_naive)

    print(f"Размер: {size:>6} | Множество: {time_set:.6f}s | Наивный метод: {time_naive:.6f}s")

plt.figure(figsize=(12, 7))
plt.plot(sizes, times_set, label="Множество (O(n))", marker="o", color="green")
plt.plot(sizes, times_naive, label="Двойной цикл (O(n²))", marker="s", color="red")

plt.title("Сравнение времени удаления всех дубликатов из списка")
plt.xlabel("Размер списка")
plt.ylabel("Время выполнения (секунды)")
plt.xscale("linear")
plt.yscale("linear")
plt.grid(True, which="both", linestyle="--")
plt.legend()
plt.show()

#4
# def set_first_dubl(lst):
#     set1 = set()
#     for item in lst:
#         if item in set1:
#             return item
#         set1.add(item)
#     return False

# def list_first_dubl(lst):
#     for i in range(len(lst)):
#         for j in range(i + 1, len(lst)):
#             if lst[i] == lst[j]:
#                 return lst[i]
#     return False

# def measure_time(func, lst, repeats = 5):
#     times = []
#     result = None
#     for _ in range(repeats):
#         start_time = time.time()
#         result = func(lst)
#         end_time = time.time()
#         times.append(end_time - start_time)
#     return result, np.mean(times)

# sizes = [10, 100, 500, 1000, 2000, 5000, 10000]
# times_set = []
# times_naive = []

# for size in sizes:
#     arr = list(np.random.randint(0, size*2, size))

#     result_set, time_set = measure_time(set_first_dubl, arr)
#     times_set.append(time_set)

#     result_naive, time_naive = measure_time(list_first_dubl, arr)
#     times_naive.append(time_naive)

#     print(f"Размер: {size:>6} | Множество: {time_set:.6f}s | Наивный метод: {time_naive:.6f}s")

# plt.figure(figsize=(12, 7))
# plt.plot(sizes, times_set, label="Множество (O(n))", marker="o", color="green")
# plt.plot(sizes, times_naive, label="Двойной цикл (O(n²))", marker="s", color="red")

# plt.title("Сравнение времени нахождения первого повторяющегося элемента в списке")
# plt.xlabel("Размер списка")
# plt.ylabel("Время выполнения (секунды)")
# plt.xscale("linear")
# plt.yscale("linear")
# plt.grid(True, which="both", linestyle="--")
# plt.legend()
# plt.show()

#5
# def find_para_set(lst, value):
#     set1 = set(lst)
#     for item in lst:
#         number = value - item
#         if number in set1:
#             return (number, item)
#         set1.add(item)
#     return False

# def find_para_list(lst, value):
#     for i in range(len(lst)):
#         for j in range(i+1, len(lst)):
#             if lst[i] + lst[j] == value:
#                 return (lst[i], lst[j])
#     return False

# def measure_time(func, lst, value, repeats = 5):
#     times = []
#     result = None
#     for _ in range(repeats):
#         start_time = time.time()
#         result = func(lst, value)
#         end_time = time.time()
#         times.append(end_time - start_time)
#     return result, np.mean(times)

# sizes = [10, 100, 500, 1000, 2000, 5000, 10000]
# times_set = []
# times_naive = []

# for size in sizes:
#     arr = list(np.random.randint(0, size*2, size))
#     value = size*2

#     result_set, time_set = measure_time(find_para_set,arr, value)
#     times_set.append(time_set)

#     result_naive, time_naive = measure_time(find_para_list, arr, value)
#     times_naive.append(time_naive)

#     print(f"Размер: {size:>6} | Множество: {time_set:.6f}s | Наивный метод: {time_naive:.6f}s")

# plt.figure(figsize=(12, 7))
# plt.plot(sizes, times_set, label="Множество (O(n))", marker="o", color="green")
# plt.plot(sizes, times_naive, label="Двойной цикл (O(n²))", marker="s", color="red")

# plt.title("Сравнение времени нахождения пары чисел с заданной суммой")
# plt.xlabel("Размер списка")
# plt.ylabel("Время выполнения (секунды)")
# plt.xscale("linear")
# plt.yscale("linear")
# plt.grid(True, which="both", linestyle="--")
# plt.legend()
# plt.show()  


