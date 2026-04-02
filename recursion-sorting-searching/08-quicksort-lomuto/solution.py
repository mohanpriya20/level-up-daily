# Quicksort — Lomuto partition scheme

def partition_lomuto(arr, low, high):
    """
    Partition arr[low..high] using last element as pivot.
    Elements <= pivot go left, > pivot go right. Return pivot index.
    """
    pivot=arr[high]
    i=low-1
    for j in range(low, high):
        if arr[j]<=pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quicksort_lomuto(arr, low, high):
    """Sort arr[low..high] in place using Lomuto partition."""
    if(low<high):
        pivot_index=partition_lomuto(arr, low, high)
        quicksort_lomuto(arr, low, pivot_index-1)
        quicksort_lomuto(arr, pivot_index+1, high)


if __name__ == "__main__":
    arr = list(map(int, input("Enter list (space-separated): ").split()))
    quicksort_lomuto(arr, 0, len(arr) - 1)
    print("Sorted:", arr)
