import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        parsed_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        for i in range(len(parsed_s) // 2):
            if parsed_s[i] != parsed_s[- 1 - i]:
                return False
        return True