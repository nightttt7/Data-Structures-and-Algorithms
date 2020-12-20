# Tree

# nodes: root, branches, leaves; childrem, parent, sibling
# nodes: ancestor, descendant
# degree of node: number of childern
# degree of tree: maximum number of childern in tree
# edge: connects two nodes
# level: root in level 1, any childern level is parent level + 1
# height: maximum number of edges from node to leaf, max(level_leaf-level_node)
# depth: number of edges form node to root (level_node-1)
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
        self.left = None
        self.right = None

    def insert_left(self, val=None):
        if self.left:
            t = BinaryTree(val)
            t.left = self.left
            self.left = t
        else:
            self.left = BinaryTree(val)

    def insert_right(self, val=None):
        if self.right:
            t = BinaryTree(val)
            t.right = self.right
            self.right = t
        else:
            self.right = BinaryTree(val)


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
            curr = curr.left
        elif x in ('+', '-', '*', '/'):
            node_list.append(curr)
            curr.val = x
            curr.insert_right()
            curr = curr.right
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
    left, right = tree.left, tree.right
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
        preorder(tree.left)
        preorder(tree.right)
# parent part, left part, right part


# 2. postordeer method
def postordeer(tree):
    if tree:
        postordeer(tree.left)
        postordeer(tree.right)
        print(tree.val)
# left part, right part, parent part


# 3. inorder method
def inorder(tree):
    if tree:
        inorder(tree.left)
        print(tree.val)
        inorder(tree.right)
# left part, parent part, right part


