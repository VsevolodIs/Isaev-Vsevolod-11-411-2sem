import numpy as np
import time
import matplotlib.pyplot as plt

# 1
def calculate_max_average_numpy(matrix):
    average = np.mean(matrix, axis = 1)
    max_m = np.max(average)
    return max_m

def calculate_max_average_list(matrix):
    elements = [sum(row) / len(row) for row in matrix]
    max_m = max(elements)
    return max_m

def measure_time(func, matrix, repeats = 5):
    if repeats <= 0:
        raise ValueError("Количество повторений должно быть больше 0")

    times = []
    result = None

    for _ in range(repeats):
        start_time = time.time()
        result = func(matrix)
        end_time = time.time()
        times.append(end_time - start_time)
    return result, np.mean(times), min(times), max(times)

sizes = [5, 10, 50, 100, 1000, 10_000, 20_000]

times_numpy_mean = []
times_numpy_min = []
times_numpy_max = []

times_list_mean = []
times_list_min = []
times_list_max = []

for size in sizes:
    N, M = size, size
    A = np.random.randint(1, 10, size = (N, M))

    A_list = A.tolist()

    average_numpy, mean_time_numpy, min_time_numpy, max_time_numpy = measure_time(calculate_max_average_numpy, A, repeats = 5)
    times_numpy_mean.append(mean_time_numpy)
    times_numpy_min.append(min_time_numpy)
    times_numpy_max.append(max_time_numpy)

    average_list, mean_time_list, min_time_list, max_time_list = measure_time(calculate_max_average_list, A_list, repeats=5)
    times_list_mean.append(mean_time_list)
    times_list_min.append(min_time_list)
    times_list_max.append(max_time_list)

    print(f"Размер матрицы: {size}x{size}")
    print(f"Наибольшее среднее арифметическое для NumPy массива: {average_numpy}")
    print(f"Среднее время выполнения для NumPy массива: {mean_time_numpy:.7f} секунд")
    print(f"Минимальное время выполнения для NumPy массива: {min_time_numpy:.7f} секунд")
    print(f"Максимальное время выполнения для NumPy массива: {max_time_numpy:.7f} секунд")
    print()

    print(f"Наибольшее среднее арифметическое для списка: {average_list}")
    print(f"Среднее время выполнения для списка: {mean_time_list:.7f} секунд")
    print(f"Минимальное время выполнения для списка: {min_time_list:.7f} секунд")
    print(f"Максимальное время выполнения для списка: {max_time_list:.7f} секунд")
    print()

plt.figure(figsize = (10, 6))

plt.plot(sizes, times_numpy_mean, label="NumPy (среднее)", marker="o")

plt.plot(sizes, times_list_mean, label="Список (среднее)", marker="o")

plt.xlabel("Размер матрицы (N x N)")
plt.ylabel("Время выполнения (секунды)")

plt.title("Зависимость времени выполнения от размера матрицы")

plt.legend()

plt.grid(True)

plt.xscale("log")
plt.yscale("log")

plt.show()


