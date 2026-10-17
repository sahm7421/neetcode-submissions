class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        stack = []

        def backtrack(open_n: int, closed_n: int):
            # Base case: valid string formed when open == closed == n
            if open_n == closed_n == n:
                res.append("".join(stack))
                return

            # Only add an open parenthesis if count is less than n
            if open_n < n:
                stack.append("(")
                backtrack(open_n + 1, closed_n)
                stack.pop()

            # Only add a closing parenthesis if closed count is less than open count
            if closed_n < open_n:
                stack.append(")")
                backtrack(open_n, closed_n + 1)
                stack.pop()

        backtrack(0, 0)
        return res