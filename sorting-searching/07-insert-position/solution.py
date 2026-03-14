# Find or Define Insert Position in a Sorted List — solution

def insert_position(arr, target):
    """
    Return the index where target would be inserted to keep arr sorted.
    If target is already present, return its index (or leftmost insert position).
    """
    low, high = 0, len(arr)-1
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return low

if __name__ == "__main__":
    arr = list(map(int, input("Enter sorted list (space-separated): ").split()))
    target = int(input("Enter target: "))
    result = insert_position(arr, target)
    print("Insert position:", result)
