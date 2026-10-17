class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        res = []

        def backtrack(i: int, cur: list[int], total: int):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return

            # Include nums[i] (can be reused, stay at index i)
            cur.append(nums[i])
            backtrack(i, cur, total + nums[i])
            cur.pop()

            # Skip nums[i] and move to the next number
            backtrack(i + 1, cur, total)

        backtrack(0, [], 0)
        return res