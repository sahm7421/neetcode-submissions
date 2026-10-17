class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []
        part = []

        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]

        def backtrack(i: int):
            # Base case: reached the end of the string
            if i >= len(s):
                res.append(part.copy())
                return

            # Explore all possible substrings starting at index i
            for j in range(i, len(s)):
                sub = s[i : j + 1]
                if is_palindrome(sub):
                    part.append(sub)
                    backtrack(j + 1)
                    part.pop()  # Backtrack step

        backtrack(0)
        return res