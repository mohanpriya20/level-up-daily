# Max Stack — explanation

## Idea

A **max stack** is a stack that supports the usual `push`, `pop`, and `top`, plus **get_max** in O(1) time. We keep a second stack, **max_stack**, that mirrors the "current maximum so far": whenever we push a value that is **≥** the current maximum (or the stack is empty), we also push it onto max_stack. When we pop, we pop from max_stack **only if** the value we're popping equals the top of max_stack. Then **get_max** is just the top of max_stack.

## Why it works

- **Push:** We only push onto max_stack when the new value is **≥** the current max (or max_stack is empty). So max_stack is **non-increasing** (top is the current max), and we don't push smaller values — they can never become the max after we pop the current top.
- **Pop:** We pop from the main stack. If that value equals the top of max_stack, it was the current max when it was pushed, so we pop it from max_stack too. The new top of max_stack (if any) is the max of the remaining elements.
- **get_max:** The top of max_stack is always the maximum among all elements currently in the stack.

## Duplicates

Using **>=** when pushing onto max_stack (i.e. push when `x >= self.max_stack[-1]`) means duplicate maxima are stored. When we pop one of them, we only pop from max_stack when the popped value **equals** the top of max_stack, so we correctly restore the previous max when multiple copies of the max exist.

## Example

- push(5) → stack: [5], max_stack: [5], get_max: 5  
- push(1) → stack: [5,1], max_stack: [5], get_max: 5  
- push(6) → stack: [5,1,6], max_stack: [5,6], get_max: 6  
- pop() → 6 removed; 6 == max_stack[-1], so max_stack: [5], get_max: 5  

## Time and space

- **push, pop, top, get_max:** O(1).
- **Space:** O(n); max_stack can have up to n elements (e.g. increasing sequence).
