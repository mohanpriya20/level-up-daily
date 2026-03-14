# Search in a Rotated Sorted Array — explanation

## Idea

The array was originally sorted in ascending order, then **rotated** (e.g. [1,2,3,4,5] → [4,5,1,2,3]). So we have two sorted segments: one from some pivot to the end, then from the start to just before the pivot. We still use binary search, but we must decide which half to keep by checking which half is “normal” sorted and whether target lies in that half.

## Key: one half is always sorted

For any mid, either the **left half [low..mid]** or the **right half [mid..high]** is a contiguous sorted segment. We compare arr[mid] with arr[low] to tell which:

- **arr[mid] >= arr[low]** — The left half [low..mid] is sorted (no wrap in that range).
- **arr[mid] < arr[low]** — The left half has the pivot in it, so the **right** half [mid..high] is sorted.

We then check whether target is inside that sorted half and narrow the range accordingly.

## How the code works

1. **arr[mid] == target** — Found; return mid.

2. **arr[mid] >= arr[low]** (left half sorted):
   - If target is in [arr[low], arr[mid]) (and strictly less than arr[mid]), target must be in the left half → **high = mid - 1**.
   - Otherwise (target > arr[mid] or target < arr[low]) target is in the right half → **low = mid + 1**.

3. **arr[mid] < arr[low]** (right half sorted):
   - If target is in (arr[mid], arr[high]], target must be in the right half → **low = mid + 1**.
   - Otherwise, target is in the left half → **high = mid - 1**.

So we always know which half is sorted and whether target can be there, and we cut the range in half each time.

## Loop exit

When low > high, the range is empty; target is not present, so return -1.
