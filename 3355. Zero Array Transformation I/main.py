class Solution:
    def isZeroArray(self, nums: list[int], queries: list[list[int]]) -> bool:
        n = len(nums)
        diff_array = [0] * (n + 2)

        # Build difference array from queries
        for l, r in queries:
            diff_array[l] += 1
            diff_array[r + 1] -= 1

        # Prefix sum of the difference array
        ops = [0] * n
        curr = 0
        for i in range(n):
            curr += diff_array[i]
            ops[i] = curr
        
        # Check if we can reduce each element of nums to 0
        for i in range(n):
            if nums[i] > ops[i]:
                return False

        return True