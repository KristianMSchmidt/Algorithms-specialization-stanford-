"""
This version uses my own home build "Union Find"-data structure.
This version ALSO works. And finishes in about 52 secounds. This is as fast as the version
using build-in-union find. Nice!
This version processes data while loading it.
"""

class Unionfind:
    def __init__(self, some_list):
        self._leader_dict = {}
        self._leader_classes = {}
        self._leader_lengths = {}

        for element in some_list:
            self._leader_dict[element] = element
            self._leader_classes[element] = set([element])
            self._leader_lengths[element] = 1

    def unite(self, repr1, repr2):
        leader1 = self._leader_dict[repr1]
        leader2 = self._leader_dict[repr2]

        if self._leader_lengths[leader1] >= self._leader_lengths[leader2]:
            self._leader_classes[leader1].update(self._leader_classes[leader2])
            for elem in self._leader_classes[leader2]:
                self._leader_dict[elem] = leader1
            #self._leader_classes[leader2] = set()
            self._leader_lengths[leader1] += self._leader_lengths[leader2]
            #self._leader_lengths[leader2] = 0
        else:
            self._leader_classes[leader2].update(self._leader_classes[leader1])
            for elem in self._leader_classes[leader1]:
                self._leader_dict[elem] = leader2
            #self._leader_classes[leader1] = set()
            self._leader_lengths[leader2] += self._leader_lengths[leader1]
            #self._leader_lengths[leader1] = 0


    def get_leader(self, element):
        return self._leader_dict[element]

    def issame(self, repr1, repr2):
        if self._leader_dict[repr1] == self._leader_dict[repr2]:
            return True
        else:
            return False

# u = Unionfind(range(1,10))
# u.unite(1,9)
# print u.issame(1,9)
# print u._leader_dict
# print u._leader_classes
# print u._leader_lengths
#
# u.unite(2,9)
#
# print u.issame(2,9)
# print u._leader_dict
# print u._leader_classes
# print u._leader_lengths

def gen_mutations(code):
    """
    Makes list of all codes that differs from code in exactly 1 or 2 letters
    """
    mutations = []
    len_code = 24
    for indx in range(len_code):
        c = code[indx]
        if c == "0":
            c = "1"
        else:
            c = "0"
        mutations.append(code[:indx] + c + code[indx + 1:])

    for indx1 in range(len_code - 1):
        first_part = code[:indx1]
        for indx2 in range(indx1 + 1, len_code):
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
            mutations.append(first_part + c1 + code[indx1 + 1 : indx2] + c2 + code[indx2 + 1:])

    return mutations


def load_data():
    global NUM_CLUSTERS

    fh = open('clustering_big.txt')
    data = fh.read()
    data_lines = data.split('\n')
    num_nodes, num_bits = data_lines[0].split()
    print "Read cluster data with {} nodes.\nThere is a pre-computed positive distance between every pair of nodes.".format(num_nodes)
    print "All distances are between 0 and {} (24 is the number of bits).".format(num_bits)
    print "Total number of edges is around {} billion.".format(int(((int(num_nodes)-1)*(int(num_nodes)-2)/2)/float(10**9)))

    codes = {}
    for indx in range(len(data_lines) - 2):
        node = indx + 1
        code = data_lines[node].replace(" ", "")
        if code not in codes:
            codes[code] = node
        else:
            u.unite(node, codes[code])
            NUM_CLUSTERS -= 1
        mutations = gen_mutations(code)
        for mut in mutations:
            if mut in codes:
                node2 = codes[mut]
                if not u.issame(node, node2):
                    u.unite(node, node2)
                    NUM_CLUSTERS -= 1

NUM_CLUSTERS = 200000
u = Unionfind(range(1, NUM_CLUSTERS + 1))
load_data()


print NUM_CLUSTERS
