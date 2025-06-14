#1
# def task1(file_path):
#     stack = []

#     with open(file_path, 'r', encoding='utf-8') as file:
#         for line in file:
#             words = line.strip().split()
#             stack.extend(words)

#     while stack:
#         print(stack.pop(), end = ' ')

# task1('text.txt')

#2
# def task2(lst):
#     n = len(lst)
#     result = n * [0]
#     stack = []

#     for i in range(n):
#         while stack and lst[stack[-1]] >= lst[i]:
#             stack.pop()

#         if stack:
#             result[i] = stack[-1] + 1
#         else:
#             result[i] = 0
#         stack.append(i)

#     return result

# print(task2([1, 2, 45, 65, 21, 45, 2, 1]))