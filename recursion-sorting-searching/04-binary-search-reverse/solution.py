# Binary search reverse — solution
# Search for target in a sorted array that is in descending order.

def binary_search_reverse(arr, target):
    """
    Return index of target in descending-sorted arr, or -1 if not found.
    """
    # your logic here
    low, high = 0, len(arr)-1
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]==target):
            return mid
        elif(arr[mid]>=target):
            low=mid+1
        else:
            high=mid-1
    return -1


if __name__ == "__main__":
    arr = list(map(int, input("Enter descending-sorted list (space-separated): ").split()))
    target = int(input("Enter target: "))
    result = binary_search_reverse(arr, target)
    print("Index:", result)
