import numpy as np
#1
arr1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print("Двумерный массив:")
print(arr1)

#2
arr2 = np.zeros((5, 5))
print("\nМассив из нулей:")
print(arr2)

#3
arr3 = np.ones((3, 6))
print("\nМассив из единиц:")
print(arr3)

#4
arr4 = np.eye(4)
print("\nЕдиничная матрица:")
print(arr4)

#5
arr5 = np.random.rand(2, 3)
print("\nМассив случайных чисел:")
print(arr5)

#6
arr6 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(f"\nКоличество осей: {arr6.ndim}")

#7
arr7 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(f"Форма массива: {arr7.shape}")

#8
arr8 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(f"Общее количество элементов: {arr8.size}")

#9
arr9 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"Тип данных элементов массива: {arr9.dtype}")

#10
arr10 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nИндексация элемента:")
print(arr10[1, 2])

#11
arr11 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print("\nСрез строки:")
print(arr11[1, :])

#12
arr12 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])
print("\nСрез столбца:")
print(arr12[:, 2])

#13
arr13 = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24], [25, 26, 27,28,29, 30], [31, 32, 33, 34,35, 36]])
print("\nСрез подмассива:")
print(arr13[0:3, 0:3])

#14
arr14 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nДвумерный массив, преобразованный в одномерный:")
print(arr14.flatten())

#15
arr15 = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])
arr_re = arr15.reshape(3, 4)
print("\nМассив, преобразованный в форму 3x4:")
print(arr_re)

#16
arr16_1 = np.array([[1, 2], [3, 4]])
arr16_2 = np.array([[5, 6], [7, 8]])
print("\nСложение двух массивов:")
print(arr16_1 + arr16_2)

#17
arr17 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nМассив, умноженный на 5:")
print(arr17 * 5)

#18
arr18_1 = np.array([[1, 2], [3, 4]])
arr18_2 = np.array([[5, 6], [7, 8]])
print("\nПоэлементное умножение массивов:")
print(arr18_1 * arr18_2)

#19
arr19 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print("\nСреднее значение массива:")
print(np.mean(arr19))

#20
arr20 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nСреднее значение по строкам:")
print(np.mean(arr20, axis=1))

#21
arr21 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])
print("\nСреднее значение по столбцам:")
print(np.mean(arr21, axis=0))

#22
arr22 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print('\n', 'Min:', np.min(arr22), 'Max:', np.max(arr22))

#23
arr23 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f'\nСумма всех элементов: {np.sum(arr23)}')

#24
arr24 = np.array([[1, 2, 3], [4, 5, 6]])
print("\nТранспонированный массив:")
print(arr24.T)

#25
arr25 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
np.save('array2d.npy', arr25)

#26
loaded_arr = np.load('array2d.npy')
print("\nЗагруженный двумерный массив из файла:")
print(loaded_arr)

#27
arr27 = np.array([[1, 2], [3, 4]])
np.savetxt('array.txt', arr27)

#28
loaded_arr_txt = np.loadtxt('array.txt')
print("\nЗагруженный массив из текстового файла:")
print(loaded_arr_txt)

#29
arr29 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nИтерация по строкам:")
for row in arr29:
    print(row)

#30
arr30 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("\nИтерация по элементам:")
for row in arr30:
    for el in row:
        print(el, end = ' ')
    print()