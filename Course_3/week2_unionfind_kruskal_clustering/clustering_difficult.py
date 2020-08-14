"""
This CODE is a mess - se version 2 or version 3 for working solutions
Hierarchical clustering using Kruskal's (greedy) algorithm and "union find" data structure

This is problem 2 - the difficult one.

u = unionfind(3) # There are 3 items.
u.unite(0, 2) # Set 0 and 2 to same group.
u.issame(1, 2) # Ask "Are 1 and 2 same?"
u.groups() # Return groups.

"""
from unionfind import*

NUM_CLUSTERS = 200000

def make_list_from_data():
    global NUM_CLUSTERS
    fh = open('clustering_big.txt')
    data = fh.read()
    data_lines = data.split('\n')
    num_nodes, num_bits = data_lines[0].split()
    print "Read cluster data with {} nodes.\nThere is a pre-computed positive distance between every pair of points.".format(num_nodes)
    print "All distances are between 0 and {} (24 is the number of bits).".format(num_bits)
    print "Total number of edges is around {} billion.".format(int(((int(num_nodes)-1)*(int(num_nodes)-2)/2)/float(10**9)))
    data_list = []
    node = 1
    for line in data_lines[1:-1]:
        data_list.append((node, line.replace(" ", "")))
        node += 1

    data_dict = {}
    for indx in range(len(data_lines) - 2):
        line = data_lines[indx + 1]
        line = line.replace(" ", "")
        if line not in data_dict:
            data_dict[line] = indx + 1
        else:
            NUM_CLUSTERS -= 1
    return data_list, data_dict

def gen_mutations(code):
    lst = [code]

    for indx in range(len(code)):
        c = code[indx]
        if c == "0":
            c = "1"
        else:
            c = "0"
        lst.append(code[:indx]+c+code[indx+1:])

    for indx1 in range(len(code)-1):
        for indx2 in range(indx1 + 1, len(code)):
            c1 = code[indx1]
            c2 = code[indx2]
            if c1 == "0":
                c1 = "1"
            else:
                c1 = "0"
            if c2 == "0":
                c2 = "1"
            else:
                c2 = "0"
            lst.append(code[:indx1] + c1 + code[indx1+1:indx2] + c2 + code[indx2+1:])

    return lst


DATA, data_dict = make_list_from_data()
# print len(data_dict)
# code1, node1 = data_dict.items()[0]
# print code1, node1
# lst = []
# mu = gen_mutations(code1)
# print code1 in mu
# for x in mu:
#     if x in data_dict:
#         lst.append(data_dict[x])
# print lst

count = 0
dict = {}

for code, node in data_dict.items():
    mu = gen_mutations(code)
    node = node[0]
    dict[node] = []
    for m in mu:
        if m in data_dict:
            dict[node].append(data_dict[m])
#print dict
    # for code in data_dict:
#     if len(data_dict[code]) > 2:
#         print code, data_dict[code]

def hamming_dist(code1, code2):
    """
    Calculates Hamming Distance between two codes (nodes)
    """
    dist = 0
    for pos in range(len(code1)):
        if code1[pos] != code2[pos]:
            dist += 1
    return dist
#print hamming_dist(DATA[0][1], DATA[1][1])

def is_hamming_less_3(code1, code2):
    """
    Answers whether Hamming Distance between two codes is <3 or not (nodes)
    """
    dist = 0
    for pos in range(len(code1)):
        if code1[pos] != code2[pos]:
            dist += 1
            if dist > 2:
                return False
    return True


def thin_out_data():
    DATA2 = []
    node1 = DATA[0]
    for node2 in DATA:
        if is_hamming_less_3(node1[1], node2[1]) and node1[0] != node2[0]:
            DATA2.append(node2[0])
            print node1[1]
            print node2[1]
            print hamming_dist(node1[1], node2[1])
            print ""
    print DATA2
#thin_out_data()
#print is_hamming_less_3("011122","111111")

#print is_hamming_less_3(DATA[0][1], DATA[1][1])




def solution(graph, num_nodes, final_num_clusters):
    """
    Makes clusters using union find package
    """
    u = unionfind(num_nodes + 1)
    current_num_clusters = num_nodes

    indx = 0
    for node1 in graph:
        if node1[0] % 100 ==0:
            print node1[0]
        for node2 in graph[indx:]:
            node_num_1 = node1[0]
            node_num_2 = node2[0]
            if node_num_1 != node_num_2:
                if is_hamming_less_3(node1[1], node2[1]):
                    if not u.issame(node_num_1, node_num_2):
                        u.unite(node_num_1, node_num_2)
                        current_num_clusters -= 1
        indx += 1
    print "Final number of clusters:", current_num_clusters
    # while current_num_clusters > final_num_clusters:
    #     distance, node_1, node_2 = distance_list[indx]
    #     if not u.issame(node_1, node_2):
    #         u.unite(node_1, node_2)
    #         current_num_clusters -= 1
    #     indx += 1
    #
    # spacing = float('inf')
    # #Spacing of a k-cluster is the minimum distance between to points that are not in the same
    # #cluster. Given k and set of point, the spacing should be as big as possible.
    #
    # for indx2 in range(indx + 1, len(distance_list)):
    #     distance, node_1, node_2 = distance_list[indx]
    #     if not u.issame(node_1, node_2):
    #         if distance < spacing:
    #             spacing = distance
    #     indx += 1
    #
    # groups = u.groups()
    # groups.pop(0)
    # print "There are now {} clusters. The minimal spacing between clusters is {}.".format(len(groups), spacing)
    #
#solution(DATA, 200000, 199999)

# bit = DATA[0][1]
# print bit
#
# indx = 1
# for node1 in DATA:
#     print node1[0]
#     for node2 in DATA[indx:]:
#         hamming_dist(node1[1], node2[1])
#     indx += 1
#
# # for node1 in DATA:
#     for node2 in DATA:
#         if node1[0] != node2[0]:
#             if hamming_dist(node1[1], node2[1]) == 0:
#                 print node1, node2
