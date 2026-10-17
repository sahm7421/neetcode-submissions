class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        perm = []
        visited = [False] * len(nums)

        def backtrack():
            # Base case: permutation is complete
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    perm.append(nums[i])

                    backtrack()

                    # Backtrack step
                    perm.pop()
                    visited[i] = False

        backtrack()
        return res