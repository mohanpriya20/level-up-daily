# Bracket balancing — solution

def is_balanced(expr):
    bracket_map={
        ')': '(',
        '}': '{',
        ']': '['
    }
    stack=[]
    for char in expr:
        if char.isalnum():
            continue
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map:
            if stack and bracket_map[char] == stack[-1]:
                stack.pop()
            else:
                return False
    return not stack


if __name__ == "__main__":
    expr = input("Enter expression: ")
    result = is_balanced(expr)
    print("Balanced" if result else "Not balanced")
