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