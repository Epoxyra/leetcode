class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def helper(nums, target, offset):
            if len(nums) == 0:
                return -1
            if len(nums) == 1:
                return offset if nums[0] == target else -1

            middle_idx = len(nums) // 2
            if target >= nums[middle_idx]:
                return helper(nums[middle_idx:], target, offset + middle_idx)
            else:
                return helper(nums[:middle_idx], target, offset)

        return helper(nums, target, 0)