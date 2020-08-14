"""
Prim's algorithm
IMPLEMENTATION NOTES: This graph is small enough that the straightforward O(mn) time implementation of Prim's
algorithm should work fine. OPTIONAL: For those of you seeking an additional challenge, try implementing a
 heap-based version. The simpler approach, which should already give you a healthy speed-up, is to maintain
  relevant edges in a heap (with keys = edge costs). The superior approach stores the unprocessed vertices
   in the heap, as described in lecture. Note this requires a heap that supports deletions, and you'll probably
   need to maintain some kind of mapping between vertices and their positions in the heap.
"""


def build_graph():
    """
    This file describes an undirected graph with integer edge costs. It has the format
    For example, the third line of the file is "2 3 -8874", indicating that there is an edge connecting
    vertex #2 and vertex #3 that has cost -8874.

    Constructed graph has form:
    {Vertex: {tail: edge_weight, tail: edge_weight}, ....}
    """

    fh = open('edges.txt')
    data = fh.read()
    print "Read data from file"
    data_lines = data.split('\n')
    print "Read data from file. Graph has 500 nodes and 2184 edges"

    data_lines =  data_lines[1:-1]

    graph = {}

    for line in data_lines:
        line = line.split()
        head = int(line[0])
        tail = int(line[1])
        edge_cost = int(line[2])
        if head not in graph:
            graph[head] = {tail: edge_cost}
        else:
            graph[head][tail] = edge_cost
        if tail not in graph:
            graph[tail] = {head: edge_cost}
        else:
            graph[tail][head] = edge_cost
    return graph

real_graph = build_graph()

def naive_implementation():
    """
    This graph is small enough that the straightforward O(mn) time
    implementation of Prim's algorithm should work fine.
    """
    graph = real_graph
    #graph = {1: {2:1, 3:4, 4:3}, 2: {4:2, 1:1}, 3:{1:4, 4:5}, 4:{3:5, 1:3, 2:2}}
    start_node = graph.keys()[0]
    tree_cost = 0
    nodes_in_tree = set([start_node])
    tree_edges = set([])

    num_iterations = len(graph)
    indx = 1

    while indx < num_iterations:
        min_score = float('inf')
        selected_tail = None
        for head in nodes_in_tree:
            for tail in graph[head]:
                if tail not in nodes_in_tree:
                    edge_cost = graph[head][tail]
                    if edge_cost < min_score:
                        min_score = edge_cost
                        selected_tail = tail
        tree_edges.add((head, selected_tail, min_score))
        nodes_in_tree.add(selected_tail)
        tree_cost += min_score
        indx += 1
    print "Length of minimal spanning tree:", tree_cost
    return tree_cost

#print naive_implementation() == -3612829

import heapq

def fast_prim(graph):
    """
    Uses heap data structure since we nead to extract minimum several times.
    Should have running time O(n log(m))
    """
    start_node = graph.keys()[0]
    tree_cost = 0
    tree_nodes = set([start_node]) # X

    #Initialize heap - use heapify as this is faster than adding one element at a time
    heap = []
    for vertex in graph:
        if vertex != start_node:
            min_cost = float('inf')
            if vertex in graph[start_node]:
                for node in graph[start_node]:
                    if node == vertex:
                        edge_cost = graph[start_node][node]
                        if edge_cost < min_cost:
                            min_cost = edge_cost
            heap.append((min_cost, vertex))
    heapq.heapify(heap)

    num_iterations = len(graph)
    indx = 1

    while indx < num_iterations:
        edge_cost, next_node = heapq.heappop(heap)
        while next_node in tree_nodes:
            edge_cost, next_node = heapq.heappop(heap)
        tree_nodes.add(next_node)
        tree_cost += edge_cost
        for head in graph[next_node]:
            if head not in tree_nodes: ##i.e. head is in the heap
                edge_cost = graph[next_node][head]
                heapq.heappush(heap, (edge_cost, head))
        indx +=1

    return tree_cost

graph1 = {1: {2:1, 3:4, 4:3}, 2: {4:2, 1:1}, 3:{1:4, 4:5}, 4:{3:5, 1:3, 2:2}}

#print fast_prim(graph1) == 7
#print fast_prim(real_graph) == -3612829


def fast_prim2(graph):
    """
    Expanded version of fastprim, that also returns resulting tree edges and their cost
    Uses heap data structure since we nead to extract minimum several times.
    Running time
    """
    start_node = graph.keys()[0]
    tree_cost = 0
    tree_nodes = set([start_node]) # X
    tree_edges = set()

    #Initialize heap - use heapify as this i faster than adding one element at a time
    heap = []
    for vertex in graph:
        if vertex != start_node:
            min_cost = float('inf')
            if vertex in graph[start_node]:
                for node in graph[start_node]:
                    if node == vertex:
                        edge_cost = graph[start_node][node]
                        if edge_cost < min_cost:
                            min_cost = edge_cost
            heap.append((min_cost, (start_node, vertex)))
    heapq.heapify(heap)
    num_iterations = len(graph)
    indx = 1

    while indx < num_iterations:
        edge_cost, edge = heapq.heappop(heap)
        next_node = edge[1]
        while next_node in tree_nodes:
            edge_cost, edge = heapq.heappop(heap)
            next_node = edge[1]
        tree_nodes.add(next_node)
        tree_cost += edge_cost
        tree_edges.add((edge, edge_cost))
        for head in graph[next_node]:
            if head not in tree_nodes: ##i.e. head is in the heap
                edge_cost = graph[next_node][head]
                heapq.heappush(heap, (edge_cost, (next_node, head)))
        indx +=1

    return tree_cost, tree_edges

#print fast_prim2(graph1)[0] == 7
#print fast_prim2(graph1)[1]
print fast_prim2(real_graph)[0] == -3612829
