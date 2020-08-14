"""
Kosaraju's algorithm for determination of strongly connected components of graph.
Uses Depth First Search twice
Note that the implementation of DFS has to iterative because of Python.
"""
import random

class Node:
    def __init__(self, value):
        self._value = value
        self._in_arrows = set()
        self._out_arrows = set()
        self._explored = False

    def __str__(self):
        s = "Node: {}. Visited: {}.Out: {}. In: {}\n".format(self._value, self._explored, self._out_arrows, self._in_arrows)
        return s

    def add_in_arrow(self, node):
        self._in_arrows.add(node)

    def add_out_arrow(self, node):
        self._out_arrows.add(node)

    def is_explored(self):
        return self._explored

    def set_explored(self):
        self._explored = True


def build_test_graph(edge_tuple):
    graph = {}
    for edge in edge_tuple:
        head = edge[0]
        tail = edge[1]
        if head not in graph:
            graph[head] = Node(head)
        graph[head].add_out_arrow(tail)
        if tail not in graph:
            graph[tail] = Node(tail)
        graph[tail].add_in_arrow(head)
    return graph

test1 = ((1, 4), (2,8),(3, 6), (4,7),(5,2), (6,9), (7,1), (8,5),(8,6),(9,7),(9,3))
test2 = ((1, 2), (2, 6), (2,3), (2, 4), (3, 1), (3, 4), (4, 5), (5, 4), (6, 5), (6, 7), (7, 6), (7, 8), (8,5), (8,7))
test3 = ((1, 2), (2, 3), (3, 1), (3 ,4), (5, 4), (6, 4), (8, 6), (6 ,7), (7 ,8))
test4 = ((1,2), (2,3), (3,1), (3,4), (5,4), (6,4),(8,6),(6,7),(7,8),(4,3),(4,6))
test5 = ((1, 2), (2, 3), (2, 4),(2, 5),(3, 6),(4, 5),(4, 7),(5, 2), (5, 6), (5, 7), (6, 3), (6, 8), (7, 8), (7, 10), (8, 7), (9, 7), (10, 9), (10, 11), (11, 12), (12, 10))
test6 = ((5,4),(1,4),(1,2),(2,3),(3,1))
test7 = ((5,4),(1,4),(1,2),(2,3),(3,1),(6,7),(7,6),(7,8),(8,7),(8,9),(9,8))
test8 = ((5,4),(1,4),(1,2),(2,3),(3,1),(6,7),(7,6),(7,8),(8,7),(8,9),(9,8),(6,3))

#problems:
test9 = ((5,4),(1,4),(1,2),(2,3),(3,1),(6,7),(7,6),(7,8),(8,7),(8,9),(9,8),(6,3),(4,6),(10,11),(10,5),(11,6), (11,100), (100,10))
test11 = ((5,4),(1,4),(1,2),(2,3),(3,1),(6,3),(4,6),(10,11),(10,5),(11,6),(11,100), (100,10))
test12 = ((5,4),(1,4),(3,1),(6,3),(4,6),(10,11),(10,5),(11,6),(11,100), (100,10))
#korrekt
test13 = ((5,4),(6,3),(4,6),(10,11),(10,5),(11,6),(11,1), (1,10), (3,4))
#forkert
test14 = ((5,4),(6,3),(4,6),(10,11),(10,5),(11,6),(11,100), (100,10), (3,4))

test15 = ((5,4),(6,4),(4,6),(10,11),(10,5),(11,6),(11,100), (100,10))


graph1 = build_test_graph(test1)
graph2 = build_test_graph(test2)
graph3 = build_test_graph(test3)
graph4 = build_test_graph(test4)
graph5 = build_test_graph(test5)
graph6 = build_test_graph(test6)
graph7 = build_test_graph(test7)
graph8 = build_test_graph(test8)
graph8 = build_test_graph(test8)
graph9 = build_test_graph(test9)
#graph10 = build_test_graph(test10)
graph11 = build_test_graph(test11)
graph12 = build_test_graph(test12)
graph13 = build_test_graph(test13)
graph14 = build_test_graph(test14)
graph15 = build_test_graph(test15)


