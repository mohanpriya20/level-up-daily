# Predicting Cooler Days Using Temperature Data Analysis — solution

def days_until_cooler(temps):
    """
    For each day i, return how many days until a strictly cooler day (to the right).
    If no cooler day exists, return -1. Uses a stack (monotonic, right-to-left scan).
    """
    res = [-1]*len(temps)
    stack = []
    for i in range(len(temps)):
        while stack and temps[i]<temps[stack[-1]]:
            res[stack[-1]]=i-stack[-1]
            stack.pop()
        stack.append(i)
    return res
            


if __name__ == "__main__":
    print(days_until_cooler([30, 60, 90, 120, 60, 30]))   # Expected: [-1, 4, 2, 1, 1, -1]
    print(days_until_cooler([100, 95, 90, 85, 80, 75]))  # Expected: [1, 1, 1, 1, 1, -1]
    print(days_until_cooler([1]))                          # Expected: [-1]
