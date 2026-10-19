class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        ROWS, COLS = len(board), len(board[0])

        # Helper DFS function to mark border-connected 'O's as safe ('T')
        def capture(r: int, c: int) -> None:
            # Base case: out of bounds or not an 'O'
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != "O":
                return

            # Temporarily mark this cell as visited/safe
            board[r][c] = "T"

            # Traverse all 4 adjacent directions
            capture(r + 1, c)  # Down
            capture(r - 1, c)  # Up
            capture(r, c + 1)  # Right
            capture(r, c - 1)  # Left

        # Step 1: Run DFS for all 'O's located on the borders
        # Check first and last rows
        for c in range(COLS):
            if board[0][c] == "O":
                capture(0, c)
            if board[ROWS - 1][c] == "O":
                capture(ROWS - 1, c)

        # Check first and last columns
        for r in range(ROWS):
            if board[r][0] == "O":
                capture(r, 0)
            if board[r][COLS - 1] == "O":
                capture(r, COLS - 1)

        # Step 2: Final pass to capture surrounded regions and restore safe cells
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    # Fully surrounded 'O's get flipped to 'X'
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    # Border-connected safe cells get restored back to 'O'
                    board[r][c] = "O"