import time
import numpy as np

#1
# def has_hamiltonian_path(G):
#     top_order = topological_sort(G)

#     for i in range(len(top_order) - 2):
#         u = top_order[i]
#         v = top_order[i + 1]
#         if v not in G[u]:
#             return False
#     return True

# def dfs(v, G, visited, stack):
#     visited[v] = True
#     for neighbor in G.get(v, []):
#         if not visited[neighbor]:
#             dfs(neighbor, G, visited, stack)
#     stack.append(v)

# def topological_sort(G):
#     visited = [False] * len(G)
#     stack = []
    
#     for v in range(0, len(G) - 1):
#         if not visited[v]:
#             dfs(v, G, visited, stack)
#     return stack[::-1]

# def measure_time(func, G, repeats = 10):
#     times = []
#     result = None
#     for _ in range(repeats):
#         start_time = time.perf_counter()
#         result = func(G)
#         end_time = time.perf_counter()
#         times.append(end_time - start_time)
#     return np.mean(times), result

# # G = {
# #     0: [1],
# #     1: [2],
# #     2: [3],
# #     3: []
# # }
# # G = {
# #     0: [1, 2],
# #     1: [3],
# #     2: [3],
# #     3: []
# # }
# times, res = measure_time(has_hamiltonian_path, G)
# print(f"Гамильтонов путь существует: {res}")
# print(f"Время выполнения: {times:.6f} секунд")

#2
# def can_accommodate(bookings, K):
#     events = []

#     for (start, end) in bookings:
#         events.append((start, +1))
#         events.append((end, -1))

#     events.sort()

#     current_rooms = 0
#     for (day, change) in events:
#         current_rooms += change
#         if current_rooms > K:
#             return False
#     return True

# def measure_time(func, lst, K, repeats = 10):
#     times = []
#     result = None
#     for _ in range(repeats):
#         start_time = time.perf_counter()
#         result = func(lst, K)
#         end_time = time.perf_counter()
#         times.append(end_time - start_time)
#     return np.mean(times), result

# lst = [(1, 4), (2, 6), (4, 7)]
# K = 2

# times, res = measure_time(can_accommodate, lst, K)
# print(f"Получится ли заселить?: {res}")
# print(f"Время выполнения: {times:.6f} секунд")