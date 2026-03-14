# Sum of even-indexed elements (recursion) — solution

def sum_even_indexed(arr):
    """
    Return the sum of elements at even indices (0, 2, 4, ...) using recursion.
    """
    if len(arr)==0:
        return 0
    if len(arr)==1:
        return arr[0]
    return arr[0]+sum_even_indexed(arr[2:])
    


if __name__ == "__main__":
    arr = list(map(int, input("Enter list (space-separated): ").split()))
    result = sum_even_indexed(arr)
    print("Sum of even-indexed elements:", result)
