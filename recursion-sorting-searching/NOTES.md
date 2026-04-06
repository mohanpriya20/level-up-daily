# Recursion, Sorting & Searching — Notes

---

## Memoization (simple)

**Idea:** Your function is called many times with the **same arguments**. Instead of computing again, **save the answer the first time** and **reuse it**.

**Spelling:** *memo*ization (like a memo), not “memorization.”

### Tiny example: Fibonacci

`F(0)=0`, `F(1)=1`, `F(n)=F(n-1)+F(n-2)`.

Naive code calls `F(2)` many times while computing `F(5)`:

```
F(5) needs F(4) and F(3)
F(4) needs F(3) and F(2)   ← F(3) computed again
F(3) needs F(2) and F(1)   ← F(2) again and again
...
```

**With a dict (cache):**

```python
def fib(n, cache=None):
    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    cache[n] = fib(n - 1, cache) + fib(n - 2, cache)
    return cache[n]
```

First time you see `n`, you compute and **store** `cache[n]`. Next time you **return cache[n]** — no repeat work.

- **Without cache:** time blows up (roughly doubles each +1 on `n`).
- **With cache:** you only compute each `0…n` once → **O(n)** time, **O(n)** space for the dict.

### One sentence summary

**Memoization = remember answers you’ve already computed so you don’t recompute them.**

### Top-down vs bottom-up (optional)

- **Top-down:** recursion + cache (what you did above).
- **Bottom-up:** fill a table from small `n` to big `n` with a loop — same idea, no recursion.

Use either when the same subproblem appears **many times**.

### Sorting / searching

Merge sort, quicksort, binary search **don’t** need this: each recursive step works on **different** data (another half of the array), not the **same** `(n)` again and again.

---

