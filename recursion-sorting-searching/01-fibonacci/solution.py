# Fibonacci (recursion) — solution

def fib(n):
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
    fib_cache={0:0,1:1}
    if n in fib_cache:
        return fib_cache[n]
    fib_cache[n]=fib(n-1)+fib(n-2)
    return fib_cache[n]


if __name__ == "__main__":
    n = int(input("Enter n: "))
    result = fib(n)
    print("fib(n) =", result)
