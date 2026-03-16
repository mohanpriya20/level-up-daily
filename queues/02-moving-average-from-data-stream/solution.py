# Moving Average from Data Stream — solution
from collections import deque

class MovingAverage:
    """
    Compute the moving average of the last `size` values from a stream.
    next(val) adds val and returns the average of the last `size` elements.
    """

    def __init__(self, size):
        self.size = size
        self.queue = deque()
        self.total = 0

    def next(self, val):
        # your code here
        if len(self.queue)==self.size:
            self.total -= self.queue.popleft()
        self.queue.append(val)
        self.total+=val
        return round((self.total / len(self.queue)), 2)


if __name__ == "__main__":
    # Example: size=3, stream 1, 10, 3, 5
    ma = MovingAverage(3)
    print(ma.next(1))   # 1 / 1 = 1.0
    print(ma.next(10))   # (1 + 10) / 2 = 5.5
    print(ma.next(3))    # (1 + 10 + 3) / 3 = 4.666...
    print(ma.next(5))    # (10 + 3 + 5) / 3 = 6.0 (drop 1)
