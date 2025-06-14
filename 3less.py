import numpy as np
import time
import random

#1 с использованием numpy
# N, M = 10000, 10000
# A = np.random.randint(1, 10, size = (N, M))

# start_time = time.time()

# average = np.mean(A, axis = 1)
# max_m = np.max(average)

# end_time = time.time()

# print(f'Наибольшее среднее значение среди строк: {max_m}')
# print(f'Время выполнения программы: {end_time - start_time}')

#1 без numpy
# N, M = 10000, 10000
# A = np.random.randint(1, 10, size = (N, M))

# def calculate_average_list(matrix):
#     elements = [sum(row) / M for row in A]
#     max_m = max(elements)
#     return max_m

# start_time = time.time()
# print(f'Наибольшее среднее значение среди строк: {calculate_average_list(A)}')
# end_time = time.time()
# print(f'Время выполнения программы: {end_time - start_time}')

#2
# N, M = 10, 10
# A = np.random.randint(-10, 10, size = (N, M))

# print("Матрица A:")
# print(A)

# start_time = time.time()

# abs_row_sums = np.sum(np.abs(A), axis=1)
# print(abs_row_sums)

# max_sum_row_index = np.argmax(abs_row_sums)
# print(f"\nИндекс строки с максимальной суммой: {max_sum_row_index}")

# min_element = np.min(A[:, max_sum_row_index])
# print(f"\nНаименьший элемент: {min_element}")

# end_time = time.time()

# print(f"Время выполнения: {end_time - start_time} секунд")

#3
# N, M = 10000, 10000
# A = np.random.randint(1, 10, size = (N, M))

# start_time = time.time()

# average_col = np.mean(A, axis = 0)
# min_mean = np.min(average_col)

# end_time = time.time()

# print(f"Наименьшее среднее значение среди столбцов: {min_mean}")
# print(f"Время выполнения: {end_time - start_time} секунд")

#4
# N, M = 10000, 10000
# A = np.random.randint(1, 10, size = (N, M))

# start_time = time.time()

# mean_row = np.mean(A, axis = 0)
# mean_col = np.mean(A, axis = 1)
# mean_all = np.mean(A)

# end_time = time.time()

# print(f"Среднее значение по строкам: {mean_row}")
# print(f"Среднее значение по столбцам: {mean_col}")
# print(f"Среднее значение по всей матрице: {mean_all}")
# print(f"Время выполнения: {end_time - start_time} секунд")

#5
# N, M = 10000, 10000
# A = np.random.randint(1, 10, size = (N, M))
# b = random.randint(1, 10)

# subA = A[:100, :100]

# start_time = time.time()
# subA *= b
# end_time = time.time()

# print(f"Подматрица после умножения:\n{subA}")
# print(f"Время выполнения: {end_time - start_time} секунд")