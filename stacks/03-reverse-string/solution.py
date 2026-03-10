# Reverse string — solution
import sys

def reverse_string(s):
    # your logic here
    reversed_string = ""
    stack = list(s)
    for char in stack:
        reversed_string += stack.pop()
    return reversed_string

if __name__ == "__main__":
    s = sys.stdin.readline().rstrip('\n')
    result = reverse_string(s)
    print("Reversed:", result)
 