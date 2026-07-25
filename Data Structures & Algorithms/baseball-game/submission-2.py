class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op.isdigit():
                stack.append(int(op))
            
            if op[0] == '-':
                stack.append(int(op[1:])*-1)
        
            if op == '+':
                stack.append(stack[-1] + stack[-2])

            if op == 'C':
                stack.pop()

            if op == 'D':
                stack.append(stack[-1] * 2)

        return sum(stack)