# Predicting Cooler Days — explanation

## Idea

For each day **i**, we want **how many days until** a **strictly cooler** day (a day to the right with lower temperature). If there is no cooler day to the right, we store **-1**. This is the "next smaller element" idea: we need the **first** index to the right where the temperature is lower, and we output the **distance** (that index minus **i**). We use a **monotonic stack** and scan **right to left** so that when we process day **i**, we have already processed all days to its right and the stack gives us the first cooler day.

## Why right to left?

We iterate from the **last** day to the **first** (`i` from `len(temps)-1` down to `0`). So when we are at day **i**, we have already processed all indices **j > i**. The **stack** holds indices of days to the **right** of **i**. After we remove from the stack every index whose temperature is **not** strictly smaller than `temps[i]`, the **top** of the stack (if any) is the **first** day to the right that is **cooler** than day **i**, so the number of days until that day is `stack[-1] - i`.

## Algorithm

1. **Initialize:** `result = [-1] * len(temps)`, empty `stack` of indices.

2. **For each** `i` from right to left:
   - **Pop** from the stack while the day at the top has temperature **>=** `temps[i]` (that day is not strictly cooler than **i**, so it cannot be the "next cooler" for **i**).
   - **After the while loop:**
     - If the stack is **empty**, there is no day to the right that is cooler → leave `result[i] = -1`, push **i**.
     - Else the **top** of the stack is an index **j > i** with `temps[j] < temps[i]`, i.e. the **first** cooler day to the right → set `result[i] = j - i`, then push **i**.

3. **Stack meaning (monotonic stack):** The stack keeps indices of days we have already seen (to the right of the current **i**). By popping while `temps[stack[-1]] >= temps[i]`, we keep only indices that are strictly cooler than **i**; the stack stays **monotonic** (temperatures at stack indices are in a valid order for "first cooler" lookups). The remaining top is the **nearest** index to the right with a strictly smaller temperature, so `result[i] = stack[-1] - i` is the number of days until a cooler day.

## Example

`temps = [30, 60, 90, 120, 60, 30]` (indices 0..5).

- **i=5 (30):** stack empty → result[5]=-1, push 5. Stack: `[5]`.
- **i=4 (60):** temps[5]=30 < 60 → top is cooler. result[4]=5-4=1, push 4. Stack: `[5,4]`.
- **i=3 (120):** temps[4]=60 < 120 → result[3]=4-3=1, push 3. Stack: `[5,4,3]`.
- **i=2 (90):** temps[3]=120 >= 90 → pop 3. temps[4]=60 < 90 → result[2]=4-2=2, push 2. Stack: `[5,4,2]`.
- **i=1 (60):** temps[2]=90 >= 60 → pop 2. temps[4]=60 >= 60 → pop 4. temps[5]=30 < 60 → result[1]=5-1=4, push 1. Stack: `[5,1]`.
- **i=0 (30):** temps[1]=60 >= 30 → pop 1. temps[5]=30 >= 30 → pop 5. Stack empty → result[0]=-1, push 0.

Result: `[-1, 4, 2, 1, 1, -1]`.

## Time and space

- **Time:** O(n) — each index is pushed once and popped at most once.
- **Space:** O(n) for the stack and result.
