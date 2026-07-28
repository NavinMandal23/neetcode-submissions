class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for op in tokens:
            if op.isdigit():
                stack.append(int(op))
            elif op[0] == '-' and op[1:].isdigit():
                stack.append(int(op))
            
            if op == '+':
                stack.append(stack.pop() + stack.pop())
            elif op == '*':
                 stack.append(stack.pop() * stack.pop())
            elif op == '-':
                 stack.append(-stack.pop() + stack.pop())
            elif op == '/':
                 stack.append(int(1/stack.pop() * stack.pop()))
            print(op, stack)
        return stack.pop()