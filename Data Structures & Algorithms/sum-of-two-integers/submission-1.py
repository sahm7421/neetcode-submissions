class Solution:

  def getSum(self, a: int, b: int) -> int:
    # 32-bit integer mask banate hain (saare 32 bits 1 rahenge)
    # Python infinite precision integers use karta hai, isliye mask lagana zaroori hai
    mask = 0xFFFFFFFF

    # Jab tak carry (b) zero nahi ho jata
    while b != 0:
      # XOR operation bina carry ka sum deta hai
      sum_without_carry = (a ^ b) & mask

      # AND + Left Shift operation carry deta hai jo agle bit pe jayegi
      carry = ((a & b) << 1) & mask

      a = sum_without_carry
      b = carry

    # 32-bit signed integer check:
    # Agar a ki value 0x7FFFFFFF (positive max) se badi hai, toh ye negative number hai
    # Python mein do's complement convert karne ke liye ~(a ^ mask) use karte hain
    return a if a <= 0x7FFFFFFF else ~(a ^ mask)