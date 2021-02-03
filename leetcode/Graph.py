# directed acyclic graph (DAG)

# 1. Adjacency Matrix
# 2. Adjacency List


class Vertex(object):
    def __init__(self, key):
        self.id = key
        self.connected_to = {}

    # nbr: neighbor
    def add_nbr(self, nbr, weight=0):
        self.connected_to[nbr] = weight


class Graph(object):
    def __init__(self):
        self.vertexes = {}

    def add_vertex(self, key):
        self.vertexes[key] = Vertex(key)

    def add_edge(self, key_from, key_toward, weight=0):
        if key_from not in self.vertexes:
            self.add_vertex(key_from)
        if key_toward not in self.vertexes:
            self.add_vertex(key_toward)
        self.vertexes[key_from].add_nbr(self.vertexes[key_toward], weight)

    def __iter__(self):
        return iter(self.vertexes.values())


# g = Graph()
# for i in range(6):
#     g.add_vertex(i)
# g.vertexes
# g.add_edge(0, 1, 5)
# g.add_edge(0, 5, 2)
# g.add_edge(1, 2, 4)
# g.add_edge(2, 3, 9)
# g.add_edge(3, 4, 7)
# g.add_edge(3, 5, 3)
# g.add_edge(4, 0, 1)
# g.add_edge(5, 4, 8)
# g.add_edge(5, 2, 1)
# for v in g:
#     for w in v.connected_to.keys():
#         print("( %s , %s )" % (v.id, w.id))
