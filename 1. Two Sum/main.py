class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Store the numbers we have already encountered from the nums list and map them to their index
        already_seen_map = dict()
        for i in range(len(nums)):
            x1 = nums[i]
            x2 = target - x1
            if x2 in already_seen_map:
                return [i, already_seen_map[x2]]
            else:
                already_seen_map[x1] = i