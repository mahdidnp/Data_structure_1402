class Node:
    def __init__(self, neighbor):
        self.neighbor = neighbor
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_edge(self, neighbor):
        new_node = Node(neighbor)
        new_node.next = self.head
        self.head = new_node

    def remove_edge(self, neighbor):
        this_node = self.head
        if this_node and this_node.neighbor == neighbor:
            self.head = this_node.next
            return
        while this_node.next:
            if this_node.next.neighbor == neighbor:
                this_node.next = this_node.next.next
                return
            this_node = this_node.next

    def display(self):
        this_node = self.head
        while this_node:
            print(f"{this_node.neighbor} -> ", end='')
            this_node = this_node.next
        print("None")


class Graph:
    def __init__(self):
        self.vertex = {}
        self.size = 0

    def add_vertex(self, vertex):
        if vertex not in self.vertex:
            self.vertex[vertex] = LinkedList()
            self.size += 1
            return True
        else:
            return False

    def remove_vertex(self, vertex):
        if vertex not in self.vertex:
            return False
        else:
            del self.vertex[vertex]
            self.size -= 1
            for otherVertex, linkedList in self.vertex.items():
                linkedList.remove_edge(vertex)
            return True

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertex and vertex2 in self.vertex:
            self.vertex[vertex1].add_edge(vertex2)
            self.vertex[vertex2].add_edge(vertex1)
            return True
        else:
            return False

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.vertex and vertex2 in self.vertex:
            self.vertex[vertex1].remove_edge(vertex2)
            self.vertex[vertex2].remove_edge(vertex1)
            return True
        else:
            return False

    def dfs_display(self, start, visited=None):
        if visited is None:
            visited = set()

        visited.add(start)
        print(start, end=' ')

        this_node = self.vertex[start].head
        while this_node:
            neighbor = this_node.neighbor
            if neighbor not in visited:
                self.dfs_display(neighbor, visited)
            this_node = this_node.next

    def display(self):
        for vertex, linkedList in self.vertex.items():
            print(f"Vertex {vertex}: ", end='')
            linkedList.display()

    def bfs_display(self, start, visited=None):
        if not visited :
            visited = set()
        queue = []
        queue.append(start)
        visited.add(start)
        while queue:
            s = queue.pop()
            print(s, end=" ")
            this_node = self.vertex[s].head
            while this_node:
                neighbor = this_node.neighbor
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
                this_node = this_node.next
        print()

# Test :


g = Graph()
g.add_vertex(0)
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
# g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

g.remove_vertex(1)

g.display()
# g.dfs_display(2)
# print()
# g.bfs_display(2)
