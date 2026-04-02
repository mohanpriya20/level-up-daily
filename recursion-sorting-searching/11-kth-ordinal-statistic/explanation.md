# K-th ordinal statistic — explanation

## Idea

We want the **k-th smallest** element (1-based: k=1 is the minimum, k=n is the maximum) without fully sorting the array. **Quickselect** does this by reusing the partition step from quicksort: after partitioning, the pivot is in its final sorted position, so we know its rank and can recurse on only one half.

## Partition (Lomuto)

We partition with the **last** element as pivot. After partitioning, every element in `arr[0..pivot_index-1]` is ≤ pivot, and every element in `arr[pivot_index+1..n-1]` is > pivot. So the pivot is the **(pivot_index + 1)-th** smallest element (1-based). We return `pivot_index`.

## Recursion

- **pivot_index == k - 1** (0-based): The pivot is the k-th smallest. Return `arr[pivot_index]`.
- **pivot_index > k - 1**: The k-th smallest is in the **left** half. Recurse on `arr[:pivot_index]` and pass **k** unchanged (we still want the k-th smallest in that subarray).
- **pivot_index < k - 1**: The k-th smallest is in the **right** half. We have already “skipped” the first **pivot_index + 1** smallest elements (left part plus pivot). So in the right subarray, the 1st smallest is the (pivot_index+2)-th overall, the 2nd is (pivot_index+3)-th, etc. So the k-th smallest overall is the **(k − pivot_index − 1)-th** smallest in the right subarray. Recurse on `arr[pivot_index+1:]` with **k - pivot_index - 1**.

## Why k - pivot_index - 1 for the right half?

We skip **pivot_index + 1** elements (indices 0..pivot_index). So the rank in the right half is **k − (pivot_index + 1) = k − pivot_index − 1**. Using just **k - pivot_index** would be off by one.

## Base case

If the array is empty, we should return `None` (or handle invalid k). In the recursive calls we always shrink the array (left or right half), so we eventually find the pivot at the correct rank or recurse on a smaller segment.

## Summary

Partition once; if the pivot’s index equals k−1, return it; otherwise recurse on the left (with the same k) or on the right (with k − pivot_index − 1). Average time O(n); worst case O(n²) if the pivot is always at an end.
