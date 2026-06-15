#Task1
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {i: [] for i in range(vertices)}

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_fill_order(self, v, visited, stack):
        visited[v] = True

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs_fill_order(neighbor, visited, stack)

        stack.append(v)

    def dfs(self, v, visited, component):
        visited[v] = True
        component.append(v)

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, component)

    def transpose(self):
        g = Graph(self.V)

        for vertex in self.graph:
            for neighbor in self.graph[vertex]:
                g.add_edge(neighbor, vertex)

        return g

    def strongly_connected_components(self):
        stack = []
        visited = [False] * self.V

        # Шаг 1
        for i in range(self.V):
            if not visited[i]:
                self.dfs_fill_order(i, visited, stack)

        # Шаг 2
        transposed = self.transpose()

        # Шаг 3
        visited = [False] * self.V
        scc_list = []

        while stack:
            vertex = stack.pop()

            if not visited[vertex]:
                component = []
                transposed.dfs(vertex, visited, component)
                scc_list.append(component)

        return scc_list
# Проверка
if __name__ == "__main__":
    g = Graph(5)

    g.add_edge(1, 0)
    g.add_edge(0, 2)
    g.add_edge(2, 1)
    g.add_edge(0, 3)
    g.add_edge(3, 4)

    scc = g.strongly_connected_components()

    print("Strongly Connected Components:")
    for component in scc:
        print(component)

#Task2

from collections import deque


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []

        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u)  # неориентированный граф

    def bfs_shortest_paths(self, start):
        distances = {vertex: float("inf") for vertex in self.graph}

        distances[start] = 0

        queue = deque([start])

        while queue:
            current = queue.popleft()

            for neighbor in self.graph[current]:
                if distances[neighbor] == float("inf"):
                    distances[neighbor] = distances[current] + 1
                    queue.append(neighbor)

        return distances

    def all_pairs_shortest_paths(self):
        result = {}

        for vertex in self.graph:
            result[vertex] = self.bfs_shortest_paths(vertex)

        return result

# Проверка

if __name__ == "__main__":

    g = Graph()

    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("C", "D")
    g.add_edge("D", "E")

    paths = g.all_pairs_shortest_paths()

    for start_vertex, distances in paths.items():
        print(f"\nВідстані від вершини {start_vertex}:")
        for end_vertex, distance in distances.items():
            print(f"{start_vertex} -> {end_vertex}: {distance}")