import heapq


class MedianFinder:

  def __init__(self):
    # small: Max-Heap (chhoti values ke liye, negative value push karenge)
    # large: Min-Heap (badi values ke liye)
    self.small = []
    self.large = []

  def addNum(self, num: int) -> None:
    # 1. By default pehle max-heap (small) mein push karte hain
    heapq.heappush(self.small, -num)

    # 2. Check karte hain ki small ka har element large ke har element se chhota ya equal ho
    # Agar small ka max element large ke min element se bada hai, toh swap/move karo
    if self.small and self.large and (-self.small[0] > self.large[0]):
      val = -heapq.heappop(self.small)
      heapq.heappush(self.large, val)

    # 3. Size balance karte hain:
    # small ka size ya toh large ke barabar hona chahiye ya large se maximum 1 bada
    if len(self.small) > len(self.large) + 1:
      val = -heapq.heappop(self.small)
      heapq.heappush(self.large, val)

    if len(self.large) > len(self.small):
      val = heapq.heappop(self.large)
      heapq.heappush(self.small, -val)

  def findMedian(self) -> float:
    # Agar total elements odd hain, toh median hamesha larger heap (small) ke top par hoga
    if len(self.small) > len(self.large):
      return float(-self.small[0])

    # Agar total elements even hain, toh dono heaps ke top elements ka average median hoga
    return (-self.small[0] + self.large[0]) / 2.0