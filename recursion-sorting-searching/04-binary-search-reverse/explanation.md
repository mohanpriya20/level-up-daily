# Binary search reverse — explanation

## Idea

The array is sorted in **descending** order: larger values on the left, smaller on the right. We still use binary search: check the middle, then eliminate one half. The only change from normal (ascending) binary search is which half we keep when we compare with the target.

## How it works

- **arr[mid] == target** — We found it; return mid.
- **arr[mid] > target** — In a descending array, everything to the left of mid is larger than arr[mid], and everything to the right is smaller. So if arr[mid] is already greater than target, target cannot be to the left (those values are even larger). Target must be in the **right** half (smaller values). So we set **low = mid + 1**.
- **arr[mid] < target** — Then target must be in the **left** half (larger values). So we set **high = mid - 1**.

## Why the opposite of ascending?

In ascending order we do: if arr[mid] < target then go right (low = mid+1); if arr[mid] > target then go left (high = mid-1). In descending order, “larger” is on the left and “smaller” on the right, so the directions flip: when arr[mid] > target we go right (toward smaller values), and when arr[mid] < target we go left (toward larger values).

## Loop exit

When low > high, the range is empty and target is not in the array, so we return -1.
