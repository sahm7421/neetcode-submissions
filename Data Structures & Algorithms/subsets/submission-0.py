class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        subset = []

        def dfs(i: int):
            # Base case: reached the end of nums
            if i >= len(nums):
                res.append(subset.copy())
                return

            # Decision 1: Include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # Decision 2: Exclude nums[i] (backtrack)
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res