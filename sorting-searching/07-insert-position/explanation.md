# Insert position — explanation

## Idea

We want the **index where target would be inserted** so the array stays sorted. That is the smallest index i such that arr[i] >= target (or i = len(arr) if all elements are smaller). So: everything before that index is strictly less than target.

## How the code works

We run a standard binary search. When **arr[mid] == target**, we return mid (target is already there; that’s a valid insert position). When we don’t find target, the loop ends with **low > high**. We then **return low**.

## Why return low when not found?

During the search we only move **low** when we see **arr[mid] < target** — meaning “everything up to and including mid is too small,” so we set **low = mid + 1**. So when the loop exits, every index **j < low** has arr[j] < target. That means the first position where we’re allowed to put target (so that everything before is still < target) is exactly **low**. So the insert position is **low**.

- If target is smaller than arr[0], we end up with low = 0 (insert at start).
- If target is larger than arr[-1], we end up with low = len(arr) (insert at end).
- If target is between two elements, low points to the first index where arr[i] >= target, which is the correct insert position.

## Summary

When target is found we return its index (mid). When it’s not found we return **low**, because everything before low is less than target, so inserting at low keeps the array sorted.
