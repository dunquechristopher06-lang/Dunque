class Node:
    """A class representing a node in a Binary Tree."""
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def post_order_traversal(node, result=None):
    """Post-order Traversal: Left -> Right -> Root"""
    if result is None:
        result = []
    if node:
        post_order_traversal(node.left, result)
        post_order_traversal(node.right, result)
        result.append(node.val)
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

    print("--- Post-order Traversal (Left -> Right -> Root) ---")
    print("Result:", post_order_traversal(root))