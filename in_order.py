class Node:
    """A class representing a node in a Binary Tree."""
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def in_order_traversal(node, result=None):
    """In-order Traversal: Left -> Root -> Right"""
    if result is None:
        result = []
    if node:
        in_order_traversal(node.left, result)
        result.append(node.val)
        in_order_traversal(node.right, result)
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

    print("--- In-order Traversal (Left -> Root -> Right) ---")
    print("Result:", in_order_traversal(root))