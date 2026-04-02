# Fibonacci — explanation

## Idea

The nth Fibonacci number (0-indexed) is defined by: fib(0) = 0, fib(1) = 1, and for n ≥ 2, fib(n) = fib(n−1) + fib(n−2). So each number is the sum of the two before it. We can implement this directly with recursion: base cases for 0 and 1, and for larger n we call fib(n−1) and fib(n−2) and add them.

## Base cases

If n is 0 or 1, we return 0 or 1 immediately. That stops the recursion and avoids negative n.

## Recursive step

For any other n, we need fib(n−1) and fib(n−2). So we call fib(n−1) and fib(n−2), add the results, and return that sum. The same function is used for those smaller values, so the recursion eventually reaches 0 and 1.

## Cache (memoization)

The code keeps a small dict `fib_cache` with known values (0 and 1 to start). Before computing fib(n), it checks if n is already in the cache; if so, it returns that value. Otherwise it computes fib(n−1) and fib(n−2), stores the sum in the cache under n, and returns it. Caching avoids recomputing the same n in different branches of the recursion tree. (For a single top-level call, the cache is local to that run; for repeated calls with the same n you’d typically use a shared cache or a global dict so results persist.)

## Summary

Recursion expresses the definition: base cases for 0 and 1, and for n ≥ 2 the answer is the sum of the two previous Fibonacci numbers. The cache stores results so we don’t recompute them when they’re needed again.
