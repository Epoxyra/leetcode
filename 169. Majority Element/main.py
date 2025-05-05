class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        element_counts = {}
        for element in nums:
            element_counts[element] = 1 + element_counts.get(element, 0)
        for key in element_counts:
            if element_counts[key] > len(nums) // 2:
                return key