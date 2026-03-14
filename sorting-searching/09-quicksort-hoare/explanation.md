# Quicksort (Hoare, descending) — explanation

## Idea

**Hoare partition** uses two pointers moving from both ends toward the middle, swapping when they find a pair that’s on the wrong sides. This version sorts in **descending** order: left side ≥ pivot, right side ≤ pivot. The pivot is chosen as the **median of three** (first, middle, last element) to improve behavior on sorted or repeated data.

## Median-of-three pivot

`find_median(arr, low, high)` takes `arr[low]`, `arr[mid]`, and `arr[high]`, sorts those three values, and returns the middle one. Using that as the pivot often gives a better split than always using the first or last element.

## Partition (Hoare, descending)

- **Pointers:** `i` starts at `low`, `j` at `high`.
- **Goal:** After partitioning, every element in the left part is ≥ pivot and every element in the right part is ≤ pivot (descending order).
- **Inner loops:**
  - Move `i` right while `i <= j` and `arr[i] > pivot` (element is already “large enough” to be on the left).
  - Move `j` left while `i <= j` and `arr[j] < pivot` (element is already “small enough” to be on the right).
- The bounds `i <= j` prevent the pointers from crossing and avoid going out of range.
- When both stop, we have `arr[i] <= pivot` and `arr[j] >= pivot`, so they’re on the wrong sides. We **swap** `arr[i]` and `arr[j]`, then do `i += 1` and `j -= 1` so we don’t get stuck when values equal the pivot.
- If `i >= j`, we’re done: we return `j` as the partition index. In Hoare, the segment is split into `[low..j]` and `[j+1..high]`; the pivot might be in either side and is not necessarily at `j`.

## Recursion

We recurse on `arr[low..pivot_index]` and `arr[pivot_index+1..high]`. Note: with Hoare, we use `pivot_index` (the returned `j`) as the split point and include `j` in the left subsegment, unlike Lomuto where the pivot is at the returned index and is excluded from both recursive calls.

## Summary

Hoare uses two pointers and swaps pairs that are on the wrong sides; median-of-three chooses the pivot. For descending order, we keep “≥ pivot” on the left and “≤ pivot” on the right. We return `j` and recurse on `[low..j]` and `[j+1..high]`. Advancing `i` and `j` after each swap avoids infinite loops when elements equal the pivot.
