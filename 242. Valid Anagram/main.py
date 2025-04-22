class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_letter_counts = {}
        t_letter_counts = {}
        for i in range(len(s)):
            s_letter_counts[s[i]] = 1 + s_letter_counts.get(s[i], 0)
            t_letter_counts[t[i]] = 1 + t_letter_counts.get(t[i], 0)
        return True if s_letter_counts == t_letter_counts else False