# # 2
# def min_element_numpy(matrix):
#     abs_row_sums = np.sum(np.abs(matrix), axis = 1)
#     max_sum_row_index = np.argmax(abs_row_sums)
#     min_element = np.min(matrix[max_sum_row_index, :])
#     return min_element
#
# def min_element_list(matrix):
#     abs_row_sums = [sum(abs(x) for x in row) for row in matrix]
#     max_sum_row_index = abs_row_sums.index(max(abs_row_sums))
#     min_element = min(matrix[max_sum_row_index])
#     return min_element
#
# def measure_time(func, matrix, repeats = 5):
#     if repeats <= 0:
#         raise ValueError("Количество повторений должно быть больше 0")
#
#     times = []
#     result = None
#
#     for _ in range(repeats):
#         start_time = time.time()
#         result = func(matrix)
#         end_time = time.time()
#         times.append(end_time - start_time)
#     return result, np.mean(times), min(times), max(times)
#
# sizes = [5, 10, 50, 100, 1000, 10_000, 20_000]
#
# times_numpy_mean = []
# times_numpy_min = []
# times_numpy_max = []
#
# times_list_mean = []
# times_list_min = []
# times_list_max = []
#
# for size in sizes:
#     N, M = size, size
#     A = np.random.randint(1, 10, size = (N, M))
#
#     A_list = A.tolist()
#
#     average_numpy, mean_time_numpy, min_time_numpy, max_time_numpy = measure_time(min_element_numpy, A, repeats = 5)
#     times_numpy_mean.append(mean_time_numpy)
#     times_numpy_min.append(min_time_numpy)
#     times_numpy_max.append(max_time_numpy)
#
#     average_list, mean_time_list, min_time_list, max_time_list = measure_time(min_element_list, A_list, repeats=5)
#     times_list_mean.append(mean_time_list)
#     times_list_min.append(min_time_list)
#     times_list_max.append(max_time_list)
#
#     print(f"Размер матрицы: {size}x{size}")
#     print(f"Наименьший элемент строки для которого сумма абс. знач. максимальна для NumPy массива: {average_numpy}")
#     print(f"Среднее время выполнения для NumPy массива: {mean_time_numpy:.7f} секунд")
#     print(f"Минимальное время выполнения для NumPy массива: {min_time_numpy:.7f} секунд")
#     print(f"Максимальное время выполнения для NumPy массива: {max_time_numpy:.7f} секунд")
#     print()
#
#     print(f"Наименьший элемент строки для которого сумма абс. знач. максимальна для списка: {average_list}")
#     print(f"Среднее время выполнения для списка: {mean_time_list:.7f} секунд")
#     print(f"Минимальное время выполнения для списка: {min_time_list:.7f} секунд")
#     print(f"Максимальное время выполнения для списка: {max_time_list:.7f} секунд")
#     print()
#
# plt.figure(figsize = (10, 6))
#
# plt.plot(sizes, times_numpy_mean, label="NumPy (среднее)", marker="o")
#
# plt.plot(sizes, times_list_mean, label="Список (среднее)", marker="o")
#
# plt.xlabel("Размер матрицы (N x N)")
# plt.ylabel("Время выполнения (секунды)")
#
# plt.title("Зависимость времени выполнения от размера матрицы")
#
# plt.legend()
#
# plt.grid(True)
#
# plt.xscale("log")
# plt.yscale("log")
#
# plt.show()
#
# # 3
# def min_average_numpy(matrix):
#     average_col = np.mean(matrix, axis = 0)
#     min_mean = np.min(average_col)
#     return min_mean
#
# def measure_time(func, matrix, repeats = 5):
#     if repeats <= 0:
#         raise ValueError("Количество повторений должно быть больше 0")
#
#     times = []
#     result = None
#
#     for _ in range(repeats):
#         start_time = time.time()
#         result = func(matrix)
#         end_time = time.time()
#         times.append(end_time - start_time)
#     return result, np.mean(times), min(times), max(times)
#
# sizes = [5, 10, 50, 100, 1000, 10_000, 20_000]
#
# times_numpy_mean = []
# times_numpy_min = []
# times_numpy_max = []
#
# for size in sizes:
#     N, M = size, size
#     A = np.random.randint(1, 10, size = (N, M))
#
#     average_numpy, mean_time_numpy, min_time_numpy, max_time_numpy = measure_time(min_average_numpy, A, repeats = 5)
#     times_numpy_mean.append(mean_time_numpy)
#     times_numpy_min.append(min_time_numpy)
#     times_numpy_max.append(max_time_numpy)
#
#     print(f"Размер матрицы: {size}x{size}")
#     print(f"Наименьшее значение среди средних значений для каждого столбца для NumPy массива: {average_numpy}")
#     print(f"Среднее время выполнения для NumPy массива: {mean_time_numpy:.7f} секунд")
#     print(f"Минимальное время выполнения для NumPy массива: {min_time_numpy:.7f} секунд")
#     print(f"Максимальное время выполнения для NumPy массива: {max_time_numpy:.7f} секунд")
#     print()
#
#
# plt.figure(figsize = (10, 6))
#
# plt.plot(sizes, times_numpy_mean, label="NumPy (среднее)", marker="o")
#
# plt.xlabel("Размер матрицы (N x N)")
# plt.ylabel("Время выполнения (секунды)")
#
# plt.title("Зависимость времени выполнения от размера матрицы")
#
# plt.legend()
#
# plt.grid(True)
#
# plt.xscale("log")
# plt.yscale("log")
#
# plt.show()
#
# # 4
# def mean_of_matrix(matrix):
#     mean_row = np.mean(matrix, axis = 1)
#     mean_col = np.mean(matrix, axis = 0)
#     mean_all = np.mean(matrix)
#     return mean_row, mean_col, mean_all
#
# def measure_time(func, matrix, repeats = 5):
#     if repeats <= 0:
#         raise ValueError("Количество повторений должно быть больше 0")
#
#     times = []
#     res_mean_row = None
#     res_mean_col = None
#     res_mean_all = None
#
#     for _ in range(repeats):
#         start_time = time.time()
#         res_mean_row, res_mean_col, res_mean_all = func(matrix)
#         end_time = time.time()
#         times.append(end_time - start_time)
#     return res_mean_row, res_mean_col, res_mean_all, np.mean(times), min(times), max(times)
#
# sizes = [5, 10, 50, 100, 1000, 10_000, 20_000]
#
# times_numpy_mean = []
# times_numpy_min = []
# times_numpy_max = []
#
# for size in sizes:
#     N, M = size, size
#     A = np.random.randint(1, 10, size = (N, M))
#
#     res_mean_row, res_mean_col, res_mean_all, mean_time_numpy, min_time_numpy, max_time_numpy = measure_time(mean_of_matrix, A, repeats = 5)
#     times_numpy_mean.append(mean_time_numpy)
#     times_numpy_min.append(min_time_numpy)
#     times_numpy_max.append(max_time_numpy)
#
#     print(f"Размер матрицы: {size}x{size}")
#     print(f"Cредние значения по всем строкам, столбцам матрицы и по всей матрицы для NumPy массива: {res_mean_row, res_mean_col, res_mean_all}")
#     print(f"Среднее время выполнения для NumPy массива: {mean_time_numpy:.7f} секунд")
#     print(f"Минимальное время выполнения для NumPy массива: {min_time_numpy:.7f} секунд")
#     print(f"Максимальное время выполнения для NumPy массива: {max_time_numpy:.7f} секунд")
#     print()
#
#
# plt.figure(figsize = (10, 6))
#
# plt.plot(sizes, times_numpy_mean, label="NumPy (среднее)", marker="o")
#
# plt.xlabel("Размер матрицы (N x N)")
# plt.ylabel("Время выполнения (секунды)")
#
# plt.title("Зависимость времени выполнения от размера матрицы")
#
# plt.legend()
#
# plt.grid(True)
#
# plt.xscale("log")
# plt.yscale("log")
#
# plt.show()
#
# # 5
# def multiply_submatrix(matrix, sub_rows=100, sub_cols=100, multiplier=5):
#     rows = min(matrix.shape[0], sub_rows)
#     cols = min(matrix.shape[1], sub_cols)
#     submatrix = matrix[:rows, :cols]
#     submatrix *= multiplier
#     return matrix
#
# def measure_time(func, matrix, repeats = 5):
#     if repeats <= 0:
#         raise ValueError("Количество повторений должно быть больше 0")
#
#     times = []
#     result = None
#
#     for _ in range(repeats):
#         start_time = time.time()
#         result = func(matrix.copy())
#         end_time = time.time()
#         times.append(end_time - start_time)
#     return result, np.mean(times), min(times), max(times)
#
# sizes = [5, 10, 50, 100, 1000, 10_000, 20_000]
#
# times_numpy_mean = []
# times_numpy_min = []
# times_numpy_max = []
#
# for size in sizes:
#     N, M = size, size
#     A = np.random.randint(1, 10, size = (N, M))
#
#     average_numpy, mean_time_numpy, min_time_numpy, max_time_numpy = measure_time(multiply_submatrix, A, repeats = 5)
#     times_numpy_mean.append(mean_time_numpy)
#     times_numpy_min.append(min_time_numpy)
#     times_numpy_max.append(max_time_numpy)
#
#     print(f"Размер матрицы: {size}x{size}")
#     print(f"Подматрица после умножения для NumPy массива: {average_numpy}")
#     print(f"Среднее время выполнения для NumPy массива: {mean_time_numpy:.7f} секунд")
#     print(f"Минимальное время выполнения для NumPy массива: {min_time_numpy:.7f} секунд")
#     print(f"Максимальное время выполнения для NumPy массива: {max_time_numpy:.7f} секунд")
#     print()
#
#
# plt.figure(figsize = (10, 6))
#
# plt.plot(sizes, times_numpy_mean, label="NumPy (среднее)", marker="o")
#
# plt.xlabel("Размер матрицы (N x N)")
# plt.ylabel("Время выполнения (секунды)")
#
# plt.title("Зависимость времени выполнения от размера матрицы")
#
# plt.legend()
#
# plt.grid(True)
#
# plt.xscale("log")
# plt.yscale("log")
#
# plt.show()