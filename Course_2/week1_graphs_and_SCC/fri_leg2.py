"""
Kosaraju's algorithm for determination of strongly connected components of graph.
Uses Depth First Search twice
Note that the implementation of DFS has to iterative because of Python.
This is the FASTEST VERSION. 27 seconds in total.
"""

import random


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



def build_graph_from_file():
    """
    Load data and build undirected graph with desired data_structure.
    {1: (set([1,4,5]), UNVISITED), 2: ...}

    NB: The graph in question has no parallel edges, so I use sets to store tails for edges.
    The graph does have self-loops

    """

    fh = open('graph_data.txt')
    data = fh.read()
    print "Read data from file"
    data_lines = data.split('\n')

    graph = {}

    for line in data_lines:
        line = line.split()
        head = int(line[0])
        tail = int(line[1])
        if head not in graph:
            graph[head] = [[tail], False, [] , False]
        else:
            graph[head][0].append(tail)
        if tail not in graph:
            graph[tail] = [[], False, [head], False]
        else:
            graph[tail][2].append(head)

    print "Graph constructed from loaded data"
    return graph

#build_graph_from_file()
#print graph[1]
#print rev_graph[600000]

def dfs_reversed(graph, start_node):
    """
    Depth first search, modified to be used in detection of strongly connected components of graph.
    Graph is a dictionary of nodes
    """
    stack = [start_node]

    while stack != []:
        node = stack[-1]
        #set node explored
        graph[node][3] = True
        end_track = True

        for neighbor in graph[node][2]:
            #if not explored
            if not graph[neighbor][3]:
                stack.append(neighbor)
                end_track = False
                break
                #Note that only one neighbor gets appended to stack.

        if end_track:
            stack.pop()
            FINISH_ORDER.append(node)

def first_loop(graph):
    global FINISH_ORDER
    FINISH_ORDER = []

    for key, val in graph.items():
        if not val[3]:
            dfs_reversed(graph, key)

def dfs_un_reversed(graph, start_node):
    """
    Depth first search, modified to be used in detection of strongly connected components of graph.
    Graph is a dictionary of nodes
    """
    stack = [start_node]

    LEADERS[LEADER] = set()

    while stack != []:
        node = stack[-1]
        graph[node][1] = True
        end_track = True
        LEADERS[LEADER].add(node)

        for neighbor in graph[node][0]:
            if not graph[neighbor][1]:
                stack.append(neighbor)
                end_track = False
                break
                #Note that only one neighbor gets appended to stack.

        if end_track:
            stack.pop()

def second_loop(graph):
    global LEADERS, LEADER
    LEADERS = {}
    LEADER = None
    length = len(FINISH_ORDER)

    for indx in range(length - 1, -1, -1):
        node = FINISH_ORDER[indx]
        if not graph[node][1]:
            LEADER = node
            dfs_un_reversed(graph, node)

def scc(graph):
    print "Starting first loop"
    first_loop(graph)
    print "Done with first loop"
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
#print rev_real_graph[616916]
#print rev_real_graph[616917]

scc(real_graph)

#scc(graph9)
#scc(graph15)
