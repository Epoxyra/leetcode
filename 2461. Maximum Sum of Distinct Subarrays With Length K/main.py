class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        if k > len(nums):
            return 0
        max_sum = 0
        found = False
        for i in range(len(nums) - k + 1):
            subarray = nums[i:i+k]
            if len(subarray) == len(set(subarray)):
                found = True
                max_sum = max(max_sum, sum(subarray))
        return max_sum if found else 0
    
nums = [1,5,4,2,9,9,9]
k = 3
solution_instance = Solution()
res = solution_instance.maximumSubarraySum(nums, k)
print(res)