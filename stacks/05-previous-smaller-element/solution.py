# Previous Smaller Element (to the left) — solution

def previous_smaller_elements(arr):
    """
    For each index i, return the previous element to the right that is smaller than arr[i].
    If none exists, use None (or -1). Returns a list of same length. Use a stack.
    """
    n = len(arr)
    result = [-1] * n  # -1 when no previous smaller
    stack = []  # indices waiting for their previous smaller to the right

    for i in range(n):
        # arr[i] is the previous smaller for every index j in stack where arr[j] > arr[i]
        while stack and arr[stack[-1]] > arr[i]:
           stack.pop()
        if stack and arr[stack[-1]] < arr[i]:
            result[i] = arr[stack[-1]]
        stack.append(i)
    return result

def previous_smaller_elements_v2(arr):
    result = []
    stack = []
    for i in range(len(arr)):
        while stack and stack[-1] > arr[i]:
                stack.pop()
        if stack and stack[-1] < arr[i]:
            result.append(stack[-1])
        else:
            result.append(-1)
        stack.append(arr[i])
    return result
    

if __name__ == "__main__":
    arr = list(map(int, input("Enter list (space-separated): ").split()))
    nse = previous_smaller_elements(arr)
    print("Previous smaller elements:", nse)
