class Solution:

  def singleNumber(self, nums: List[int]) -> int:
    # Result ko 0 se initialize karte hain
    res = 0

    # Saare numbers par bitwise XOR (^) operation perform karte hain
    # Property:
    # 1. a ^ a = 0 (jo number do baar aayega wo cancel out hoke 0 ban jayega)
    # 2. a ^ 0 = a (kisi number ko 0 ke saath XOR karne par wahi number bachta hai)
    for num in nums:
      res ^= num

    # End mein sirf wahi number bachega jo array mein akela (single) tha
    return res