class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            x1 = nums[i]
            for j in range(i + 1, len(nums)):
                x2 = nums[j]
                sum = x1 + x2
                if sum == target:
                    return [i, j]

nums = [2,7,11,15]
target = 9
solution_instance = Solution()
res = solution_instance.twoSum(nums, target)
print("The resul is :", res)