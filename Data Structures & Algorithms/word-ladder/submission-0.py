from collections import defaultdict, deque
from typing import List


class Solution:

  def ladderLength(
      self, beginWord: str, endWord: str, wordList: List[str]
  ) -> int:
    # Agar endWord wordList mein exist hi nahi karta toh sequence banna impossible hai
    if endWord not in wordList:
      return 0

    # 1. Patterns / Adjacency list prepare karte hain
    # Jaise 'hot' ke patterns honge: '*ot', 'h*t', 'ho*'
    pattern_map = defaultdict(list)
    wordList.append(beginWord)

    for word in wordList:
      for j in range(len(word)):
        pattern = word[:j] + "*" + word[j + 1 :]
        pattern_map[pattern].append(word)

    # 2. BFS queue initialize karte hain: (current_word, current_level_length)
    queue = deque([(beginWord, 1)])

    # Visited set banate hain taaki infinite loops avoid ho sakein
    visited = set([beginWord])

    # 3. BFS traversal
    while queue:
      word, length = queue.popleft()

      # Agar hum target word par pahuch gaye toh length return karo
      if word == endWord:
        return length

      # Current word ke saare possible wildcard patterns check karte hain
      for j in range(len(word)):
        pattern = word[:j] + "*" + word[j + 1 :]

        # Is pattern se connect hone wale saare neighboring words explore karte hain
        for neighbor in pattern_map[pattern]:
          if neighbor not in visited:
            visited.add(neighbor)
            queue.append((neighbor, length + 1))

        # Optimization: Is pattern ko clear kar dete hain taaki duplicate work na ho
        pattern_map[pattern] = []

    # Agar endWord tak pahuchne ka koi raasta nahi mila
    return 0