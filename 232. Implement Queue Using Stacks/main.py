class MyQueue:

    def __init__(self):
        self.stack1 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if len(self.stack1) == 0:
            raise ValueError("Pop method must be used on a non-empty queue")
        return self.stack1.pop(0)

    def peek(self) -> int:
        if len(self.stack1) == 0:
            raise ValueError("Peek method must be used on a non-empty queue")
        return self.stack1[0]
        
    def empty(self) -> bool:
        return len(self.stack1) == 0