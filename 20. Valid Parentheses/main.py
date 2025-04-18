class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_map = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        open_brackets = ['(', '[', '{']
        close_brackets = [')', ']', '}']
        stack = []
        for char in s:
            if char in open_brackets:
                stack.append(char)
            if char in close_brackets:
                if len(stack) != 0 and parentheses_map[char] == stack[-1]:
                    stack.pop(-1)
                else:
                    return False
        if len(stack) != 0:
            return False
        return True