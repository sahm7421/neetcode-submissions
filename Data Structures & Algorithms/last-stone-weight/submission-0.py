import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # Python provides a min-heap by default; invert values to simulate a max-heap
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            first = heapq.heappop(max_heap)   # Heaviest stone (most negative)
            second = heapq.heappop(max_heap)  # Second heaviest stone

            if first != second:
                # first is smaller (more negative), so first - second is negative
                heapq.heappush(max_heap, first - second)

        # If a stone remains, invert it back; otherwise, return 0
        return -max_heap[0] if max_heap else 0