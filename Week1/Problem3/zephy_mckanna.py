"""
Given a binary tree, find its maximum depth
The maximum depth is the number of nodes along the longest path from the root
node down to the farthest leaf node
"""

extra_tests = False

# Constructor to create a new node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def try_next_node(node,max_depth):
    max_left = max_depth
    max_right = max_depth
    if (node.left is not None):
        max_left = try_next_node(node.left, max_depth + 1)
    if (node.right is not None):
        max_right = try_next_node(node.right, max_depth + 1)
    md = max(max_left, max_right)
    return md

def depth_helper(node):
    # bail on zero or one nodes
    if not isinstance(node, Node):
        return 0 # maybe should return an error here?
    if (node.left is None) and (node.right is None):
        return 1

    max_depth = try_next_node(node,1) # note to self: if time, think about how to do this non-recursively

    return max_depth


# PLEASE DO NOT CHANGE THIS
def find_max_depth(tree):
    depth = depth_helper(tree)
    return depth


# test cases
def main():
    if (extra_tests == True):
        # test some edge conditions
        root = []
        print("Depth of tree is %d, and the expected result is 0"
              % (find_max_depth(root),))
        root = Node(1)
        print("Depth of tree is %d, and the expected result is 1"
              % (find_max_depth(root),))
        root = Node(1)
        root.left = Node(2)
        root.left.left = Node(3)
        root.left.left.left = Node(4)
        root.left.left.left.left = Node(5)
        print("Depth of tree is %d, and the expected result is 5"
              % (find_max_depth(root),))
        root = Node(1)
        root.right = Node(2)
        root.right.right = Node(3)
        root.right.right.right = Node(4)
        root.right.right.right.right = Node(5)
        print("Depth of tree is %d, and the expected result is 5"
              % (find_max_depth(root),))
        # and some more complicated trees
        root = Node(1)
        root.right = Node(2)
        root.right.left = Node(3)
        root.right.left.right = Node(4)
        root.right.left.right.left = Node(5)
        print("Depth of tree is %d, and the expected result is 5"
              % (find_max_depth(root),))
        root = Node(1)
        root.right = Node(2)
        root.right.left = Node(3)
        root.right.left.right = Node(4)
        root.right.left.right.left = Node(5)
        root.left = Node(6)
        root.left.left = Node(7)
        root.left.right = Node(8)
        root.left.left.left = Node(9)
        root.left.left.right = Node(10)
        root.left.left.right.left = Node(11)
        root.left.left.right.left = Node(12)
        print("Depth of tree is %d, and the expected result is 5"
              % (find_max_depth(root),))
        root = Node(1)
        root.right = Node(2)
        root.right.left = Node(3)
        root.right.left.right = Node(4)
        root.right.left.right.left = Node(5)
        root.left = Node(6)
        root.left.left = Node(7)
        root.left.right = Node(8)
        root.left.left.left = Node(9)
        root.left.left.right = Node(10)
        root.left.left.right.left = Node(11)
        root.left.left.right.left = Node(12)
        root.left.left.right.left.left = Node(13)
        root.left.left.right.left.right = Node(14)
        root.left.left.right.left.right.right = Node(15)
        print("Depth of tree is %d, and the expected result is 7"
              % (find_max_depth(root),))




    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print("Depth of tree is %d, and the expected result is 3"
          % (find_max_depth(root),))


if __name__ == "__main__":
    main()
