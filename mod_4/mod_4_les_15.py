from collections import deque

class Node:
    def __init__(self, value):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other):
        self.outbound.append(other)
        other.inbound.append(self)

    def __repr__(self):
        return f'Node({self.value})'

class Graph:
    def __init__(self, root):
        self._root = root

    def dfs(self, vertex=None, visited=None):
        if visited is None:
            visited = []
        if vertex is None:
            vertex = self._root

        if vertex not in visited:
            visited.append(vertex)
            for neighbor in vertex.outbound:
                self.dfs(neighbor, visited)
        return visited

    def bfs(self):
        start = self._root
        visited = []
        queue = deque()

        queue.append(start)
        visited.append(start)

        while queue:
            vertex = queue.popleft()
            
            for neighbor in vertex.outbound:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.append(neighbor)
        return visited




a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
a.point_to(b)
b.point_to(c)
c.point_to(d)
d.point_to(a)
b.point_to(d)

g = Graph(a)

# print(g.dfs())
print(g.bfs())