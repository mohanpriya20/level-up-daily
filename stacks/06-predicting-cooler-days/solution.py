# Predicting Cooler Days Using Temperature Data Analysis — solution

def days_until_cooler(temps):
    """
    For each day i, return how many days until a strictly cooler day (to the right).
    If no cooler day exists, return -1. Uses a stack (monotonic, right-to-left scan).
    """
    result = [-1] * len(temps)
    stack = []

    for i in range(len(temps) - 1, -1, -1):
        while stack and temps[stack[-1]] >= temps[i]:
            stack.pop()
        if not stack:
            stack.append(i)
        else:
            if temps[stack[-1]] < temps[i]:
                result[i] = stack[-1] - i
                stack.append(i)
    return result


if __name__ == "__main__":
    print(days_until_cooler([30, 60, 90, 120, 60, 30]))   # Expected: [-1, 4, 2, 1, 1, -1]
    print(days_until_cooler([100, 95, 90, 85, 80, 75]))  # Expected: [1, 1, 1, 1, 1, -1]
    print(days_until_cooler([1]))                          # Expected: [-1]
