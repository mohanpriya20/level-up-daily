# Search in a Rotated Sorted Array — solution
# Array was sorted then rotated. Find target.

def search_rotated(arr, target):
    """
    Return index of target in rotated sorted array, or -1 if not found.
    """
    low, high = 0, len(arr)-1
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>=arr[low]:
            if target>=arr[low] and target<arr[mid]:
                high=mid-1
            else:
                low=mid+1
        else:
            if target>arr[mid] and target<=arr[high]:
                low=mid+1
            else:
                high=mid-1
    return -1


if __name__ == "__main__":
    arr = list(map(int, input("Enter rotated sorted list (space-separated): ").split()))
    target = int(input("Enter target: "))
    result = search_rotated(arr, target)
    print("Index:", result)
