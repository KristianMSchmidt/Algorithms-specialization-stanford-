"""
In this programming problem you'll code up the dynamic
 programming algorithm for computing a maximum-weight independent set of a path graph.

Download the text file below.

mwis.txt
This file describes the weights of the vertices in a path graph (with the weights listed in the order in which
vertices appear in the path). It has the following format:

[number_of_vertices]

[weight of first vertex]

[weight of second vertex]

...

For example, the third line of the file is "6395702," indicating that the weight of the second vertex of the graph
 is 6395702.

Your task in this problem is to run the dynamic programming algorithm (and the reconstruction procedure) from
lecture on this data set. The question is: of the vertices 1, 2, 3, 4, 17, 117, 517, and 997, which ones belong
 to the maximum-weight independent set? (By "vertex 1" we mean the first vertex of the graph---there is no vertex 0.)
 In the box below, enter a 8-bit string, where the ith bit should be 1 if the ith of these 8 vertices is in the
 maximum-weight independent set, and 0 otherwise. For example, if you think that the vertices 1, 4, 17, and 517
  are in the maximum-weight independent set and the other four vertices are not, then you should enter the
  string 10011010 in the box below.
"""



def load_data():
    """
    Read data from file.
    """
    fh = open('data_for_pa3.txt')
    data = fh.read()
    data_lines = data.split('\n')
    vertices = {}
    index = 1
    for line in data_lines[1:-1]:
        vertices[index] = int(line)
        index += 1
    return vertices

#vertices = load_data()
#vertices = {1: 4, 2:5, 3:4, 4:5, 5:0, 6:20, 7:21, 8:40, 9:41}
#vertices  = {1: 4}

def max_wis(vertices):
    """
    Find the weight of the max weight independent set.
    A[i] = max weight of of vertices 0, 1, ..., i
    """
    A = {}
    A[-1] = 0
    A[0] = 0
    A[1] = vertices[1]

    for indx in range(2, len(vertices) + 1):
        A[indx] = max(A[indx - 1], A[indx -2] + vertices[indx])

    print "Maximum weight of independent set of graph is:", A[len(vertices)]
    return A


def reconstruct(vertices, A):
    """
    Reconstructs the vertices in the max weight independent set from the array A.
    """
    vertex_set = set()
    indx = len(vertices)

    while indx >= 1:
        if A[indx - 2] + vertices[indx] > A[indx - 1]:
            vertex_set.add(indx)
            indx -= 2
        else:
            indx -= 1

    #control check
    summa = 0
    for x in vertex_set:
        summa += vertices[x]
    print "Control check:", summa
    return vertex_set

def solution():
    vertices = load_data()
    max_w = max_wis(vertices)
    vert_set = reconstruct(vertices, max_w)
    integers = [1, 2, 3, 4, 17, 117, 517, 997]
    solution = ""
    for integer in integers:
        if integer in vert_set:
            solution = solution + "1"
        else:
            solution = solution + "0"
    print "Solution code to assignment:", solution

solution()
