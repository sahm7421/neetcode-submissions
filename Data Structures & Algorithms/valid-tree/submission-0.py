from typing import List


class Solution:

  def validTree(self, n: int, edges: List[List[int]]) -> bool:
    # A valid tree with n nodes must have exactly n - 1 edges
    if len(edges) != n - 1:
      return False

    # Build the undirected adjacency list
    adj = {i: [] for i in range(n)}
    for u, v in edges:
      adj[u].append(v)
      adj[v].append(u)

    visited = set()

    # DFS function to detect cycles and visit connected nodes
    def dfs(node: int, parent: int) -> bool:
      # If the node is already visited, a cycle exists
      if node in visited:
        return False

      visited.add(node)

      for neighbor in adj[node]:
        # Skip the edge back to the direct parent
        if neighbor == parent:
          continue

        # If a cycle is detected down the branch, propagate False
        if not dfs(neighbor, node):
          return False

      return True

    # Start traversal from node 0 with no parent (-1)
    if not dfs(0, -1):
      return False

    # The graph is a valid tree only if all n nodes are connected
    return len(visited) == n