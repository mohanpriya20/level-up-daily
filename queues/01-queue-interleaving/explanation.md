# Queue Interleaving — explanation

## Idea

We have a queue of **even** length. We want to **interleave** the first half with the second half: the first element stays first, then the first element of the second half, then the second of the first half, then the second of the second half, and so on. Example: `[1, 2, 3, 4, 5, 6]` → `[1, 4, 2, 5, 3, 6]`. We use **only queue operations** (enqueue at back, dequeue from front).

## Algorithm

1. **Split the first half:** Dequeue the first `n/2` elements into a separate queue (e.g. `first_half`). The original queue `q` now contains only the **second half** (in order).

2. **Interleave:** While `first_half` is not empty:
   - Dequeue one element from `first_half` and enqueue it at the back of `q`.
   - Dequeue one element from the **front** of `q` (this is from the second half) and enqueue it at the back of `q`.

So we alternate: one from the first half, one from the (current) front of `q` (which is the second half, moving left to right). The result builds at the back of `q`; when we've used all of the first half, the second half has been consumed in order too, and the queue is fully interleaved.

## Example

Queue: `[1, 2, 3, 4, 5, 6]`, n = 6.

- **Split:** first_half = [1, 2, 3], q = [4, 5, 6].
- **Step 1:** first_half gives 1 → q becomes [4, 5, 6, 1]; front 4 goes to back → [5, 6, 1, 4].
- **Step 2:** first_half gives 2 → [5, 6, 1, 4, 2]; front 5 → [6, 1, 4, 2, 5].
- **Step 3:** first_half gives 3 → [6, 1, 4, 2, 5, 3]; front 6 → [1, 4, 2, 5, 3, 6].

Result: `[1, 4, 2, 5, 3, 6]`.

## Time and space

- **Time:** O(n) — we do a constant number of enqueue/dequeue per element.
- **Space:** O(n) for the auxiliary queue (first half).
