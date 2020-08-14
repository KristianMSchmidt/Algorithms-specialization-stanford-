"""
Hierarchical clustering using Kruskal's (greedy) algorithm and "union find" data structure

u = unionfind(3) # There are 3 items.
u.unite(0, 2) # Set 0 and 2 to same group.
u.issame(1, 2) # Ask "Are 1 and 2 same?"
u.groups() # Return groups.

"""
from unionfind import*


def make_list_from_data():
    fh = open('clustering_data.txt')
    data = fh.read()
    data_lines = data.split('\n')
    print "Read cluster data with {} nodes. There is a pre-computed positive distance between every pair of points.\n".format(data_lines[0])
    data_list = []
    print "There are {} edges in the provided graph.\n".format(len(data_lines)-2)
    for line in data_lines[1:-1]:
        node_1, node_2, distance = line.split()
        data_list.append((int(distance), int(node_1), int(node_2)))
    return data_list

DATA = make_list_from_data()

def test():
    distance_list = [(2,1,3), (5,2,3), (7, 1, 2), (10, 2, 4), (13, 1,4), (11, 3,4), (1,5,6), (1,6,7), (1,5,7), (9,6,1)]
    distance_list.sort()

    num_nodes = 7
    final_num_clusters = 7
    indx = 0
    u = unionfind(num_nodes + 1)

    while len(u.groups()) - 1 > final_num_clusters:
        distance, node_1, node_2 = distance_list[indx]
        if not u.issame(node_1, node_2):
            u.unite(node_1, node_2)
        indx += 1

    spacing = float('inf')
    #Spacing of a k-cluster is the minimum distance between to points that are not in the same
    #cluster. Given k and set of point, the spacing should be as big as possible.

    for indx2 in range(indx + 1, len(distance_list)):
        distance, node_1, node_2 = distance_list[indx]
        if not u.issame(node_1, node_2):
            if distance < spacing:
                spacing = distance
        indx += 1

    groups = u.groups()
    groups.pop(0)
    print groups, spacing

#test()




def solution(distance_list, num_nodes, final_num_clusters):
    """
    Makes clusters using union find package
    """
    distance_list.sort()

    indx = 0
    u = unionfind(num_nodes + 1)
    current_num_clusters = num_nodes

    while current_num_clusters > final_num_clusters:
        distance, node_1, node_2 = distance_list[indx]
        if not u.issame(node_1, node_2):
            u.unite(node_1, node_2)
            current_num_clusters -= 1
        indx += 1

    spacing = float('inf')
    #Spacing of a k-cluster is the minimum distance between to points that are not in the same
    #cluster. Given k and set of point, the spacing should be as big as possible.

    for indx2 in range(indx + 1, len(distance_list)):
        distance, node_1, node_2 = distance_list[indx]
        if not u.issame(node_1, node_2):
            if distance < spacing:
                spacing = distance
        indx += 1

    groups = u.groups()
    groups.pop(0)
    print "There are now {} clusters. The minimal spacing between clusters is {}.".format(len(groups), spacing)
solution(DATA, 500, 4)



def make_test_case():
    fh = open('test_data_problem_1.txt')
    data = fh.read()
    data_lines = data.split('\n')

    print "Read cluster data with {} nodes. There is a pre-computed positive distance between every pair of points.\n".format(data_lines[0])
    data_lines = data_lines[2:-5]
    data_lines = [line for line in data_lines if line != ""]
    data_list = []
    for line in data_lines:
        node_1, node_2, distance = line.split()
        data_list.append((int(distance), int(node_1), int(node_2)))
    return data_list
#TEST_DATA = make_test_case()
#solution(TEST_DATA, 12, 4)

#Should yield min_spacing of 99 with k=4.
#clusters are [1,2,3], [4,5,6], [7,8,9], [10,11,12]
