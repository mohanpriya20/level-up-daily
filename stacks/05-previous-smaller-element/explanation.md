# Previous Smaller Element — explanation

## Idea

For each index **i**, we want the **first element to the right** that is **smaller** than `arr[i]`. If there is none, we store **-1**. We do this in **one pass** using a **monotonic stack** of indices: when we move right, the current value `arr[i]` can be that "next smaller" for some indices we've already seen (those still on the stack).

## Algorithm

1. **Initialize:** `result = [-1] * n`, empty **stack** of **indices** (not values).

2. **Scan left to right.** For each index **i**:
   - **While** the stack is non-empty and `arr[stack[-1]] > arr[i]`, we have found the first smaller element to the right for the index at the top: it is `arr[i]`. So **pop** that index **j**, set `result[j] = arr[i]`, and repeat.
   - **Push** **i** onto the stack (we don't yet know the next smaller for `arr[i]`).

3. Any index left in the stack at the end has no smaller element to the right, so its result stays **-1**.

## Why the stack works (monotonic stack)

This is the **monotonic stack** pattern: we keep a stack of **indices** whose "next smaller to the right" we haven't found yet. The **values** at those indices form a **non-decreasing** sequence (bottom to top). Whenever we see a value smaller than the top's value, that value is the next smaller for the top (and possibly for more below), so we pop and assign until the stack is empty or the top's value is ≤ current. Then we push the current index. So each index is pushed once and popped at most once → **O(n)** time.

## Example

`arr = [4, 5, 2, 10, 8]`

- **i=0 (4):** stack empty → push 0. Stack: `[0]`.
- **i=1 (5):** 5 > 4 → no pop → push 1. Stack: `[0, 1]`.
- **i=2 (2):** 2 < 5 → pop 1, result[1]=2; 2 < 4 → pop 0, result[0]=2; push 2. Stack: `[2]`.
- **i=3 (10):** 10 > 2 → push 3. Stack: `[2, 3]`.
- **i=4 (8):** 8 < 10 → pop 3, result[3]=8; 8 > 2 → stop; push 4. Stack: `[2, 4]`.

Result: `[2, 2, -1, 8, -1]` — at each index, the value is the first smaller element to the right (or -1).

## Time and space

- **Time:** O(n) — each index is pushed once and popped at most once.
- **Space:** O(n) for the stack and result.
