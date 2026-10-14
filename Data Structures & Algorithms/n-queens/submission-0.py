from typing import List


class Solution:

  def solveNQueens(self, n: int) -> List[List[str]]:
    # Columns aur diagonals track karne ke liye sets
    col = set()
    pos_diag = set()  # (r + c) diagonal: bottom-left se top-right
    neg_diag = set()  # (r - c) diagonal: top-left se bottom-right

    res = []
    # n x n empty board create karte hain '.' ke sath
    board = [["."] * n for _ in range(n)]

    def backtrack(r: int):
      # Base Case: Agar saari rows complete ho gayi hain (r == n)
      # toh current board state ko strings mein convert karke result mein add kar lo
      if r == n:
        copy = ["".join(row) for row in board]
        res.append(copy)
        return

      # Current row r ke har column c par queen rakhne ki koshish karte hain
      for c in range(n):
        # Agar column ya diagonals already attack under hain, toh skip karo
        if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
          continue

        # 1. Queen place karo aur sets update karo
        col.add(c)
        pos_diag.add(r + c)
        neg_diag.add(r - c)
        board[r][c] = "Q"

        # 2. Agli row ke liye recurse karo
        backtrack(r + 1)

        # 3. Backtrack: Queen remove karo aur sets se values hatao
        col.remove(c)
        pos_diag.remove(r + c)
        neg_diag.remove(r - c)
        board[r][c] = "."

    # Row 0 se start karte hain
    backtrack(0)
    return res