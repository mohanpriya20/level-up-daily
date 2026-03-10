# Reverse string — explanation

## Idea

Reverse the order of characters in a string using a stack. The last character we push becomes the first we pop, so reading by popping gives us the string in reverse order.

## How it works

1. **Load the string onto a stack** — `stack = list(s)` turns the string into a list of characters. We treat that list as a stack (we only use append and pop from the end).
2. **Build the reversed string by popping** — We iterate over the stack and each time we pop one character from the end and add it to `reversed_string`. Because the stack is last-in-first-out, the first character we pop was originally last in the string, the next was second-to-last, and so on. So we get the string in reverse order.
3. **Return** — `reversed_string` is the original string reversed.

## Why a stack?

Reversing is “last character first, then second-to-last, …” — exactly the order you get when you push everything and then pop until empty. So a stack is a natural way to reverse: push all, then pop all.

## Input

The code uses `sys.stdin.readline().rstrip('\n')` so it reads one full line from stdin, including spaces, and strips the trailing newline. That way multi-word or space-separated input is read as a single string before reversing.
