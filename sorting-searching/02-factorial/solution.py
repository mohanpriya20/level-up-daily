# Factorial (recursion) — solution

def factorial(n):
    """
    Return n! (n factorial). 0! = 1, n! = n * (n-1)! for n >= 1.
    """
    # your logic here
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)


if __name__ == "__main__":
    n = int(input("Enter n: "))
    result = factorial(n)
    print("n! =", result)
