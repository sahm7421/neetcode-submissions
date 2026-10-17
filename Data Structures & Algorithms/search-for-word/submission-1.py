class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r: int, c: int, i: int) -> bool:
            # Successfully matched all characters
            if i == len(word):
                return True

            # Out of bounds or character mismatch
            if (
                r < 0
                or c < 0
                or r >= ROWS
                or c >= COLS
                or board[r][c] != word[i]
            ):
                return False

            # Mark cell as visited
            temp = board[r][c]
            board[r][c] = "#"

            # Explore 4 neighboring directions
            found = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )

            # Backtrack and restore original value
            board[r][c] = temp

            return found

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True

        return False