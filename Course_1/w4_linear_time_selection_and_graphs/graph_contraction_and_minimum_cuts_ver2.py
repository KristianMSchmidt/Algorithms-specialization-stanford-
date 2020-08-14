"""
KRAGER'S ALGORITHM

Version 2 is better!

The file contains the adjacency list representation of a simple undirected graph. There are 200 vertices labeled 1
to 200. The first column in the file represents the vertex label, and the particular row (other entries except the
first column) tells all the vertices that the vertex is adjacent to. So for example, the 6th row looks like : "6
155	56	52	120	......". This just means that the vertex with label 6 is adjacent to (i.e., shares an edge with)
 the vertices with labels 155,56,52,120,......,etc

Your task is to code up and run the randomized contraction algorithm for the min cut problem and use it on
the above graph to compute the min cut. (HINT: Note that you'll have to figure out an implementation of
 edge contractions. Initially, you might want to do this naively, creating a new graph from the old every time there's
an edge contraction. But you should also think about more efficient implementations.)
(WARNING: As per the video lectures, please make sure to run the algorithm many times with different random seeds,
 and remember the smallest cut that you ever find.) Write your numeric answer in the space provided. So e.g., if your answer is 5, just type 5 in the space provided.
"""
import random
import urllib2

def undirected(graph):
    """
    Un-used assertion
    """
    for vertex1 in graph.keys():
        for vertex2 in graph[vertex1]:
            if vertex1 not in graph[vertex2]:
                return False
    return True


def remove_vertex(graph, super_vertex, dis_vertex):
    """
    helper function doing some of the dirty work
    """
    global all_edges

    for ver in graph[dis_vertex]:
        all_edges.remove((ver, dis_vertex))
        all_edges.remove((dis_vertex, vertex))

        all_edges.add(tuple(sorted((ver, super_vertex))))
        graph[ver].append(super_vertex)
        graph[ver].remove(dis_vertex)
    graph.pop(dis_vertex)
    return graph

#graph = {1: [2,3], 2:[1,3,4], 3: [1,2,4], 4:[3,2]}


def contract_edge(graph, contractions, vertex1, vertex2):
    """
    Takes a undirected graph (parallel edges allowed) represented as an adjecency list, a dictionary containing infor
    about current contractions. Performs one randomized edge contraction.
    Returns updated grapgh and updates contraction info.
    """
    #assert undirected(graph)
    graph[vertex1] += graph[vertex2]
    graph = remove_vertex(graph, vertex1, vertex2)

    graph[vertex1] = [ver for ver in graph[vertex1] if ver != vertex1]
    global all_edges
    all_edges
    contractions[vertex1] = contractions.get(vertex1, set([vertex1]))
    union_with_this = contractions.get(vertex2, set([vertex2]))
    contractions[vertex1].update(union_with_this)

    if vertex2 in contractions:
       contractions.pop(vertex2)

    return graph, contractions

def test():
    graph = {1: [2,3], 2:[1,3,4], 3: [1,2,4], 4:[3,2]}

    contractions = {}
    print contract_edge(graph, contractions, 1, 3)
    print contract_edge(graph, contractions, 1, 2)

#test()

def gen_all_edges(graph):
    edges = []
    for key, val in graph.items():
        for ver in val:
            edges.append((key, ver))
    return edges

#graph = {1: [2,3], 2:[1,3,4], 3: [1,2,4], 4:[3,2]}
#ed= gen_all_edges(graph)
#print ed.pop()
#print ed
def contract_graph(graph, num_vertices):
    """
    Takes a undirected graph (parallel edges allowed) represented as an adjecency list, performs randomized
    edge contractions until only 2 vertices left. Returns resulting graph.
    Loops not allowed
    """
    contractions = {}
    global all_edges
    all_edges = gen_all_edges(graph)

    while num_vertices > 2:
        chosen = False
        while not chosen:
            vertex1, vertex2 = all_edges.pop()
            print vertex1, vertex2
            if (vertex1 in graph and vertex2 in graph) and vertex1 != vertex2:
                #print "good choice"
                chosen = True
            #else:
                #print "not in graph"
        graph, contractions = contract_edge(graph, contractions, vertex1, vertex2)
        #print num_vertices
        num_vertices -= 1

    for key in graph.keys():
       if not key in contractions:
           contractions[key] = set([key])

    return graph, contractions


def build_graph():
    """
    Load data and build graph with desired data_structure
    """
    import urllib2
    url = "https://d3c33hcgiwev3.cloudfront.net/_f370cd8b4d3482c940e4a57f489a200b_kargerMinCut.txt?Expires=1514764800&Signature=e--6BnvkWa1PahltjjsNILmmQorGeWZynX5zTHoiJ5uB~BNOCj2Fuv7P7Fge3RBe2k6bjnDUG13dD9fgwJP3sLhFim3KSOa~nbSXU3X8L6f27122AJqekB4E~680mlAvL0BR3up~pgThyb1yOJTZEMFeenLcNFYaAXYROvnubss_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A"
    data_file = urllib2.urlopen(url)
    data = data_file.read()
    data_lines = data.split('\n')
    data_lines = data_lines[:-1]

    graph = {}
    for line in data_lines:
        line = line.split()
        graph[int(line[0])] = [int(number) for number in line[1:]]

    print "A graph with {} nodes has been build from loaded data".format(len(graph))
    return graph

#graph = build_graph()



def test_cases():
    """
    if num_trials = n^2*log(n), then prob for getting wrong result is 1/n
    n=num_vertices
    """

    min_num_cuts = 1000
    for num in range(100):
        #graph1 = {1: [2,3,4,7], 2: [1,3,4], 3:[1,2,4], 4:[1,2,3,5], 5:[4,6,7,8], 6:[5,7,8], 7:[1,5,6,8], 8:[5,6,7]}
        #xpected = 2
        graph2 = {1: [2,3,4], 2:[1,3,4], 3: [1,2,4], 4:[1,2,3,5], 5:[4,6,7,8], 6:[5,7,8], 7:[5,6,8], 8:[5,6,7]}
        #expected = 1
        num_cuts = len((contract_graph(graph2, 8)[0]).popitem()[1])
        if num_cuts < min_num_cuts:
            min_num_cuts = num_cuts
    print min_num_cuts

#test_cases()

def make_graph():
    fh = open('test_case.txt', 'r')
    data = fh.read()
    #print data

    data_lines = data.split('\n')
    data_lines = data_lines[:-3]

    graph = {}
    for line in data_lines:
        line = line.split()
        graph[int(line[0])] = [int(number) for number in line[1:]]
    return graph

def compute_answer():
    min_num_cuts = 1000
    min_graph = None
    graph = build_graph()
    for num in range(5):
        new_graph = {}
        for node in graph:
            new_graph[node] = list(graph[node])
        result_graph, result_contractions = contract_graph(new_graph, 200)
        num_cuts = len(result_graph.popitem()[1])
        if num_cuts < min_num_cuts:
            min_num_cuts = num_cuts
            min_graph = result_graph
    print "The big graph of the assignment has minimum cut value: ", min_num_cuts
    print result_graph
compute_answer()



def test_case():
    #expect 3
    min_num_cuts = 1000
    for num in range(1000):
        num_cuts = len((contract_graph(make_graph(), 40)[0]).popitem()[1])
        if num_cuts < min_num_cuts:
            min_num_cuts = num_cuts
    print min_num_cuts

#test_case()
