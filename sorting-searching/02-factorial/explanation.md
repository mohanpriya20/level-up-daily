# Factorial — explanation

## Idea

The factorial of n (written n!) is the product of the positive integers from 1 up to n. By convention, 0! = 1. So 1! = 1, 2! = 2, 3! = 6, 4! = 24, and so on. We can define it recursively: n! = n × (n−1)! for n ≥ 1, with 0! = 1 (and often 1! = 1 as a base case too).

## Base case

If n is 0 or 1, we return 1. That’s the end of the recursion: we don’t call factorial again for smaller n.

## Recursive step

For n ≥ 2, we use the definition n! = n × (n−1)!. So we compute factorial(n−1), multiply it by n, and return that. The call to factorial(n−1) will itself recurse until it hits 0 or 1, then the multiplications happen on the way back up.

## Why it works

Each call reduces the problem to a smaller one (n − 1). The chain of calls goes n → n−1 → … → 1 → 0, then returns 1, then each level multiplies by its n and returns. So we get n × (n−1) × … × 1 = n!.

## Summary

Factorial is defined by a base case (0 or 1 returns 1) and a recursive case (n! = n × (n−1)!). The code matches that: base case returns 1, otherwise return n * factorial(n−1).
