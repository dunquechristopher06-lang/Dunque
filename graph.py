from collections import deque


class UndirectedGraph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def bfs(self, start_node):
        """BFS using a Queue (visits neighbors in alphabetical order)."""
        visited = set([start_node])
        queue = deque([start_node])
        traversal_order = []

        while queue:
            current = queue.popleft()
            traversal_order.append(current)

            for neighbor in sorted(self.adj_list[current]):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return traversal_order

    def dfs(self, start_node):
        """DFS using a Stack (follows branch: D -> U -> N -> Q -> U2 -> E)."""
        visited = set()
        stack = [start_node]
        traversal_order = []

        while stack:
            current = stack.pop()

            if current not in visited:
                visited.add(current)
                traversal_order.append(current)

                # Push neighbors in alphabetical order so the later-alphabet
                # neighbor ('U' over 'E') sits on top of the stack and is visited first
                for neighbor in sorted(self.adj_list[current]):
                    if neighbor not in visited:
                        stack.append(neighbor)

        return traversal_order


if __name__ == "__main__":
    graph = UndirectedGraph()

    # Edges from diagram: D-U, U-N, N-Q, Q-U2, U2-E, E-D, and U-U2
    edges = [
        ("D", "U"),
        ("U", "N"),
        ("N", "Q"),
        ("Q", "U2"),
        ("U2", "E"),
        ("E", "D"),
        ("U", "U2"),
    ]

    for u, v in edges:
        graph.add_edge(u, v)

    print("=== 2. UNDIRECTED GRAPH (DUNQUE) ===")
    print("BFS (Starting at D) :", " -> ".join(graph.bfs("D")))
    print("DFS (Starting at D) :", " -> ".join(graph.dfs("D")))