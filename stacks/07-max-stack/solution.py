# Max Stack — solution

class MaxStack:

    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.max_stack or x >= self.max_stack[-1]:
            self.max_stack.append(x)

    def pop(self):
        if not self.stack:
            return None
        val = self.stack.pop()
        if self.max_stack and val == self.max_stack[-1]:
            self.max_stack.pop()
        return val

    def top(self):
        return self.stack[-1] if self.stack else None

    def get_max(self):
        return self.max_stack[-1] if self.max_stack else None


if __name__ == "__main__":
    stack = MaxStack()
    stack.push(5)
    print(stack.get_max())   # Expected: 5
    stack.push(5)
    stack.push(1)
    print(stack.get_max())   # Expected: 5
    stack.push(6)
    print(stack.get_max())   # Expected: 6
    stack.pop()
    print(stack.get_max())   # Expected: 5
