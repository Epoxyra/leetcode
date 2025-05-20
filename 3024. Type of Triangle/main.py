class Solution:
    def triangleType(self, nums: list[int]) -> str:
        if nums[0] == nums[1] == nums[2]:
            return "equilateral"
        # Check if the triangle can be formed

        if nums[0] + nums[1] <= nums[2] or nums[1] + nums[2] <= nums[0] or nums[0] + nums[2] <= nums[1]:
            return "none"
        
        a, b, c = sorted(nums)
        if a + b <= c:
            return "none"

        if nums[0] == nums[1] or nums[1] == nums[2] or nums[2] == nums[0]:
            return "isosceles"

        return "scalene"
