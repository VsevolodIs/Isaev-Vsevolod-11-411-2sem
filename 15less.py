import time
import numpy as np

#1
# def nod(a, b):
#     if b == 0:
#         return a
#     else:
#         return nod(b, a % b)
    
# def measure_time(a, b, func, repeats=10):
#     times = []
#     result = None
#     for _ in range(repeats):
#         start_time = time.perf_counter()
#         result = func(a, b) 
#         end_time = time.perf_counter()
#         times.append(end_time - start_time)
#     return result, np.mean(times)

# a, b = 56, 98
# res, avg_time = measure_time(a, b, nod)
# print(f'НОД({a}, {b}) = {res}')
# print(f"Среднее время работы: {avg_time:.8f} секунд")

# a, b = 12345678901234567890, 987654321087654321
# res, avg_time = measure_time(a, b, nod)
# print(f'НОД({a}, {b}) = {res}')
# print(f"Среднее время работы: {avg_time:.8f} секунд")

#2
# class TreeNode: 
#     def __init__(self, value): 
#         self.value = value 
#         self.left = None 
#         self.right = None 
#         self.descendants = 0 

# def count_descendants(node):
#     if node == None:
#         return 0
    
#     left_descendants = count_descendants(node.left)
#     right_descendants = count_descendants(node.right)
    
#     node.descendants = left_descendants + right_descendants

#     return  node.descendants + 1

# def measure_time(tree, func, repeats=10):
#     times = []
#     result = None
#     for _ in range(repeats):
#         start_time = time.perf_counter()
#         result = func(tree) 
#         end_time = time.perf_counter()
#         times.append(end_time - start_time)
#     return result, np.mean(times)

# a = TreeNode('A') 
# b = TreeNode('B') 
# c = TreeNode('C') 
# d = TreeNode('D') 
# e = TreeNode('E') 
# a.left = b 
# a.right = c 
# b.left = d 
# b.right = e 

# result, avg_time = measure_time(a, count_descendants, repeats=1000)
# print(f'Среднее время работы: {avg_time * 1e6:.3f} микросекунд')

# def print_preorder(node): 
#     if node: 
#         print(f"Узел {node.value}: потомков = {node.descendants}") 
#         print_preorder(node.left) 
#         print_preorder(node.right)

# print_preorder(a) 

#3
# class Node:
#     def __init__(self, x):
#         self.data = x
#         self.left = None
#         self.right = None

# def isIsomorphic(root1, root2):
#     if root1 is None and root2 is None:
#         return True

#     if root1 is None or root2 is None:
#         return False

#     if root1.data != root2.data:
#         return False

#     return (isIsomorphic(root1.left, root2.left) and
#             isIsomorphic(root1.right, root2.right)) or \
#            (isIsomorphic(root1.left, root2.right) and
#             isIsomorphic(root1.right, root2.left))

# def measure_time(root1,root2, func, repeats=10):
#     times = []
#     result = None
#     for _ in range(repeats):
#         start_time = time.perf_counter()
#         result = func(root1, root2) 
#         end_time = time.perf_counter()
#         times.append(end_time - start_time)
#     return result, np.mean(times)

# root1 = Node(1)
# root1.left = Node(2)
# root1.right = Node(3)
# root1.left.left = Node(4)
# root1.left.right = Node(5)
# root1.left.right.left = Node(7)
# root1.left.right.right = Node(8)

# root2 = Node(1)
# root2.left = Node(3)
# root2.right = Node(2)
# root2.left.left = Node(6)
# root2.right.left = Node(4)
# root2.right.right = Node(5)
# root2.right.right.left = Node(8)
# root2.right.right.right = Node(7)

# result, avg_time = measure_time(root1, root2, isIsomorphic, repeats=1000)
# print(f'Деревья изоморфны: {result}')
# print(f'Среднее время работы: {avg_time * 1e6:.3f} микросекунд')

#4
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0  

def calculate_height(node):
    if node is None:
        return 0
    left_height = calculate_height(node.left)
    right_height = calculate_height(node.right)
    node.height = 1 + max(left_height, right_height)
    return node.height

def print_preorder(node):
    if node:
        print(f"Узел {node.value}: высота = {node.height}")
        print_preorder(node.left)
        print_preorder(node.right)

def measure_time(tree, func, repeats=10):
    times = []
    result = None
    for _ in range(repeats):
        start_time = time.perf_counter()
        result = func(tree) 
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    return result, np.mean(times)

a = TreeNode('A')
b = TreeNode('B')
c = TreeNode('C')
d = TreeNode('D')
e = TreeNode('E')
a.left = b
a.right = c
b.left = d
b.right = e

result, avg_time = measure_time(a, calculate_height, repeats=1000)
print(f"\nСреднее время работы: {avg_time * 1e6:.3f} микросекунд")

calculate_height(a)

print_preorder(a)
