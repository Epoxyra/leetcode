class Solution:
    def longestPalindrome(self, s: str) -> int:
        letter_count_and_position = {}
        max_length = 0
        uneven_included = False
        for i in range(len(s)):
            letter_count_and_position[s[i]] = 1 + letter_count_and_position.get(s[i], 0)
        max_length = 0
        for key in letter_count_and_position:
            max_length += letter_count_and_position[key] // 2 * 2
            if letter_count_and_position[key] % 2 == 1 and not uneven_included:
                max_length += 1
                uneven_included = True       
        return max_length
