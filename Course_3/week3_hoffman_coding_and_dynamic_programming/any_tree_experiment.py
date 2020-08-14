"""
anytree modulet ser godt ud. Vildt mange muligheder i det.
Men der er utallige maader at lave traer paa. Se her for diskussion

https://stackoverflow.com/questions/2358045/how-can-i-implement-a-tree-in-python-are-there-any-built-in-data-structures-in/29531977

"""

from anytree import Node, RenderTree



udo = Node("Udo")
marc = Node("Marc", parent=udo)
lian = Node("Lian", parent=marc)
dan = Node("Dan", parent=udo)
jet = Node("Jet", parent=dan)
jan = Node("Jan", parent=dan)
joe = Node("Joe", parent=dan)

print udo
print dan
print joe

print ""

for pre, fill, node in RenderTree(udo):
    print("%s%s" % (pre, node.name))

print ""



#from anytree.exporter import DotExporter
#>>> # graphviz needs to be installed for the next line!
#>>> DotExporter(udo).to_picture("udo.png")


mary = Node("Mary")
urs = Node("Urs", parent=mary)
chris = Node("Chris", parent=mary)
marta = Node("Marta", parent=mary)

for pre, fill, node in RenderTree(mary):
    print("%s%s" % (pre, node.name))

print ""

#append
udo.parent = mary


for pre, fill, node in RenderTree(mary):
    print("%s%s" % (pre, node.name))
