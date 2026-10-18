class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        parent = list(range(n + 1))
        rank = [1] * (n + 1)

        def find(node: int) -> int:
            while node != parent[node]:
                parent[node] = parent[parent[node]]  # Path compression
                node = parent[node]
            return node

        def union(n1: int, n2: int) -> bool:
            p1, p2 = find(n1), find(n2)

            # If both nodes already share the same root, adding this edge forms a cycle
            if p1 == p2:
                return False

            # Union by rank
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]

        return []