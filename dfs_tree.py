class Node:
    """A class representing a node in a Binary Tree."""

    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class TreeDFS:
    """Class containing Depth-First Search (DFS) traversal methods for trees."""

    def __init__(self, root=None):
        self.root = root

    # 1. Pre-order Traversal (Root -> Left -> Right)
    def pre_order_traversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            result.append(node.val)
            self.pre_order_traversal(node.left, result)
            self.pre_order_traversal(node.right, result)
        return result

    # 2. In-order Traversal (Left -> Root -> Right)
    def in_order_traversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.in_order_traversal(node.left, result)
            result.append(node.val)
            self.in_order_traversal(node.right, result)
        return result

    # 3. Post-order Traversal (Left -> Right -> Root)
    def post_order_traversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.post_order_traversal(node.left, result)
            self.post_order_traversal(node.right, result)
            result.append(node.val)
        return result


# --- Example Usage / Testing ---
if __name__ == "__main__":
    # Constructing a sample binary tree:
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

    tree_dfs = TreeDFS(root)

    print("--- Depth-First Search (DFS) Tree Traversals ---")
    print("Pre-order Traversal  (Root -> Left -> Right):", tree_dfs.pre_order_traversal(root))
    print("In-order Traversal   (Left -> Root -> Right):", tree_dfs.in_order_traversal(root))
    print("Post-order Traversal (Left -> Right -> Root):", tree_dfs.post_order_traversal(root))