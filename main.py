from collections import deque


# ==========================================
# 1. COMPLETE BINARY TREE IMPLEMENTATION
# ==========================================
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


def tree_bfs_level_order(root):
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


def tree_dfs_preorder(node, result=None):
  if result is None:
    result = []
  if node:
    result.append(node.value)
    tree_dfs_preorder(node.left, result)
    tree_dfs_preorder(node.right, result)
  return result


def tree_dfs_inorder(node, result=None):
  if result is None:
    result = []
  if node:
    tree_dfs_inorder(node.left, result)
    result.append(node.value)
    tree_dfs_inorder(node.right, result)
  return result


def tree_dfs_postorder(node, result=None):
  if result is None:
    result = []
  if node:
    tree_dfs_postorder(node.left, result)
    tree_dfs_postorder(node.right, result)
    result.append(node.value)
  return result


# ==========================================
# 2. UNDIRECTED GRAPH IMPLEMENTATION
# ==========================================
class UndirectedGraph:

  def __init__(self):
    self.adj_list = {}

  def add_vertex(self, vertex):
    if vertex not in self.adj_list:
      self.adj_list[vertex] = []

  def add_edge(self, u, v):
    self.add_vertex(u)
    self.add_vertex(v)
    self.adj_list[u].append(v)
    self.adj_list[v].append(u)

  def bfs(self, start_node):
    visited = set([start_node])
    queue = deque([start_node])
    traversal_order = []

    while queue:
      current = queue.popleft()
      traversal_order.append(current)

      for neighbor in sorted(self.adj_list[current]):
        if neighbor not in visited:
          visited.add(neighbor)
          queue.append(neighbor)

    return traversal_order

  def dfs(self, start_node):
    visited = set()
    stack = [start_node]
    traversal_order = []

    while stack:
      current = stack.pop()

      if current not in visited:
        visited.add(current)
        traversal_order.append(current)

        for neighbor in sorted(self.adj_list[current]):
          if neighbor not in visited:
            stack.append(neighbor)

    return traversal_order


# ==========================================
# MAIN EXECUTION BLOCK
# ==========================================
def main():
  # --- Part 1: Complete Binary Tree ---
  letters = ["D", "U", "N", "Q", "U2", "E"]
  root = build_complete_binary_tree(letters)

  print("==========================================")
  print("1. COMPLETE BINARY TREE (DUNQUE)")
  print("==========================================")
  print("BFS (Level-Order) :", " -> ".join(tree_bfs_level_order(root)))
  print("DFS (Pre-order)   :", " -> ".join(tree_dfs_preorder(root)))
  print("DFS (In-order)    :", " -> ".join(tree_dfs_inorder(root)))
  print("DFS (Post-order)  :", " -> ".join(tree_dfs_postorder(root)))
  print()

  # --- Part 2: Undirected Graph ---
  graph = UndirectedGraph()
  edges = [
      ("D", "U"),
      ("U", "N"),
      ("N", "Q"),
      ("Q", "U2"),
      ("U2", "E"),
      ("E", "D"),
      ("U", "U2"),
  ]
  for u, v in edges:
    graph.add_edge(u, v)

  print("==========================================")
  print("2. UNDIRECTED GRAPH (DUNQUE)")
  print("==========================================")
  print("BFS (Starting at D) :", " -> ".join(graph.bfs("D")))
  print("DFS (Starting at D) :", " -> ".join(graph.dfs("D")))


if __name__ == "__main__":
  main()