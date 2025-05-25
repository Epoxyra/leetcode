class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        hash_map = {}
        max_len = 0
        for i in range(len(words)):
            word_freq = 1 + hash_map.get(words[i], 0)
            hash_map[words[i]] = word_freq
            reverse_word_freq = hash_map.get(words[i][::-1], 0)
            if word_freq >= 1 and reverse_word_freq >= 1 and words[i][0] != words[i][1]:                
                hash_map[words[i]] = word_freq - 1
                hash_map[words[i][::-1]] = reverse_word_freq - 1
                max_len += 4
            elif words[i][0] == words[i][1] and word_freq >=2:
                hash_map[words[i]] = word_freq - 2
                max_len += 4
        for k, v in hash_map.items():
            if k[0] == k[1] and v == 1:
                return max_len + 2
        return max_len