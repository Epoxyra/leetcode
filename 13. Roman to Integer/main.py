# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_value_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        res = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and symbol_value_map[s[i]] < symbol_value_map[s[i + 1]]:
                res += 9*symbol_value_map.get(s[i]) if s[i + 1] in ["X", "C", "M"] else 4*symbol_value_map.get(s[i])
                i += 2
            else:
                res += symbol_value_map.get(s[i])
                i += 1
        return res