class Node:
    """A class representing a node in a Binary Tree."""
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def pre_order_traversal(node, result=None):
    """Pre-order Traversal: Root -> Left -> Right"""
    if result is None:
        result = []
    if node:
        result.append(node.val)
        pre_order_traversal(node.left, result)
        pre_order_traversal(node.right, result)
    return result

if __name__ == "__main__":
    # Sample Tree Construction:
    #         1
    #       /   \
    #      2     3
    #     / \
    #    4   5
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("--- Pre-order Traversal (Root -> Left -> Right) ---")
    print("Result:", pre_order_traversal(root))