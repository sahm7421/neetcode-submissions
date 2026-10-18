import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        max_heap = []
        
        for x, y in points:
            # Distance squared from origin: x^2 + y^2
            dist = -(x * x + y * y)
            heapq.heappush(max_heap, (dist, x, y))
            
            if len(max_heap) > k:
                heapq.heappop(max_heap)
                
        return [[x, y] for (_, x, y) in max_heap]