# Postfix evaluation — solution

def evaluate_postfix(expr):
    # your logic here
    try:
        stack=[]
        for token in expr:
            if token.isdigit():
                stack.append(token)
            else:
                if len(stack) < 2:
                    raise ValueError("Invalid expression")
                operand2 = stack.pop()
                operand1=stack.pop()
                stack.append(str(eval(f"{operand1}{token}{operand2}")))
        return stack[0]
    except Exception as e:
        print(e)
        return None


if __name__ == "__main__":
    expr = input("Enter postfix expression (space-separated): ").split()
    result = evaluate_postfix(expr)
    print("Result:", result)
