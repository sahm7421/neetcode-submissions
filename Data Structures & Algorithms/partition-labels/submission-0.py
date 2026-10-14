from typing import List


class Solution:

  def partitionLabels(self, s: str) -> List[int]:
    # 1. Har character ka last index hash map / dictionary mein store karte hain
    last_index = {}
    for i, char in enumerate(s):
      last_index[char] = i

    res = []
    size = 0
    end = 0

    # 2. String ko iterate karte hain aur partition banate hain
    for i, char in enumerate(s):
      size += 1

      # Current character ka last index dekhte hain aur partition ka end expand karte hain
      end = max(end, last_index[char])

      # Agar current index partition ke end par pahuch gaya,
      # iska matlab is partition ke saare characters yahi tak limit hain
      if i == end:
        res.append(size)
        size = 0  # Agle partition ke liye size reset karte hain

    return res