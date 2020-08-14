"""
My own implementation of union find data structure.
I have not tested it that much - but it seems to work fast and smoothly.
Can use pre-build "unionfind" instead
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
            self._leader_classes[leader2] = set()
            self._leader_lengths[leader1] += self._leader_lengths[leader2]
            self._leader_lengths[leader2] = 0
        else:
            self._leader_classes[leader2].update(self._leader_classes[leader1])
            for elem in self._leader_classes[leader1]:
                self._leader_dict[elem] = leader2
            self._leader_classes[leader1] = set()
            self._leader_lengths[leader2] += self._leader_lengths[leader1]
            self._leader_lengths[leader1] = 0


    def get_leader(self, element):
        return self._leader_dict[element]

    def issame(self, repr1, repr2):
        if self._leader_dict[repr1] == self._leader_dict[repr2]:
            return True
        else:
            return False

u = Unionfind(range(1,10))
u.unite(1,9)
print u.issame(1,9)
print u._leader_dict
print u._leader_classes
print u._leader_lengths

u.unite(2,9)

print u.issame(2,9)
print u._leader_dict
print u._leader_classes
print u._leader_lengths
