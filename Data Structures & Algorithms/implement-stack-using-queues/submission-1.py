class MyStack:
    from collections import deque
    def __init__(self):
        self.queue = deque() 
        self.tmp = deque()

    def push(self, x: int) -> None:
        while len(self.queue) > 0:
            self.tmp.append(self.queue.popleft())
        self.queue.append(x)
        while len(self.tmp) > 0:
            self.queue.append(self.tmp.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()