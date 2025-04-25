class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        if left == right:
            return 1
        while left < right:
            if right - left == 1:
                if isBadVersion(left):
                    return left
                else:
                    return right
            middle = (left + right) // 2
            if isBadVersion(middle):
                right = middle
            else:
                left = middle