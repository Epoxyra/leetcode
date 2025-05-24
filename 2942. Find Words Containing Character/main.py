class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        res_list = []
        for i in range(len(words)):
            if x in words[i]:
                res_list.append(i)
        return res_list