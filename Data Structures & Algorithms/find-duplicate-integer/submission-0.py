class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # Phase 1: Cycle ke andar meeting point dhundho
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 2: Cycle ka entrance (duplicate number) dhundho
        slow2 = nums[0]
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow