from typing import List


class Solution:

  def countComponents(self, n: int, edges: List[List[int]]) -> int:
    # Each node initially is its own parent
    parent = list(range(n))
    # Rank array to keep the tree flat (union by rank)
    rank = [1] * n

    # Find operation with path compression
    def find(node: int) -> int:
      p = parent[node]
      while p != parent[p]:
        parent[p] = parent[parent[p]]  # Path compression
        p = parent[p]
      return p

    # Union operation: returns 1 if successfully merged, 0 if already connected
    def union(n1: int, n2: int) -> int:
      p1, p2 = find(n1), find(n2)

      # Already part of the same component
      if p1 == p2:
        return 0

      # Attach the smaller rank tree under the larger rank tree
      if rank[p1] >= rank[p2]:
        parent[p2] = p1
        rank[p1] += rank[p2]
      else:
        parent[p1] = p2
        rank[p2] += rank[p1]

      return 1

    # Initially, we have n separate components
    components = n

    # Merge nodes for each edge; decrement component count on every successful merge
    for u, v in edges:
      components -= union(u, v)

    return components