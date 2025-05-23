class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = {}
        maximum = 0
        i = 0
        bottom = 0
        while i < len(s):
            if s[i] in hash_map:
                maximum = max(len(hash_map.keys()), maximum)
                new_bottom = hash_map[s[i]] + 1
                for j in range(bottom, hash_map[s[i]] + 1):
                    hash_map.pop(s[j])
                bottom = new_bottom
            hash_map[s[i]] = i
            i += 1
        maximum = max(len(hash_map.keys()), maximum)
        return maximum