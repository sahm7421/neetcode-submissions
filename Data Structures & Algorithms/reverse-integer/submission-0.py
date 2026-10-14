class Solution:

  def reverse(self, x: int) -> int:
    # 32-bit signed integer ki limits define karte hain
    INT_MIN = -(2**31)  # -2147483648
    INT_MAX = 2**31 - 1  #  2147483647

    res = 0
    # Sign ko track karte hain taaki positive aur negative handle ho sake
    sign = -1 if x < 0 else 1
    x = abs(x)

    # Ek-ek digit nikaal kar reverse karte hain
    while x != 0:
      digit = x % 10
      x //= 10

      # Overflow check: agar res ko 10 se multiply karne par INT_MAX cross ho jaye
      if res > INT_MAX // 10 or (
          res == INT_MAX // 10 and digit > INT_MAX % 10
      ):
        return 0

      res = res * 10 + digit

    # Original sign apply karte hain
    res *= sign

    # Final check for underflow (INT_MIN)
    if res < INT_MIN or res > INT_MAX:
      return 0

    return res