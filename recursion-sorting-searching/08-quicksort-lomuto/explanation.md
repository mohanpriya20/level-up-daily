# Quicksort (Lomuto) — explanation

## Idea

Quicksort picks a pivot, partitions the segment so everything ≤ pivot is on the left and everything > pivot is on the right, then recursively sorts the two sides. **Lomuto partition** uses the **last** element as the pivot and a single left-to-right scan with an index `i` that marks the end of the “≤ pivot” region.

## Partition (Lomuto)

- **Pivot:** `arr[high]` (last element).
- **Invariant:** After processing indices up to `j`, all elements in `arr[low..i]` are ≤ pivot, and all in `arr[i+1..j-1]` are > pivot.
- **Single scan:** `j` runs from `low` to `high-1` (we skip the pivot at `high`). For each `j`:
  - If `arr[j] <= pivot`, we extend the “≤” region: do `i += 1` and swap `arr[i]` with `arr[j]`.
  - If `arr[j] > pivot`, we do nothing (it’s already in the “> pivot” region by position).
- **Place pivot:** After the loop, `arr[low..i]` are ≤ pivot and `arr[i+1..high-1]` are > pivot. We swap the pivot `arr[high]` with `arr[i+1]` so the pivot sits between the two regions. The final pivot index is `i+1`.

So we return `i+1` and the segment is split into “≤ pivot” and “> pivot” with the pivot at `i+1`.

## Recursion

If `low < high`, we call `partition_lomuto` to get `pivot_index`, then recursively sort `arr[low..pivot_index-1]` and `arr[pivot_index+1..high]`. The element at `pivot_index` is the pivot and is already in its final place. Base case: when the segment has 0 or 1 element (`low >= high`), we do nothing.

## Summary

Lomuto: one pointer `j` scans left to right; `i` marks the end of the ≤ pivot region. Last element is pivot; after the loop we swap the pivot into position `i+1` and return that index. Then we recurse on the two sides.
