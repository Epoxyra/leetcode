class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_count = {}
        ransomNote_count = {}
        for char in magazine:
            magazine_count[char] = 1 + magazine_count.get(char, 0)
        for char in ransomNote:
            ransomNote_count[char] = 1 + ransomNote_count.get(char, 0)

        for key in ransomNote_count:
            if key not in magazine_count:
                return False
            if ransomNote_count[key] > magazine_count[key]:
                return False
        return True
