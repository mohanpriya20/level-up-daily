# Count inversions — explanation

## Idea

An **inversion** is a pair (i, j) with i < j and arr[i] > arr[j]. We count them using the same structure as merge sort: count inversions inside the left half, inside the right half, and **cross-inversions** between the two halves while merging. Because each half is sorted after the recursive calls, we can count cross-inversions in linear time during the merge.

## Divide and recurse

We use a helper `_count_inversions(arr, low, high)` that works on the same array with indices. If **low >= high**, the segment has at most one element, so there are 0 inversions; return 0. Otherwise we set **mid = (low + high) // 2**, recursively count inversions in **arr[low..mid]** and **arr[mid+1..high]**, and then call **merge(arr, low, mid, high)** to merge the two sorted halves and count cross-inversions. The total count is the sum of the two recursive counts plus the count returned by merge.

## Why the array is sorted

The merge step not only counts cross-inversions but also merges the two halves into one sorted segment (same as in merge sort). So when we return from the recursive calls, **arr[low..mid]** and **arr[mid+1..high]** are sorted. That allows the next merge to count cross-inversions correctly.

## Counting cross-inversions in merge

We have two sorted halves: **arr[low..mid]** and **arr[mid+1..high]**. We merge with two pointers **i** (left) and **j** (right). When we take an element from the **right** half (arr[j]), every element still in the left half (from **i** to **mid**) is larger than that right element (because the left half is sorted and we take the smallest first). So taking this right element creates **(mid − i + 1)** new inversions. We add that to **count** and then append arr[j] to the temp array and advance j. When we take from the left (arr[i] ≤ arr[j]), we just append and advance i; no new cross-inversions. When we append the remaining left or right elements, we don’t add any more cross-inversions.

## Summary

Base case: 0 inversions for a segment of length ≤ 1. Otherwise: count inversions in the left half, count in the right half, then merge and add the number of pairs (left element, right element) where the left element is greater—that’s **(mid − i + 1)** each time we take from the right. Total time O(n log n), same as merge sort.
