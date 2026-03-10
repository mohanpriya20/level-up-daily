# Bracket balancing — explanation

## Idea

Check whether an expression has balanced brackets: every opening bracket `(`, `{`, `[` has a matching closing bracket `)`, `}`, `]` in the right order, and they’re properly nested. We don’t care about other characters (letters, digits, operators); we only look at brackets.

## Data we use

- **`bracket_map`** — A small dict that maps each closing bracket to its opening pair: `')' → '('`, `'}' → '{'`, `']' → '['`. So when we see a closing bracket, we know which opening bracket must be on top of the stack.
- **`stack`** — We only push opening brackets here. When we see a closing bracket, we check that the top of the stack is its matching open; if so, we pop.

## How it works

We scan the expression character by character.

1. **Non-bracket** — If `char.isalnum()` is true, we skip (we could also allow operators; the point is to ignore anything that isn’t a bracket).
2. **Opening bracket** — If the character is one of `(`, `{`, `[` (i.e. in `bracket_map.values()`), we push it onto the stack.
3. **Closing bracket** — If the character is one of `)`, `}`, `]` (i.e. in `bracket_map`):
   - If the stack is not empty and the top of the stack equals `bracket_map[char]`, that open bracket matches this close — we pop it.
   - Otherwise (stack empty or top doesn’t match), the expression is invalid — we return `False`.

After the loop, every opening bracket we saw should have been matched and popped. So we return `True` only when the stack is empty: `return not stack`. If something is left (e.g. extra `(((`), we return `False`.

## Why a stack?

Closing brackets must match the **most recent** opening bracket. That’s last-in-first-out: the stack’s top is always the current “pending” open bracket we’re waiting to close, so the stack is the right structure for this check.
