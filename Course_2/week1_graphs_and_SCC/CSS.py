import sys
#import resource
#resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))

sys.setrecursionlimit(2 ** 20)

class Node:
    def __init__(self, value):
        self._value = value
        self._in_arrows = set()
        self._out_arrows = set()
        self._finish_time = None
        self._explored = False

    def __str__(self):
        s = "Node: {}. Visited: {}. Time:{}. Out: {}. In: {}:\n".format(self._value, self._explored, self._finish_time, self._out_arrows, self._in_arrows)
        return s

    def add_in_arrow(self, node):
        self._in_arrows.add(node)

    def add_out_arrow(self, node):
        self._out_arrows.add(node)

    def set_finish_time(self, time):
        self._finish_time = time

    def is_explores(self):
        return self._explored

    #def re_arrange(self):
    #    self._value = self._finish_time

#n1 = Node(1)
#print n1
#Test cases
#n1.add_in_arrow(4)
#print n1._in_arrows

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

graph1 = build_test_graph(test1)
graph2 = build_test_graph(test2)
graph3 = build_test_graph(test3)
graph4 = build_test_graph(test4)
graph5 = build_test_graph(test5)


def build_graph_from_file():
    fh = open('graph_data.txt')
    data = fh.read()
    print "read data from file"
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
    print "Graph constructed from data"
    #for num in graph:
    #    print graph[num]
    return graph
#build_graph_from_url()

    pass

build_graph_from_file()

def build_graph_from_url():
    """
    Load data and build undirected graph with desired data_structure.
    {1: (set([1,4,5]), UNVISITED), 2: ...}

    NB: The graph in question has no parallel edges, so I use sets to store tails for edges.
    The graph does have self-loops

    """
    import urllib2
    url = "https://d3c33hcgiwev3.cloudfront.net/_410e934e6553ac56409b2cb7096a44aa_SCC.txt?Expires=1514937600&Signature=MSp-2k-rHk0-Gr6yP3mhkQqnYH2GqSpfyr5R6NKXTittXVb80-4kqHA8hbwtuDbUu5LwUe6QE1mocYsD89BY6pbLh71E5i4FUHxEdpHTY27FmkDkAPIBWSSncEWYOAuG3VrffbYygoqga0idXQCkXPEMR26xkHH8qKEdfs5ybeE_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A"
    data_file = urllib2.urlopen(url)
    #data = urllib2.urlopen(url)
    print "Opened file"
    data = data_file.read()
    print "Read data"
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
    print "Graph constructed from data"
    #for num in graph:
    #    print graph[num]
    return graph
#build_graph_from_url()


    #print graph
    #print ""
    #print rev_graph
    # #print "A connected graph with {},
    # nodes has been build from loaded data".format(len(graph))
    # #print graph
    # print len(graph)
#build_graph()


#leaders = {leader1: set... , leader2:set..., ....}


def dfs(graph, node, reverse):
    """
    Depth first search, modified to be used in detection of strongly connected components of graph.
    Graph is a dictionary of nodes
    """
    global FINISH_TIME
    node._explored = True

    if not reverse:
        if LEADER not in LEADERS:
            LEADERS[LEADER] = set([node._value])
        else:
            LEADERS[LEADER].add(node._value)

    if not reverse:
        for tail in node._out_arrows:
            if not graph[tail]._explored:
                dfs(graph, graph[tail], reverse)
    else:
        for tail in node._in_arrows:
            if not graph[tail]._explored:
                dfs(graph, graph[tail], reverse)
    if reverse:
        FINISH_TIME += 1
        #node.set_finish_time(FINISH_TIME)
        FINISH_TIMES[FINISH_TIME] = node

FINISH_TIMES = {}

def dfs_loop(graph, reverse):
    global LEADERS, LEADER, FINISH_TIME, FINISH_TIMES
    LEADERS = {}
    LEADER = None
    FINISH_TIME = 0

    if reverse:
        for node in graph.values():
            if not node._explored:
                LEADER = node._value
                dfs(graph, node, True)
    else:
        order = FINISH_TIMES.items()
        order.sort(reverse = True)
        for rank, node in order:
            #print rank, node._value
            if not node._explored:
            #    print node._value
                LEADER = node._value
                dfs(graph, node, False)

# dfs_loop(graph1, True)
# for node in graph1.values():
#     node._explored = False
# dfs_loop(graph1, False)
#
# print LEADERS
#
#
# dfs_loop(graph2, True)
# for node in graph2.values():
#     node._explored = False
# dfs_loop(graph2, False)
#
# print LEADERS
#
# dfs_loop(graph3, True)
# for node in graph3.values():
#     node._explored = False
# dfs_loop(graph3, False)
#
# print LEADERS
#
#
#
#
#
#
# def len_scc(dict):
#     lst = []
#     for key, val in dict.items():
#         lst.append(len(val))
#         lst.sort(reverse = True)
#     if len(lst) < 20:
#         print lst
#     else:
#         print lst[:20]
#
#
# print "test4"
# dfs_loop(graph4, True)
# for node in graph4.values():
#     node._explored = False
# dfs_loop(graph4, False)
# len_scc(LEADERS)
#
# print "test5"
# dfs_loop(graph5, True)
# for node in graph5.values():
#     node._explored = False
# dfs_loop(graph5, False)
# len_scc(LEADERS)
#
#
# real_graph = build_graph_from_url()
# print "first loop starts"
# dfs_loop(real_graph, True)
# print "first loop finished"
# for node in real_graph.values():
#     node._explored = False
# print "second loop starts"
# dfs_loop(real_graph, False)
# print len_scc(LEADERS)


#dfs(graph1, graph1[1])
#dfs(graph1, graph1[5])

#for key, val in FINISH_TIMES.items():
#    print key, val


#print LEADERS


def build_graph_from_url():
    """
    Load data and build undirected graph with desired data_structure.
    {1: (set([1,4,5]), UNVISITED), 2: ...}

    NB: The graph in question has no parallel edges, so I use sets to store tails for edges.
    The graph does have self-loops

    """
    import urllib2
    url = "https://d3c33hcgiwev3.cloudfront.net/_410e934e6553ac56409b2cb7096a44aa_SCC.txt?Expires=1514937600&Signature=MSp-2k-rHk0-Gr6yP3mhkQqnYH2GqSpfyr5R6NKXTittXVb80-4kqHA8hbwtuDbUu5LwUe6QE1mocYsD89BY6pbLh71E5i4FUHxEdpHTY27FmkDkAPIBWSSncEWYOAuG3VrffbYygoqga0idXQCkXPEMR26xkHH8qKEdfs5ybeE_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A"
    data_file = urllib2.urlopen(url)
    print "Opened file"
    data = data_file.read()
    print "Read data"
    data_lines = data.split('\n')
    graph = {}
    rev_graph = {}
    for line in data_lines:
        line = line.split()
        head = int(line[0])
        tail = int(line[1])
        if head not in graph:
            graph[head] = (set([tail]), UNVISITED)
        else:
            graph[head][0].add(tail)
        if tail not in rev_graph:
            rev_graph[tail] = (set([head]), UNVISITED)
        else:
            rev_graph[tail][0].add(head)
    print graph[1]
    print graph[100]
    print rev_graph[1]
    print rev_graph[100]
    #print graph
    #print ""
    #print rev_graph
    # #print "A connected graph with {},
    # nodes has been build from loaded data".format(len(graph))
    # #print graph
    # print len(graph)
#build_graph()