def build_graph_from_file():
    fh = open('graph_data.txt')
    data = fh.read()
    print "Read data from file"
    data_lines = data.split('\n')
    graph = {}
    rev_graph = {}
    for line in data_lines:
#        print line
        line = line.split()
        head = int(line[0])
        tail = int(line[1])
        if head not in graph:
            graph[head] = Node(head)
        graph[head].add_out_arrow(tail)
        if tail not in graph:
            graph[tail] = Node(tail)
        graph[tail].add_in_arrow(head)
    print "Graph constructed from loaded data"
    return graph
#build_graph_from_file()

def build_graph_from_url():
    """
    Load data and build undirected graph with desired data_structure.
    {1: (set([1,4,5]), UNVISITED), 2: ...}

    NB: The graph in question has no parallel edges, so I use sets to store tails for edges.
    The graph does have self-loops

    """
    import urllib2
    url = "https://d3c33hcgiwev3.cloudfront.net/_410e934e6553ac56409b2cb7096a44aa_SCC.txt?Expires=1514937600&Signature=MSp-2k-rHk0-Gr6yP3mhkQqnYH2GqSpfyr5R6NKXTittXVb80-4kqHA8hbwtuDbUu5LwUe6QE1mocYsD89BY6pbLh71E5i4FUHxEdpHTY27FmkDkAPIBWSSncEWYOAuG3VrffbYygoqga0idXQCkXPEMR26xkHH8qKEdfs5ybeE_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A"
    data_file =  urllib2.urlopen(url)
    print "Opened file"
    data = data_file.read()
    print "Read data from url"
    data_lines = data.split('\n')
    graph = {}
    rev_graph = {}
    for line in data_lines:
        line = line.split()
        head = int(line[0])
        tail = int(line[1])
        if head not in graph:
            graph[head] = Node(head)
        graph[head].add_out_arrow(tail)
        if tail not in graph:
            graph[tail] = Node(tail)
        graph[tail].add_in_arrow(head)
    print "Graph constructed from data"
    return graph
#build_graph_from_url()

def dfs_reversed(graph, start_node):
    """
    Depth first search, modified to be used in detection of strongly connected components of graph.
    Graph is a dictionary of nodes
    """
    stack = [start_node]

    while stack != []:
        node = stack[-1]
        node.set_explored()
        end_track = True

        for neighbor in node._in_arrows:
            neighbor_node = graph[neighbor]
            if not neighbor_node.is_explored():
                stack.append(neighbor_node)
                end_track = False
                break
                #Note that only one neighbor gets appended to stack.

        if end_track:
            stack.pop()
            FINISH_ORDER.append(node)

def first_loop(graph):
    global FINISH_ORDER
    FINISH_ORDER = []

    for node in graph.values():
        if not node._explored:
            dfs_reversed(graph, node)


def dfs_un_reversed(graph, start_node):
    """
    Depth first search, modified to be used in detection of strongly connected components of graph.
    Graph is a dictionary of nodes
    """
    stack = [start_node]

    LEADERS[LEADER] = set()

    while stack != []:
        node = stack[-1]
        node.set_explored()
        end_track = True
        LEADERS[LEADER].add(node._value)

        for neighbor in node._out_arrows:
            neighbor_node = graph[neighbor]
            if not neighbor_node.is_explored():
                stack.append(neighbor_node)
                end_track = False
                break
                #Note that only one neighbor gets appended to stack.

        if end_track:
             end_node = stack.pop()

def second_loop(graph):
    global LEADERS, LEADER
    LEADERS = {}
    LEADER = None
    length = len(FINISH_ORDER)

    for indx in range(length - 1, -1, -1):
        node = FINISH_ORDER[indx]
        if not node.is_explored():
            LEADER = node._value
            dfs_un_reversed(graph, node)

def scc(graph):
    print "Starting first loop"
    first_loop(graph)
    print "Done with first loop"
    for node in graph:
        graph[node]._explored = False
    second_loop(graph)
    print "Done with second loop"
    lst = []

    for key, val in LEADERS.items():
        lst.append(len(val))

    print "Number of SCC's:", len(LEADERS)

    lst.sort(reverse = True)
    if len(lst) < 20:
        print lst
    else:
        print lst[:20]

real_graph = build_graph_from_file()
scc(real_graph)

#scc(graph9)
#scc(graph15)
