# Queue Interleaving — solution with queue operations only and for even length

from collections import deque


def interleave_queue(q):
    """
    Reorder the queue so first half is interleaved with second half.
    E.g. queue [1, 2, 3, 4, 5, 6] -> [1, 4, 2, 5, 3, 6].
    Use queue operations only (enqueue/dequeue). Modify q in place or return a new queue.
    """
    first_half = deque()
    for i in range(len(q)//2):
        first_half.append(q.popleft())
    while first_half:
        q.append(first_half.popleft())
        q.append(q.popleft())


if __name__ == "__main__":
    # Example 1: even length
    q1 = deque([1, 2, 3, 4, 5, 6])
    print("Input queue:", list(q1))
    interleave_queue(q1)
    print("Interleaved:", list(q1))  # Expected: [1, 4, 2, 5, 3, 6]

    # Example 2: another queue
    q2 = deque([10, 20, 30, 40])
    print("\nInput queue:", list(q2))
    interleave_queue(q2)
    print("Interleaved:", list(q2))  # Expected: [10, 30, 20, 40]
