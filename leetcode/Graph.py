# directed acyclic graph (DAG)

# 1. Adjacency Matrix
# 2. Adjacency List


class Vertex(object):
    dist = None
    prev = None
    color = 'white'

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


# Word Ladder Problem
def build_graph(word_list):
    d = {}
    g = Graph()
    # create buckets of words that differ by one letter
    for word in word_list:
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.add_edge(word1, word2)
    return g


word_list = ['foil', 'fail', 'fall', 'pall', 'poll', 'pool',
             'cool', 'fool', 'foul', 'pole', 'pope', 'pale',
             'sale', 'page', 'sage']
g = build_graph(word_list)


# Breadth First Search (BFS)
# start is a Vertex
def bfs(start):
    start.dist = 0
    vert_queue = []
    vert_queue.append(start)
    while (len(vert_queue) > 0):
        vert_curr = vert_queue.pop()
        for nbr in vert_curr.connected_to:
            if nbr.color == 'white':
                nbr.color = 'gray'
                nbr.dist = vert_curr.dist + 1
                nbr.pred = vert_curr
                vert_queue.append(nbr)
        vert_curr.color = 'black'


bfs(g.vertexes['fool'])
g.vertexes['sage'].dist
