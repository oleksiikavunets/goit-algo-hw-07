class BinaryTree:

    def __init__(self):
        self.root = None

    class Node:
        def __init__(self, key):
            self.left = None
            self.right = None
            self.val = key

        def __str__(self, level=0, prefix='   '):
            ret = f'{"\t" * level}{prefix}[{self.val}]\n'
            # ret = "\t" * level + str(self.val) + "\n"
            if self.left:
                ret += self.left.__str__(level + 1, "L---")
            if self.right:
                ret += self.right.__str__(level + 1, "R---")
            return ret

    def __str__(self):
        return self.root.__str__() if self.root else ''

    def insert(self, key):
        if self.root is None:
            self.root = self.Node(key)
            return self.root
        else:
            def _insert(_root, _key):
                if _root is None:
                    _root = self.Node(_key)
                    return _root
                else:
                    if _key < _root.val:
                        _root.left = _insert(_root.left, _key)
                    else:
                        _root.right = _insert(_root.right, _key)
                return _root

            return _insert(self.root, key)

    def max_node_val(self):
        def _max_node(node):
            current = node
            while current.right:
                current = current.right
            return current

        return _max_node(self.root).val

    def min_node_val(self):
        def _min_node(node):
            current = node
            while current.left:
                current = current.left
            return current

        return _min_node(self.root).val

    def sum_nodes_vals(self):
        if not self.root:
            return

        res = 0

        def _node_val(node):
            if node is not None:
                nonlocal res
                res += node.val

                _node_val(node.left)
                _node_val(node.right)

        _node_val(self.root)
        return res
