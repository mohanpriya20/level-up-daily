# Count inversions in a list — solution

def count_inversions(arr):
    """
    Return the number of inversions: pairs (i, j) with i < j and arr[i] > arr[j].
    Uses merge sort: count inversions in left half, right half, and while merging.
    """
    return _count_inversions(arr, 0, len(arr) - 1)


def _count_inversions(arr, low, high):
    if low >= high:
        return 0
    mid = (low + high) // 2
    count = _count_inversions(arr, low, mid)
    count += _count_inversions(arr, mid + 1, high)
    count += merge(arr, low, mid, high)
    return count


def merge(arr, low, mid, high):
    temp = []
    i, j = low, mid + 1
    count = 0
    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
            count += mid - i + 1  # remaining left elements are all > this right element
    while i <= mid:
        temp.append(arr[i])
        i += 1
    while j <= high:
        temp.append(arr[j])
        j += 1
    arr[low : high + 1] = temp
    return count



if __name__ == "__main__":
    arr = list(map(int, input("Enter list (space-separated): ").split()))
    result = count_inversions(arr)
    print("Number of inversions:", result)
