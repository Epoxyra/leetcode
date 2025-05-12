class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        ints_set = set()
        for int in nums:
            if int not in ints_set:
                ints_set.add(int)
            else:
                return True
        return False
