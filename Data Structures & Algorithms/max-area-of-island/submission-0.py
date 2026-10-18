class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def dfs(r: int, c: int) -> int:
            # Check bounds and whether the cell is water or already visited (0)
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0

            # Mark cell as visited by sinking it to 0
            grid[r][c] = 0

            # Count current cell (1) + all connected land in 4 directions
            area = 1
            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)

            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))

        return max_area