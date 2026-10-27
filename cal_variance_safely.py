try:
    data = list(map(float, input("Enter numbers separated by spaces: ").split()))

    if len(data) == 0:
        raise ValueError("At least one number must be provided.")

    mean = sum(data) / len(data)
    squared_diffs = [(x - mean) ** 2 for x in data]
    variance = sum(squared_diffs) / len(data)
    print("The variance of the numbers is:", variance)

except ValueError as e:
    print("Invalid input:", e)