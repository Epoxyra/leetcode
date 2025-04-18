class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_map = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        stack = []
        for char in s:
            if char in parentheses_map:
                if len(stack) != 0 and parentheses_map[char] == stack[-1]:
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(char)
        return not stack