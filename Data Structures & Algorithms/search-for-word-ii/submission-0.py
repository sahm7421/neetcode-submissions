from typing import List


class TrieNode:

  def __init__(self):
    self.children = {}
    self.word = None  # Word ka end mark karne ke liye seedha poora word store karte hain


class Solution:

  def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    # 1. Trie build karte hain
    root = TrieNode()
    for w in words:
      node = root
      for char in w:
        if char not in node.children:
          node.children[char] = TrieNode()
        node = node.children[char]
      node.word = w  # Word complete hone par leaf node par word assign karte hain

    ROWS, COLS = len(board), len(board[0])
    res = []

    # 2. Backtracking DFS function
    def dfs(r: int, c: int, parent_node: TrieNode):
      char = board[r][c]
      curr_node = parent_node.children[char]

      # Agar ye node kisi word ka end hai, toh answer mein add karo
      if curr_node.word:
        res.append(curr_node.word)
        curr_node.word = None  # Duplicate entries prevent karne ke liye None kar dete hain

      # Current cell ko temporarily mark karte hain taaki same path mein repeat na ho
      board[r][c] = "#"

      # 4 directions explore karte hain (Up, Down, Left, Right)
      for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if (
            0 <= nr < ROWS
            and 0 <= nc < COLS
            and board[nr][nc] in curr_node.children
        ):
          dfs(nr, nc, curr_node)

      # Backtrack: original character restore karte hain
      board[r][c] = char

      # Optimization (Pruning): Agar is node ke aage koi children nahi bache, toh parent se delete kar do
      if not curr_node.children:
        parent_node.children.pop(char)

    # 3. Har board cell se search initiate karte hain agar wo Trie root mein present hai
    for r in range(ROWS):
      for c in range(COLS):
        if board[r][c] in root.children:
          dfs(r, c, root)

    return res