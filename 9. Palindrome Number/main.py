class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        div = 1
        while x >= 10 * div:
            div *= 10
        while x:
            low_remainder = x % 10
            high_quotient = x // div
            if low_remainder != high_quotient:
                return False
            x = x % div
            x = x // 10
            div = div / 100
        return True
