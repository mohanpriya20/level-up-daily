# Fibonacci (recursion) — solution

def fib(n, cache):
    """
    Return the nth Fibonacci number (0-indexed).
    fib(0)=0, fib(1)=1, fib(n)=fib(n-1)+fib(n-2).
    """
    # if n==0:
    #     return 0
    # if n==1:
    #     return 1
    # return fib(n-1)+fib(n-2)
    
    #memoization
    if cache is None:
        cache = {}
    if n<=1:
        return n
    if n in cache:
        return cache[n]
    cache[n] = fib(n-1, cache) + fib(n-2, cache)
    return cache[n]


if __name__ == "__main__":
    n = int(input("Enter n: "))
    result = fib(n, None)
    print("fib(n) =", result)
