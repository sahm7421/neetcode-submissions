from typing import List


class Solution:

  def missingNumber(self, nums: List[int]) -> int:
    n = len(nums)
    # Result ko n se initialize karte hain
    # (kyunki range [0, n] hai aur loop 0 se n-1 tak chalega)
    res = n

    # Har index i aur array element nums[i] dono ko XOR karte hain
    # Jo numbers array mein present hain wo do baar appear honge (index + value)
    # aur ek dusre ko cancel out kar denge (a ^ a = 0)
    for i in range(n):
      res ^= i ^ nums[i]

    # Sirf wahi number bachega jo range mein tha par nums array mein missing tha
    return res