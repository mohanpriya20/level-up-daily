# K-th ordinal statistic (K-th smallest element) — solution

def kth_smallest(arr, k):
    """
    Return the K-th smallest element (1-based: k=1 is minimum, k=len(arr) is maximum).
    You may use quickselect, sorting, or another method.
    """
    if(len(arr)>0):
        print(arr)
        pivot_index=partition_lomuto(arr, 0, len(arr)-1)
        if pivot_index==k-1:
            return arr[pivot_index]
        elif pivot_index>k-1:
            return kth_smallest(arr[:pivot_index], k)
        else:
            return kth_smallest(arr[pivot_index+1:], k-pivot_index-1) 
            #since we are passing only right half of the array, the index of the target is k-pivot_index-1 
            #because the array is shrunk by pivot_index+1 elements and we are only passsing the right half
            
def partition_lomuto(arr, left, right):
    pivot=arr[right]
    i=left-1
    for j in range(left, right):
        if arr[j]<=pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i+1

if __name__ == "__main__":
    arr = list(map(int, input("Enter list (space-separated): ").split()))
    k = int(input("Enter k (1-based): "))
    result = kth_smallest(arr, k)
    print("K-th smallest:", result)
