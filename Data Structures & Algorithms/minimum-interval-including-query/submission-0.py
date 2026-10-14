import heapq
from typing import List


class Solution:

  def minInterval(
      self, intervals: List[List[int]], queries: List[int]
  ) -> List[int]:
    intervals.sort()

    # Queries ko unke original index ke sath sort karte hain
    sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])

    res = [-1] * len(queries)
    min_heap = []  # stores (length, end)
    i = 0
    n = len(intervals)

    for q, original_idx in sorted_queries:
      # 1. Jo intervals current query se pehle ya usi pe start ho rahe hain, heap mein add karo
      while i < n and intervals[i][0] <= q:
        left, right = intervals[i]
        heapq.heappush(min_heap, (right - left + 1, right))
        i += 1

      # 2. Jo intervals query se pehle hi khatam ho chuke hain, unhe discard karo
      while min_heap and min_heap[0][1] < q:
        heapq.heappop(min_heap)

      # 3. Heap ka top element shortest valid interval dega
      if min_heap:
        res[original_idx] = min_heap[0][0]

    return res