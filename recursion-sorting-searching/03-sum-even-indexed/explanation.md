# Sum of even-indexed — explanation

## Idea

We want the sum of elements at even indices: index 0, 2, 4, 6, … So for [a, b, c, d, e] we want a + c + e. We do it recursively: take the first element (index 0), then handle the rest. The “rest” should be the part of the list that still has even-indexed positions relative to the original—that’s everything from index 2 onward. In the sublist arr[2:], the element at position 0 is the original index 2, position 1 is original index 3, and so on. So the even-indexed elements of arr[2:] (positions 0, 2, 4, … in the sublist) are exactly the original indices 2, 4, 6, …. So the total sum is arr[0] + sum_even_indexed(arr[2:]).

## Base cases

- **Empty list** — There are no even-indexed elements, so the sum is 0. We return 0 and stop.
- **Single element** — The only even index is 0, so the sum is arr[0]. We return it and stop.

## Recursive step

For a list of length at least 2, we take the first element arr[0] and add the sum of even-indexed elements of arr[2:]. That recursive call works on a shorter list and will eventually hit one of the base cases.

## Why arr[2:]?

Skipping one position (index 1) keeps the alignment: the “first” element of the sublist is the original index 2, so indexing in the sublist by 0, 2, 4, … still means original indices 2, 4, 6, …. So one step is “take index 0” and “recurse on from index 2 onward.”

## Summary

Base cases: empty list → 0, one element → that element. Otherwise: first element plus the sum of even-indexed elements of the list starting at index 2. The recursion always works on a shorter list and ends at an empty or single-element list.
