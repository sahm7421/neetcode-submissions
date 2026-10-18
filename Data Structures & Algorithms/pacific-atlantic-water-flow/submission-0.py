from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        pac = set()
        atl = set()

        def dfs(r: int, c: int, visit: set, prev_height: int):
            # Check bounds, already visited, or if next cell cannot receive flow (water flows uphill in reverse)
            if (
                r < 0 or r >= rows or 
                c < 0 or c >= cols or 
                (r, c) in visit or 
                heights[r][c] < prev_height
            ):
                return

            visit.add((r, c))

            # Traverse adjacent 4 directions
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # Step 1: Start DFS from horizontal borders
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])                # Top row (Pacific)
            dfs(rows - 1, c, atl, heights[rows - 1][c])  # Bottom row (Atlantic)

        # Step 2: Start DFS from vertical borders
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])                # Left column (Pacific)
            dfs(r, cols - 1, atl, heights[r][cols - 1])  # Right column (Atlantic)

        # Step 3: Intersection of cells reachable by both oceans
        return list(pac & atl)