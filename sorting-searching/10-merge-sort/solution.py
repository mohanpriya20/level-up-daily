# Merge sort — solution

def merge(arr, low, mid, high):
    """
    Merge two sorted halves arr[low..mid] and arr[mid+1..high] into sorted order.
    Use a temporary array, then copy back into arr[low..high].
    """
    # your logic here
    temp=[]
    i=low
    j=mid+1
    while(i<=mid and j<=high):
        if arr[i]<=arr[j]:
            temp.append(arr[i])
            i+=1
        else:
            temp.append(arr[j])
            j+=1
    while(i<=mid):
        temp.append(arr[i])
        i+=1
    while(j<=high):
        temp.append(arr[j])
        j+=1
    arr[low:high+1]=temp

def merge_sort(arr, low, high):
    """Sort arr[low..high] in place using merge sort."""
    # your logic here
    if low >= high:
        return
    mid = (low + high) // 2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid + 1, high)
    merge(arr, low, mid, high)


if __name__ == "__main__":
    arr = list(map(int, input("Enter list (space-separated): ").split()))
    merge_sort(arr, 0, len(arr) - 1)
    print("Sorted:", arr)
