import time
import math
import numpy as np

#1
# def LogFactorial(N):
#     if N == 0 or N == 1:
#         return 0
#     else:
#         return math.log(N, 2) + LogFactorial(N - 1)
    
# def measure_time(N, repeats = 10):
#     times = []
#     res = None
#     for _ in range(repeats):
#         start_time = time.perf_counter()
#         res = LogFactorial(N)
#         end_time = time.perf_counter()
#         times.append(end_time - start_time)
#     return res, np.mean(times)

# N = int(input())
# res, timee = measure_time(N)
# print(f'Среднее время выполнения для числа {N}: {timee:.8f}')
# print(f'Результат: {res}')

#2
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
    
#     def __repr__(self):
#         return f'Node({self.value})'

# def print_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> ")
#         current = current.next
#     print("None")

# def reverse_list(head):
#     if head is None or head.next is None:
#         return head
    
#     new_head = reverse_list(head.next)
    
#     head.next.next = head
#     head.next = None
    
#     return new_head

# def create_list(size):
#     if size == 0:
#         return None
#     head = Node(0)
#     current = head
#     for i in range(1, size):
#         current.next = Node(i)
#         current = current.next
#     return head

# def measure_time(size, repeats=10):
#     times = []
#     res_head = None
    
#     test_list = create_list(size)
    
#     for _ in range(repeats):
#         head_copy = create_list(size)
        
#         start_time = time.perf_counter()
#         res_head = reverse_list(head_copy)
#         end_time = time.perf_counter()
        
#         times.append(end_time - start_time)
    
#     return res_head, np.mean(times)

# if __name__ == "__main__":
#     size = int(input())

#     res_head, avg_time = measure_time(size)
#     print(f"Размер списка: {size:6}, Среднее время: {avg_time:.6f} сек")

#3
class TreeNode: 
    def __init__(self, value): 
        self.value = value 
        self.left = None 
        self.right = None 

def pre_order(node):
    if node:
        pre_order.result.append(node.value)
        pre_order(node.left)
        pre_order(node.right)

def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        post_order.result.append(node.value)

def in_order(node):
    if node:
        in_order(node.left)
        in_order.result.append(node.value)
        in_order(node.right)

def measure_time(tree, func,  repeats = 10):
    times = []
    func.result = []
    for _ in range(repeats):
        func.result = []
        start_time = time.perf_counter()
        func(tree)
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    return np.mean(times)


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)

print(f'Время выполнения для прямого обхода: {measure_time(tree, pre_order)}')
print(f'Время выполнения для обратного обхода: {measure_time(tree, post_order)}')
print(f'Время выполнения для центрированного  обхода: {measure_time(tree, in_order)}')