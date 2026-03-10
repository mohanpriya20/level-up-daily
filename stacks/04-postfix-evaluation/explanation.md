# Postfix evaluation — explanation

## Idea

In postfix (Reverse Polish) notation, the operator comes after its operands. For example, `3 4 +` means “3 + 4”, and `5 2 3 + *` means “5 * (2 + 3)”. We evaluate such an expression using a single stack: we scan tokens left to right, push numbers, and when we see an operator we pop the two operands, apply the operator, and push the result.

## How it works

We assume the expression is already split into tokens (e.g. `["5", "2", "3", "+", "*"]`).

1. **Number** — If the token is a digit (or a multi-digit number; here we use `token.isdigit()` so single-digit tokens are handled), we push it onto the stack. We keep them as strings and only combine them with an operator when we pop.
2. **Operator** — If the token is not a number, it’s an operator (`+`, `-`, `*`, `/`, etc.). We need two operands: we pop the top of the stack as the second operand and the next as the first (order matters for `-` and `/`). We apply the operator (e.g. with `eval(f"{operand1}{token}{operand2}")`), then push the result back as a string so the stack stays uniform.
3. **Invalid expression** — If we see an operator but the stack has fewer than two values, we can’t evaluate; we raise an error and return `None`.
4. **Result** — After processing all tokens, the stack should have one value: the result. We return `stack[0]`.

## Why a stack?

Each operator applies to the “last two values we computed”. So we always need to get the two most recent numbers, use them, and replace them with one number. That’s exactly what a stack does: pop two, compute, push one. The stack holds partial results until they’re used by an operator.

## Input

The main block reads one line with `input(...).split()`, so the user types something like `5 2 3 + *` and we get a list of tokens. That list is passed to `evaluate_postfix`, which assumes each token is either a number (digit string) or an operator.
