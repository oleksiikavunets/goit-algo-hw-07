import random

from binary_tree import BinaryTree

tree = BinaryTree()

items = list(range(1, 10))

random.shuffle(items)

[tree.insert(i) for i in items]

print(tree)

print(tree.min_node_val())
