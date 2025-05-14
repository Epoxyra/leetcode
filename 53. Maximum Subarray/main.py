class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sub = nums[0]
        sum = 0
        for num in nums:
            if sum < 0:
                sum = 0
            sum += num
            max_sub = max(max_sub, sum)
        return max_sub