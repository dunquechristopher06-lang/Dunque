from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_complete_binary_tree(letters):
    """Inserts letters from top to bottom, left to right (Level-Order)."""
    if not letters:
        return None

    root = TreeNode(letters[0])
    queue = deque([root])
    index = 1

    while index < len(letters):
        current = queue.popleft()

        # Insert Left Child
        if index < len(letters):
            current.left = TreeNode(letters[index])
            queue.append(current.left)
            index += 1

        # Insert Right Child
        if index < len(letters):
            current.right = TreeNode(letters[index])
            queue.append(current.right)
            index += 1

    return root


def bfs_level_order(root):
    """BFS: Visit level by level, left to right."""
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        current = queue.popleft()
        result.append(current.value)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return result


def dfs_preorder(node, result=None):
    """DFS Pre-order: Root -> Left -> Right."""
    if result is None:
        result = []
    if node:
        result.append(node.value)
        dfs_preorder(node.left, result)
        dfs_preorder(node.right, result)
    return result


def dfs_inorder(node, result=None):
    """DFS In-order: Left -> Root -> Right."""
    if result is None:
        result = []
    if node:
        dfs_inorder(node.left, result)
        result.append(node.value)
        dfs_inorder(node.right, result)
    return result


def dfs_postorder(node, result=None):
    """DFS Post-order: Left -> Right -> Root."""
    if result is None:
        result = []
    if node:
        dfs_postorder(node.left, result)
        dfs_postorder(node.right, result)
        result.append(node.value)
    return result


if __name__ == "__main__":
    # Last Name: DUNQUE (Second 'U' labeled as 'U2' for clarity)
    letters = ["D", "U", "N", "Q", "U2", "E"]
    root = build_complete_binary_tree(letters)

    print("=== 1. COMPLETE BINARY TREE (DUNQUE) ===")
    print("BFS (Level-Order) :", " -> ".join(bfs_level_order(root)))
    print("DFS (Pre-order)   :", " -> ".join(dfs_preorder(root)))
    print("DFS (In-order)    :", " -> ".join(dfs_inorder(root)))
    print("DFS (Post-order)  :", " -> ".join(dfs_postorder(root)))