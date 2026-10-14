class Solution:

  def isHappy(self, n: int) -> bool:
    # Numbers ke digits ke squares ka sum nikaalne ke liye helper function
    def get_next(num: int) -> int:
      total_sum = 0
      while num > 0:
        digit = num % 10
        total_sum += digit * digit
        num //= 10
      return total_sum

    # Pehle se visit kiye huye numbers ko store karne ke liye hash set
    seen = set()

    # Loop tab tak chalega jab tak number 1 na ban jaye
    # ya phir koi purana number dobara na repeat hone lage (cycle detect ho jaye)
    while n != 1 and n not in seen:
      seen.add(n)
      n = get_next(n)

    # Agar n ki value 1 par aakar ruk gayi toh True, cycle bani toh False
    return n == 1