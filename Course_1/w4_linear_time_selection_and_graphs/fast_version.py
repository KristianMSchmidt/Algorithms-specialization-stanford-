"""
This version is faster, but the edges don't really get chosen the honestly random way.
Making it "honest" would take something like what I've commented out in line 17&18.
"""
import urllib2
import random

def remove_vertex(graph, super_vertex, dis_vertex):
    """
    helper function doing some of the dirty work
    """
    global nodes

    for ver in graph[dis_vertex]:
        graph[ver].append(super_vertex)
        graph[ver].remove(dis_vertex)
        if ver != super_vertex:
            nodes.append(super_vertex)
    graph.pop(dis_vertex)
    return graph


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

    contractions[vertex1] = contractions.get(vertex1, set([vertex1]))
    union_with_this = contractions.get(vertex2, set([vertex2]))
    contractions[vertex1].update(union_with_this)

    if vertex2 in contractions:
       contractions.pop(vertex2)

    return graph, contractions


def contract_graph(graph, num_vertices, nodes):
    """
    Takes a undirected graph (parallel edges allowed) represented as an adjecency list, performs randomized
    edge contractions until only 2 vertices left. Returns resulting graph.
    Loops not allowed
    """
    contractions = {}

    while num_vertices > 2:
        vertex1 = random.choice(nodes)
        vertex2 = random.choice(graph[vertex1])
        nodes = [node for node in nodes if node != vertex2]
        #print vertex1, vertex2
        graph, contractions = contract_edge(graph, contractions, vertex1, vertex2)
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
    global nodes

    url = "https://d3c33hcgiwev3.cloudfront.net/_f370cd8b4d3482c940e4a57f489a200b_kargerMinCut.txt?Expires=1514764800&Signature=e--6BnvkWa1PahltjjsNILmmQorGeWZynX5zTHoiJ5uB~BNOCj2Fuv7P7Fge3RBe2k6bjnDUG13dD9fgwJP3sLhFim3KSOa~nbSXU3X8L6f27122AJqekB4E~680mlAvL0BR3up~pgThyb1yOJTZEMFeenLcNFYaAXYROvnubss_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A"
    data_file = urllib2.urlopen(url)
    data = data_file.read()
    data_lines = data.split('\n')
    data_lines = data_lines[:-1]

    graph = {}
    nodes = []

    for line in data_lines:
        line = line.split()
        node = int(line[0])
        graph[node] = []
        for number in line[1:]:
            graph[node].append(int(number))
            nodes.append(node)
    #random.shuffle(nodes)
    print "A connected graph with {} nodes has been build from loaded data".format(len(graph))
    return graph, nodes

def compute_answer():
    min_num_cuts = 1000
    min_graph = None
    min_clusterings = None
    graph, nodes = build_graph()
    for num in range(20):
        new_graph = {}
        for node in graph:
            new_graph[node] = list(graph[node])
        result_graph, result_contractions = contract_graph(new_graph, 200, nodes)
        num_cuts = len(random.choice(result_graph.values()))
        if num_cuts < min_num_cuts:
            min_graph = result_graph
            min_num_cuts = num_cuts
            min_clusterings = result_contractions

    print "\nThe big graph of the assignment has minimum cut value: ", min_num_cuts
    #print "\nResulting graph after Krager's algorithm: ", min_graph

    cluster1, cluster2 = list(min_clusterings.values()[0]), list(min_clusterings.values()[1])
    cuts = []
    for node in cluster1:
        for head in graph[node]:
            if head in cluster2:
                cuts.append((node, head))
    print "\nCuts in minimal cuts (aka. 'critial connections' in network):\n", cuts

    print "\nAfter doing the minimal cut, there will be to connected graphs left. One of them will have these vertices: \n{}\n\nThe other will have these:\n{}".format(cluster1, cluster2)

compute_answer()
