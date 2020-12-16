# Tree

# nodes: root, branches, leaves; childrem, parent, sibling
# nodes: ancestor, descendant
# degree of node: number of childern
# degree of tree: maximum number of childern in tree
# level: root in level 1, any childern level is parent level + 1
# depth/height: maximum level in tree
# edge: connects two nodes
# path: ordered list of nodes that are connected by edges
# binary tree: maximum two children

# 1. List of Lists Representation
myTree = ['a',  # root
          ['b',  # left subtree
           ['d', [], []],
           ['e', [], []]],
          ['c',  # right subtree
           ['f', [], []],
           []]
          ]


# 2. Representation using nodes and references
class BinaryTree:
    def __init__(self, val=None):
        self.val = val
        self.left_child = None
        self.right_child = None

    def insert_left(self, val=None):
        if self.left_child:
            t = BinaryTree(val)
            t.left_child = self.left_child
            self.left_child = t
        else:
            self.left_child = BinaryTree(val)

    def insert_right(self, val=None):
        if self.right_child:
            t = BinaryTree(val)
            t.right_child = self.right_child
            self.right_child = t
        else:
            self.right_child = BinaryTree(val)


# Parse Tree
def parse_tree(expression):
    elist = expression.split()
    # node_list: to save ancestors
    node_list = []
    etree = BinaryTree()
    curr = etree
    # think about it
    node_list.append(curr)

    for x in elist:
        if x == '(':
            node_list.append(curr)
            curr.insert_left()
            curr = curr.left_child
        elif x in ('+', '-', '*', '/'):
            node_list.append(curr)
            curr.val = x
            curr.insert_right()
            curr = curr.right_child
        elif x == ')':
            curr = node_list.pop()
        else:
            curr.val = float(x)
            curr = node_list.pop()

    return etree


# solve parsed tree, recursion
def solve(tree):
    import operator
    symbols = {'+': operator.add, '-': operator.sub,
               '*': operator.mul, '/': operator.truediv}
    left, right = tree.left_child, tree.right_child
    if left and right:
        return symbols[tree.val](solve(left), solve(right))
    else:
        return tree.val


# expression = "( ( 10 + 5 ) * 3 )"
# expression = "( 3 + ( 4 * 5 ) )"
# t = parse_tree(expression)
# a = solve(t)


# Tree Traversals
# 1. preorder method
def preorder(tree):
    if tree:
        print(tree.val)  # or other codes that operate tree.val
        preorder(tree.left_child)
        preorder(tree.right_child)
# parent part, left part, right part


# 2. postordeer method
def preorder(tree):
    if tree:
        preorder(tree.left_child)
        preorder(tree.right_child)
        print(tree.val)
# left part, right part, parent part


# 3. inorder method
def preorder(tree):
    if tree:
        preorder(tree.left_child)
        print(tree.val)
        preorder(tree.right_child)
# left part, parent part, right part
