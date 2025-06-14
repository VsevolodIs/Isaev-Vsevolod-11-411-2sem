import time
import random
import numpy as np

#1
# def find_vertex(graph):
#     V = len(graph)
#     visited = [False] * V
#     candidate = None

#     for v in range(0, V):
#         if not visited[v]:
#             dfs(graph, v, visited)
#             candidate = v

    
#     visited = [False] * V
#     dfs(graph, candidate, visited)

#     for v in range(0, V):
#         if not visited[v]:
#             return None
#     return candidate


# def dfs(graph, v, visited):
#     visited[v] = True
#     for neighbor in graph[v]:
#         if not visited[neighbor]:
#             dfs(graph, neighbor, visited)


# def generate_random_graph(V, edge_prob=0.3):
#     graph = [[] for _ in range(V)]
#     for i in range(V):
#         for j in range(V):
#             if i != j and random.random() < edge_prob:
#                 graph[i].append(j)
#     return graph


# def measure_time(func, V,  repeats=10):
#     x = generate_random_graph(V)
#     times = []
#     result = None
#     for _ in range(repeats):
#         x_copy = x.copy()
#         start_time = time.perf_counter()
#         result = func(x_copy)
#         end_time = time.perf_counter()
#         times.append(end_time - start_time)
#     return result, np.mean(times)

# V = 100
# result, avg_time = measure_time(find_vertex, V)

# print(f"Вершина для графа длиной {V}: ", result)
# print(f"Среднее время выполнения: {avg_time:.8f} секунд")


#2
# def find_i(a):
#     n = len(a)
#     candidate = 0

#     for i in range(1, n):
#         if a[candidate][i] == 1 or a[i][candidate] == 0:
#             candidate = i

#     for j in range(0, n):
#         if j != candidate and a[candidate][j] != 0:
#             return None
        
#     for i in range(0, n):
#         if i != candidate and a[i][candidate] != 1:
#             return None
        
#     return candidate

# def measure_time(func, a,  repeats=10):
#     times = []
#     result = None
#     for _ in range(repeats):
#         start_time = time.perf_counter()
#         result = func(a)
#         end_time = time.perf_counter()
#         times.append(end_time - start_time)
#     return result, np.mean(times)

# a = [ 
# [0, 1, 1, 1], 
# [0, 0, 0, 0], 
# [0, 1, 0, 1], 
# [0, 1, 1, 0] 
# ] 
# result, avg_time = measure_time(find_i, a)
# print(f"Найденная i: ", result)
# print(f"Среднее время выполнения: {avg_time:.8f} секунд")


#3
# def select(stones, k):
#     n = len(stones)

#     if n <= 5:
#         return sorted(stones)[k - 1]
    
#     groups = [stones[i: i+5] for i in range(0, n, 5)]

#     medians = []

#     for group in groups:
#         sorted_group = sorted(group)
#         m = len(group)
#         mid_index = m // 2
#         medians.append(sorted_group[mid_index])

#     pivot = select(medians, len(medians) // 2 + 1)

#     less = []
#     greater = []
#     equal = []

#     for stone in stones:
#         if stone < pivot:
#             less.append(stone)
#         elif stone == pivot:
#             equal.append(stone)
#         else:
#             greater.append(stone)
    
#     size_less = len(less)
#     size_equal = n - size_less - len(greater)

#     if k <= size_less:
#         return select(less, k)
#     elif k <= size_less + size_equal:
#         return pivot
#     else:
#         return select(greater, k - size_less - size_equal)
    
# def measure_time(func, a, k,  repeats=10):
#     times = []
#     result = None
#     for _ in range(repeats):
#         start_time = time.perf_counter()
#         result = func(a, k)
#         end_time = time.perf_counter()
#         times.append(end_time - start_time)
#     return result, np.mean(times)


# stones = [7, 2, 9, 4, 1, 5, 3, 6, 8]
# k = 4

# result, avg_time = measure_time(select, stones, k )
# print(f"Результат: {result}, Среднее время: {avg_time:.8f} сек")