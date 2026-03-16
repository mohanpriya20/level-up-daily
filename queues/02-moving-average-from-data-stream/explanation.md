# Moving Average from Data Stream — explanation

## Idea

We process a **stream** of numbers one at a time. After each new value, we must return the **average of the last `size` values** (or of all values seen so far if we have fewer than `size`). Using a **queue** to keep only the last `size` elements and a **running sum** lets us compute each new average in **O(1)** time.

## Algorithm

1. **State:** Keep:
   - `size` — the window length.
   - A **queue** (e.g. `deque`) holding at most `size` elements (the current window).
   - `total` — the sum of the elements currently in the queue.

2. **next(val):**
   - If the queue already has `size` elements, **dequeue** the front element and subtract it from `total` (so the window slides by one).
   - **Enqueue** `val` at the back and add `val` to `total`.
   - Return `total / len(queue)` (and optionally round). While the window is not yet full, `len(queue)` is less than `size`, so we average over all values seen so far.

## Why a queue?

The window is "last `size` values": when a new value arrives, the **oldest** value in the window drops out. That is exactly **FIFO** — we remove from the front and add at the back. So a queue is the right structure. The running sum avoids summing the window every time and keeps **next()** O(1).

## Example

`size = 3`, stream: 1, 10, 3, 5.

- **next(1):** queue [1], total 1 → avg 1.0.
- **next(10):** queue [1, 10], total 11 → avg 5.5.
- **next(3):** queue [1, 10, 3], total 14 → avg ≈ 4.67.
- **next(5):** full → dequeue 1, total 13; enqueue 5, total 18; queue [10, 3, 5] → avg 6.0.

## Time and space

- **next(val):** O(1).
- **Space:** O(size) for the queue.
