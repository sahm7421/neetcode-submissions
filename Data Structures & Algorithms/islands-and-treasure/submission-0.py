from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return

        rows, cols = len(grid), len(grid[0])
        q = deque()

        # Step 1: Add all treasure chests (0s) to the queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))

        # Directions: down, up, right, left
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Step 2: Multi-source BFS
        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Only move to valid in-bounds cells that are empty land (INF = 2147483647)
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))