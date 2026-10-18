"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # Maps original node -> cloned node
        old_to_new = {}

        def dfs(curr: 'Node') -> 'Node':
            # If the node has already been cloned, return the clone
            if curr in old_to_new:
                return old_to_new[curr]

            # Create the clone and record it in the map before recursing
            copy = Node(curr.val)
            old_to_new[curr] = copy

            # Recursively clone all neighbors
            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)