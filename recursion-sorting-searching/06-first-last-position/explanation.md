# First and Last Position — explanation

## Idea

We want the **first** (leftmost) and **last** (rightmost) index of target in a sorted array. A single binary search that stops when it finds target only gives one occurrence. So we use **two** binary searches: one that keeps searching left when it finds target (to get the first index), and one that keeps searching right when it finds target (to get the last index).

## First index (leftmost)

We do a normal binary search, but when **arr[mid] == target** we don’t return. We record mid as a candidate and set **high = mid - 1** to keep looking for a smaller index. So we only stop when the range is empty. The last time we saw target is the smallest index where it appears → that’s **first**.

## Last index (rightmost)

We do another binary search. When **arr[mid] == target** we don’t return; we record mid and set **low = mid + 1** to keep looking for a larger index. The last time we saw target is the largest index where it appears → that’s **last**.

## Why two passes?

If we tried to do both in one loop, we’d mix “go left for first” and “go right for last” and can end up with last < first or missing one side. Two separate passes keep the logic clear: first pass finds leftmost, second finds rightmost.

## Edge cases

- Empty array: return (-1, -1).
- Target not present: both searches never store a valid index, so first and last stay -1 → (-1, -1).
- Single occurrence: first and last will be the same index.
