# Quicksort — Hoare partition scheme (descending order)
def find_median(arr, low, high):
    mid=(low+high)//2
    return sorted([arr[low], arr[mid], arr[high]])[1]


def partition_hoare(arr, low, high):
    """
    Partition arr[low..high] using first element as pivot, for descending order.
    Two pointers from both ends: left side >= pivot, right side <= pivot.
    Return partition index.
    """
    #pivot is the splitting rule for the array
    pivot = find_median(arr, low, high)
    i, j = low, high
    while True:
        while i <= j and arr[i] > pivot:
            i += 1
        while i <= j and arr[j] < pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1


def quicksort_hoare(arr, low, high):
    """Sort arr[low..high] in place in descending order using Hoare partition."""
    # your logic here
    if(low<high):
        pivot_index=partition_hoare(arr, low, high)
        quicksort_hoare(arr, low, pivot_index)
        quicksort_hoare(arr, pivot_index+1, high)

if __name__ == "__main__":
    arr = list(map(int, input("Enter list (space-separated): ").split()))
    quicksort_hoare(arr, 0, len(arr) - 1)
    print("Descending:", arr)