# Binary Heap, complete tree, List Representation
# NB! only need to get a Min-heap (but not a sorted list):
#   nodes can't have a smaller value than its parent
# we start form 0: (i-1)//2 is parent, 2i+1 and 2i+2 is children
# if start form 1: i//2 is parent, 2i and 2i+1 is children
class Heap:
    def __init__(self):
        self.heap_list = []

    def move_up(self, i):
        while (i-1)//2 >= 0 and self.heap_list[i] < self.heap_list[(i-1)//2]:
            (self.heap_list[i], self.heap_list[(i-1)//2]) = (
                self.heap_list[(i-1)//2], self.heap_list[i])
            i = (i-1)//2

    # insert x from heap end
    def insert(self, x):
        self.heap_list.append(x)
        self.move_up(self.heap_list.__len__())

    def move_down(self, i):
        n = self.heap_list.__len__()
        while 2*i+1 < n:
            min_ = i
            left = 2*i+1
            right = 2*i+2
            if self.heap_list[min_] > self.heap_list[left]:
                min_ = left
            if right < n:
                if self.heap_list[min_] > self.heap_list[right]:
                    min_ = right
            if min_ != i:
                (self.heap_list[i], self.heap_list[min_]) = (
                    self.heap_list[min_], self.heap_list[i])
                i = min_
            else:
                break

    def delete_min(self):
        # save min
        min_ = self.heap_list[0]
        # max replace min
        self.heap_list[0] == self.heap_list[-1]
        # delete end
        self.heap_list.pop()
        # move_down max
        self.move_down(0)
        return min_

    def buildHeap(self, input_list):
        i = (len(input_list)-1) // 2
        self.heap_list = input_list
        while (i >= 0):
            self.move_down(i)
            i = i - 1


# h = Heap()
# h.buildHeap([9, 5, 6, 2, 3, 5, 3, 5, 78, 4, 56,
#              7, 4, 3, 5, 6, 7, 98, 76, 6, 454])
# h.heap_list

# Application of Heap: see "Heap Sort" in Sorting.py


# Binary Search Trees (the tree implementation of dictionary)
# BST property: smaller than parent on the left subtree, greater on right
# sometimes I use "if x is not None:", but most cases "if x:" is enough
class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        self.balance_factor = 0

    def update(self, key, val, left, right):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self

    # NB! it is recursion
    # traversal method is inorder method
    def __iter__(self):
        if self is not None:
            if self.left:
                for x in self.left:
                    yield x
            yield self.key
            if self.right:
                for x in self.right:
                    yield x


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    # to use recursion, must divide into 2 function
    # best case: O(log(n)), worst case: o(n)
    def __setitem__(self, key, val):
        if self.root is None:
            self.root = TreeNode(key, val)
        else:
            self._set(key, val, self.root)
        self.size += 1

    # recurtion part of self.__setitem__
    def _set(self, key, val, node):
        if key < node.key:
            # base case
            if node.left is None:
                node.left = TreeNode(key, val, parent=node)
            # move on
            else:
                self._set(key, val, node.left)
        else:
            # base case
            if node.right is None:
                node.right = TreeNode(key, val, parent=node)
            # move on
            else:
                self._set(key, val, node.right)

    # to use recursion, must divide into 2 function (loop also works)
    def __getitem__(self, key):
        return self._get(key, self.root).val

    # recurtion part of self.__getitem__, return a treenode
    def _get(self, key, node):
        if node is None:
            raise KeyError(key)
        elif key == node.key:
            return node
        elif key < node.key:
            return self._get(key, node.left)
        else:
            return self._get(key, node.right)

    # to overloads the 'in' operator
    def __contains__(self, key):
        try:
            if self._get(key, self.root) is not None:
                return True
        except Exception:
            return False

    # 'del' operator
    def __delitem__(self, key):
        if self.size == 1 and self.root.key == key:
            self.root = None
            self.size = 0
        elif self.size <= 1:
            raise KeyError(key)
        else:
            node = self._get(key, self.root)
            if node:
                self._remove(node)
                self.size -= 1
            else:
                raise KeyError(key)

    # remove is complex, and may be used in other places
    def _remove(self, node):
        # no child
        if (node.left is None) and (node.right is None):
            if node == node.parent.left:
                node.parent.left = None
            else:
                node.parent.right = None
        # 2 children
        elif (node.left is not None) and (node.right is not None):
            # replaced by a successor
            # successor could be max in left (I use it), or min in right
            successor = node.left
            while successor.right:
                successor = successor.right
            # the successor can't have right
            if successor.left:
                if successor.parent.left == successor:
                    successor.parent.left = successor.left
                else:
                    successor.parent.right = successor.left
            # successor has no child
            else:
                successor.parent.left = None
                successor.parent.right = None
            node.key = successor.key
            node.val = successor.val
        # 3 cases for each below:
        # node is left child, right child or root (no parent)
        # only left
        elif node.left:
            if node.parent:
                node.left.parent = node.parent
                if node.parent.left == node:
                    node.parent.left = node.left
                else:
                    node.parent.right = node.left
            else:
                node.update(node.left.key, node.left.val,
                            node.left.left, node.left.right)
        # only right
        else:
            if node.parent:
                node.right.parent = node.parent
                if node.parent.left == node:
                    node.parent.left = node.right
                else:
                    node.parent.right = node.right
            else:
                node.update(node.right.key, node.right.val,
                            node.right.left, node.right.right)


# b = BST()
# b[53] = 'a'
# b[24] = 'b'
# b[13] = 'c'
# b[78] = 'd'
# b[57] = 'e'
# b[87] = 'f'
# b[36] = 'g'
# b[22] = 'h'
# b[1] = 'i'
# b[65] = 'j'
# b.root.val
# b.root.left.val
# b.root.right.val
# b.root.left.left.val
# b.root.left.left.left.val
# b.root.left.left.left.left.val
# b[22]
# b[87]
# b[99]
# 87 in b
# 99 in b
# del b[53]
# b[53]
# del b[22]
# for x in b:
#     print(x)


# Balanced Binary Search Trees
# also AVL tree (named for its inventors: G.M. Adelson-Velskii and E.M. Landis)
class BBST(BST):

    def _set(self, key, val, node):
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key, val, parent=node)
                # new codes
                self.update_balance(node.left)
            else:
                self._set(key, val, node.left)
        else:
            if node.right is None:
                node.right = TreeNode(key, val, parent=node)
                # new codes
                self.update_balance(node.right)
            else:
                self._set(key, val, node.right)

    # find the unbalanced subtree with max depth
    def update_balance(self, node):
        # base case
        if abs(node.balance_factor) > 1:
            self.rabalance(node)
        # move on
        elif node.parent:
            if node.left:
                node.parent.balance_factor += 1
            elif node.right:
                node.parent.balance_factor -= 1
            if node.parent.balance_factor != 0:
                # call self
                self.update_balance(node.parent)

    def rebalance(self, node):
        # node is right heavy (here balance_factor = -2)
        if node.balance_factor < 0:
            # right child is left heavy (here balance_factor = 1)
            if node.right.balance_factor > 0:
                self.rotate_right(node.right)
                self.rotate_left(node)
            # right child not left heavy
            else:
                self.rotate_left(node)
        # node is left heavy (here balance_factor = 2)
        if node.balance_factor > 0:
            # left child is right heavy (here balance_factor = -1)
            if node.left.balance_factor < 0:
                # use this case as example:
                # left will be new root, root will be new right
                # right of left will be new left of new right (level unchange)
                # left of left will be new left (level-1)
                # level of left of left can't be smaller than right of left
                # (that is, left.balance_factor can't < 0)
                # so we rotate_left left at first
                self.rotate_left(node.left)
                self.rotate_right(node)
            # right child not right heavy
            else:
                self.rotate_right(node)

    # to rotate from right to left (to let left heavier)
    # need to move root right
    def rotate_left(self, node):
        # the order of codes below most important
        root = node
        new_root = root.right
        # connect between root and new_root.left
        # if new_root.left is None, just right, let root.right be None
        root.right = new_root.left
        # if new_root.left is None, no need to do this
        if new_root.left is not None:
            new_root.left.parent = root
        # conncet new_root to tree
        if root.parent is None:
            self.root = new_root
        elif root.parent.left == root:
            root.parent.left = new_root
        else:
            root.parent.right = new_root
        # connect between new_root and root
        new_root.left = root
        root.parent = new_root
        # update balance, 2 lines enough, not use update_balance()
        root.balance_factor = (
            root.balance_factor + 1 - min(new_root.balance_factor, 0))
        new_root.balance_factor = (
            new_root.balance_factor + 1 + max(root.balance_factor, 0))

    def rotate_right(self, node):
        pass

    def __delitem__(self, key):
        pass

    def _remove(self, node):
        pass
