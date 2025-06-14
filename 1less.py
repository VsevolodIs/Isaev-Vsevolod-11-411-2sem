import numpy as np

#1
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Одномерный массив:")
print(arr1)

#2
arr2 = np.zeros(7)
print("\nМассив из нулей:")
print(arr2)

#3
arr3 = np.ones(5)
print("\nМассив из единиц:")
print(arr3)

#4
arr4 = np.arange(10, 50, 5)
print("\nМассив с последовательностью чисел:")
print(arr4)

#5
arr5 = np.linspace(0, 100, 6)
print("\nМассив с линейно распределенными числами:")
print(arr5)

#6
arr6 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
second_element = arr6[1]
last_element = arr6[-1]
elements_3_to_6 = arr6[3:7]

print("\nВторой элемент:", second_element)
print("Последний элемент:", last_element)
print("Элементы с индексами от 3 до 6:", elements_3_to_6)

#7
arr7 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
for i in arr7:
    print(i)

#8
arr8 = np.array([1, 2, 3])
arr9 = np.array([4, 5, 6])
result = arr8 + arr9
print("\nСложение массивов:", result)

#9
scaled_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
result = scaled_arr * 2
print("\nУмножение на 2:", result)

#10
squared_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
result = squared_arr ** 2
print("\nВозведение в квадрат:", result)

#11
stats_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f'\nМинимальное: {np.min(stats_arr)}')
print(f'Максимальное: {np.max(stats_arr)}')

#12
analytics_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
arr_mean = np.mean(analytics_arr)
arr_std = np.std(analytics_arr)
print("\nСреднее значение массива:")
print(arr_mean)
print("\nСтандартное отклонение массива:")
print(arr_std)

#13
arr13 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
arr_sin = np.sin(arr13)
arr_exp = np.exp(arr13)
arr_log = np.log(arr13)
print("\nСинус элементов массива:")
print(arr_sin)
print("\nЭкспонента элементов массива:")
print(arr_exp)
print("\nЛогарифм элементов массива:")
print(arr_log)

#14
arr14 = np.random.rand(10)
print("\nМассив случайных чисел от 0 до 1:")
print(arr14)

#15
arr15 = np.random.randint(1, 100, size = 6)
print("\nМассив случайных целых чисел от 1 до 100:")
print(arr15)

#16
arr16 = arr1.reshape(2, 5)
print("\nДвумерный массив:")
print(arr16)

#17
arr17 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
arr2d_1 = arr17.reshape(3, 3)
print("\nДвумерный массив:")
print(arr2d_1)

#18
arr_condition = arr1 > 5
print("\nБулевый массив:")
print(arr_condition)

#19
vectorized_func = np.vectorize(lambda x: x ** 3)
arr19 = vectorized_func(arr1)
print("\nПрименение функции ко всем элементам:")
print(arr19)

#20
np.save('array.npy', arr1)
loaded_arr = np.load('array.npy')
print("\nЗагруженный одномерный массив из файла:")
print(loaded_arr)