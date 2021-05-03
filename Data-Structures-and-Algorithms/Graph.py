# references:
#   https://runestone.academy/runestone/books/published/pythonds/Graphs/toctree.html


from pythonds.graphs import Graph, Vertex, PriorityQueue
import sys


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
    # queue, first-in-first-out
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


# Knight’s Tour

# Building the Graph
def knightGraph(bdSize):
    ktGraph = Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = posToNodeId(row, col, bdSize)
            newPositions = genLegalMoves(row, col, bdSize)
            for e in newPositions:
                nid = posToNodeId(e[0], e[1], bdSize)
                ktGraph.addEdge(nodeId, nid)
    return ktGraph


def posToNodeId(row, column, board_size):
    return (row * board_size) + column


def genLegalMoves(x, y, bdSize):
    newMoves = []
    moveOffsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),
                   (1, -2), (1, 2), (2, -1), (2, 1)]
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        if (legalCoord(newX, bdSize) and
                legalCoord(newY, bdSize)):
            newMoves.append((newX, newY))
    return newMoves


def legalCoord(x, bdSize):
    if x >= 0 and x < bdSize:
        return True
    else:
        return False


# Implementing the Tour
# depth first search (DFS)
# n: the current depth in the search tree
# path: a list of vertices visited up to this point
# u: the vertex in the graph we wish to explore
# limit: the number of nodes in the path
def knightTour(n, path, u, limit):
    # visited vertices are colored gray
    u.setColor('gray')
    path.append(u)
    if n < limit:
        nbrList = list(u.getConnections())
        i = 0
        done = False
        # keep going
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == 'white':
                # self call
                done = knightTour(n+1, path, nbrList[i], limit)
            i = i + 1
        if not done:  # prepare to backtrack
            path.pop()
            u.setColor('white')
    # exit
    else:
        done = True
    return done


# inplace the call to u.getConnections
def orderByAvail(n):
    resList = []
    for v in n.getConnections():
        if v.getColor() == 'white':
            c = 0
            for w in v.getConnections():
                if w.getColor() == 'white':
                    c = c + 1
            resList.append((c, v))
    resList.sort(key=lambda x: x[0])
    return [y[1] for y in resList]


# DFS: General Depth First Search
class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)

    def dfsvisit(self, startVertex):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)


# TODO: Dijkstra's algorithm
def dijkstra(aGraph, start):
    pq = PriorityQueue()
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(), v) for v in aGraph])
    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() \
                    + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                nextVert.setDistance(newDist)
                nextVert.setPred(currentVert)
                pq.decreaseKey(nextVert, newDist)


# TODO: Prim's algorithm
def prim(G, start):
    pq = PriorityQueue()
    for v in G:
        v.setDistance(sys.maxsize)
        v.setPred(None)
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(), v) for v in G])
    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
            newCost = currentVert.getWeight(nextVert)
            if nextVert in pq and newCost < nextVert.getDistance():
                nextVert.setPred(currentVert)
                nextVert.setDistance(newCost)
                pq.decreaseKey(nextVert, newCost)
