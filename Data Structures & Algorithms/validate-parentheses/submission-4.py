class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bkt in s:
            if bkt in '{[(':
                stack.append(bkt)
            elif bkt in '}])':
                if len(stack) != 0 and ((bkt == '}' and stack[-1] == '{') or (bkt == ')' and stack[-1] == '(') or (bkt == ']' and stack[-1] == '[')):
                    stack.pop(-1)
                else:
                    return False
        return stack == []
