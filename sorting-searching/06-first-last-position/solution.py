# First and Last Position of Element in Sorted Array — solution

def first_last_position(arr, target):
    """
    Return (first_index, last_index) of target in sorted arr, or (-1, -1) if not found.
    """
    if not arr:
        return (-1, -1)

    # Binary search for leftmost (first) occurrence
    low, high = 0, len(arr) - 1
    first = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            first = mid
            high = mid - 1  # keep looking left
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    # Binary search for rightmost (last) occurrence
    low, high = 0, len(arr) - 1
    last = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            last = mid
            low = mid + 1  # keep looking right
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return (first, last)


if __name__ == "__main__":
    arr = list(map(int, input("Enter sorted list (space-separated): ").split()))
    target = int(input("Enter target: "))
    result = first_last_position(arr, target)
    print("First and last position:", result)
