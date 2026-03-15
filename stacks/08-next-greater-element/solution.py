# Next Greater Element (to the right) — solution

def next_greater_elements(arr):
    """
    For each index i, return the first element to the right that is greater than arr[i].
    If none exists, return -1. Uses a monotonic stack (indices, left-to-right).
    """
    res=[-1]*len(arr)
    stack=[]
    for i in range(len(arr)):
        while stack and arr[i]>arr[stack[-1]]:
            res[stack[-1]]=arr[i]
            stack.pop()
        stack.append(i)
    return res

if __name__ == "__main__":
    arr = list(map(int, input("Enter list (space-separated): ").split()))
    nge = next_greater_elements(arr)
    print("Next greater elements:", nge)
