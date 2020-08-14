"""
This version works. And finishes in about 62 secounds.
"""

from unionfind import*

NUM_CLUSTERS = 200000
u = unionfind(NUM_CLUSTERS + 1)
#ignore cluster [0]

def load_data():
    global NUM_CLUSTERS
    fh = open('clustering_big.txt')
    data = fh.read()
    data_lines = data.split('\n')
    num_nodes, num_bits = data_lines[0].split()
    print "Read cluster data with {} nodes.\nThere is a pre-computed positive distance between every pair of points.".format(num_nodes)
    print "All distances are between 0 and {} (24 is the number of bits).".format(num_bits)
    print "Total number of edges is around {} billion.".format(int(((int(num_nodes)-1)*(int(num_nodes)-2)/2)/float(10**9)))

    data_dict = {}
    for indx in range(len(data_lines) - 2):
        line = data_lines[indx + 1]
        line = line.replace(" ", "")
        if line not in data_dict:
            data_dict[line] = indx + 1
        else:
            u.unite(indx + 1, data_dict[line])
            NUM_CLUSTERS -= 1

    return data_dict

DATA_DICT = load_data()
print "NUM_CLUSTERS:", NUM_CLUSTERS

print "There now are {} distinct clusters in DATA_DICT".format(len(DATA_DICT))

def gen_mutations(code):
    """
    Makes list of all codes that differs from code in exactly 1 or 2 letters
    """
    mutations = set()

    for indx in range(len(code)):
        c = code[indx]
        if c == "0":
            c = "1"
        else:
            c = "0"
        mutations.add(code[:indx]+c+code[indx+1:])

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
            mutations.add(code[:indx1] + c1 + code[indx1+1:indx2] + c2 + code[indx2+1:])

    return mutations

for code, node in DATA_DICT.items():
    mutations = gen_mutations(code)
    for mutation in mutations:
        if mutation in DATA_DICT:
            node2 = DATA_DICT[mutation]
            if not u.issame(node, node2):
                u.unite(node, node2)
                NUM_CLUSTERS -= 1

print "Result: Number of clusters when no nodes with Hammel distance less than 3 are in distinct clusters:", NUM_CLUSTERS
#print len(u.groups())
