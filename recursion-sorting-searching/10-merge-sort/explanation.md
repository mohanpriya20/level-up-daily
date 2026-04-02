# Merge sort — explanation

## Idea

Merge sort is **divide and conquer**: split the segment in half, recursively sort each half (until they have 0 or 1 element), then **merge** the two sorted halves into one sorted segment. The merge step does the real work by combining two sorted runs in linear time using two pointers.

## Base case

If **low >= high**, the segment has at most one element, so it’s already sorted. We return without doing anything. That stops the recursion.

## Split and recurse

We compute **mid = (low + high) // 2** and recursively sort:
- **arr[low..mid]** (left half),
- **arr[mid+1..high]** (right half).

After these calls return, both halves are sorted. We then call **merge(arr, low, mid, high)** to combine them in place.

## Merge step

We have two sorted halves: **arr[low..mid]** and **arr[mid+1..high]**. We merge them into one sorted run using a **temporary array** and two pointers:

- **i** points at the next element in the left half (starts at low).
- **j** points at the next element in the right half (starts at mid+1).

While both pointers are in range, we compare **arr[i]** and **arr[j]**, append the smaller (or equal) one to **temp**, and advance that pointer. When one half is exhausted, we append the rest of the other half to **temp**. Finally we copy **temp** back into **arr[low..high]** with **arr[low:high+1] = temp**.

So we always take the smaller of the two current elements, which keeps **temp** sorted and gives a single sorted run in **arr[low..high]**.

## Why it works

Each recursive call works on a shorter segment, so we eventually hit the base case. On the way back up, every merge combines two sorted segments into one, so when we return to the top level we have the whole array sorted. Time is O(n log n) because we do O(n) work per level and there are O(log n) levels.
