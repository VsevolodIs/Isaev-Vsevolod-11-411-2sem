import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def dfs(graph, start):
    visited = set()
    stack = [start]
    poryadok = []

    while stack:
        top = stack.pop()
        if top not in visited:
            visited.add(top)
            poryadok.append(top)

            for i in reversed(graph[top]):
                if i not in visited:
                    stack.append(i)
    
    return poryadok

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    poryadok = []

    while queue:
        top = queue.popleft()

        if top not in visited:
            visited.add(top)
            poryadok.append(top)

            for i in graph[top]:
                if i not in visited:
                    queue.append(i)

    return poryadok

def show_undirected_graph():
    G = nx.Graph()

    edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('E', 'F')]
    G.add_edges_from(edges)

    plt.figure(figsize=(6, 4))
    nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1000, font_size=14)
    plt.title("Неориентированный граф")
    plt.show()

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    print("Неориентированный граф:")
    for vertex in graph:
        print(f"{vertex}: {graph[vertex]}")

    print("\nОбход в глубину DFS")
    print(dfs(graph, 'A'))

    print("\nОбход в ширину BFS")
    print(bfs(graph, 'A'))

    show_undirected_graph()