import numpy as np
import time
import random
import matplotlib.pyplot as plt

#1
# string = '5 3 2 + 3 * +'
# stack = []
# for i in string.split():
#     if i.isdigit():
#         stack.append(int(i))
#     elif i in '+-*':
#         if len(stack) < 2:
#             raise ValueError('Недостаточно операндов для операции')
#         a = stack.pop()
#         b = stack.pop()
#         if i == '+':
#             stack.append(b + a)
#         elif i == '-':
#             stack.append(b - a)
#         elif i == '*':
#             stack.append(b * a)
#
# if len(stack) != 1:
#     raise ValueError('Некорректное выражение')
# else:
#     print(stack[0])


#2
def prav(string):
    stack = []
    for i in string:
        if i == '(':
            stack.append('(')
        else:
            if len(stack) == 0:
                return 'структура неправильная'
            else:
                stack.remove('(')
    
    if len(stack) == 0:
        return 'структура правильная'
    else:
        return 'структура неправильная'
    
print(prav('(((()))'))


#3
# def del_dubl(lst):
#     new_lst = [lst[0]]
#     for i in range(1, len(lst)):
#         if lst[i] != lst[i-1]:
#             new_lst.append(lst[i])
#     return new_lst
#
# def measure_time(func, lst, repeats = 10):
#     times = []
#     res = None
#     for _ in range(repeats):
#         start_time = time.perf_counter()
#         res = func(lst)
#         end_time = time.perf_counter()
#         times.append(end_time - start_time)
#     return res, np.mean(times)
#
# sizes = [1000, 5000, 10000, 20000, 50000, 100000]
# times_func = []
#
# for size in sizes:
#     lst = sorted([random.randint(1, size // 2) for _ in range(size)])
#     res, total_time = measure_time(del_dubl, lst)
#     times_func.append(total_time)
#
#     # print(f'Удаление дубликатов из сортированного списка {lst}: {res}')
#     print(f'Время выполнения (среднее), размера {size}: {total_time}')
#
# plt.figure(figsize=(12, 7))
# plt.plot(sizes, times_func, label = 'Алгортим', marker = "o", color = 'pink')
#
# plt.title('График зависимости времени выполнения программы от входных данных')
# plt.xlabel('Число')
# plt.ylabel('Время выполнения (секунды)')
# plt.xscale('log')
# plt.yscale('log')
# plt.grid(True, which = "both", linestyle = '--')
# plt.legend()
# plt.show()





