class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []

        def backtrack(start: int, current: list[int], remain: int):
            if remain == 0:
                res.append(current.copy())
                return

            for i in range(start, len(candidates)):
                # Prune branch: remaining numbers are larger than needed
                if candidates[i] > remain:
                    break

                # Skip duplicate elements at the same recursion level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                current.append(candidates[i])
                # Each element can only be used once, so move to i + 1
                backtrack(i + 1, current, remain - candidates[i])
                current.pop()

        backtrack(0, [], target)
        return res