try:
    n=int(input("Enter the number of elements: "))
    if n <= 0:
        raise ValueError("Number of elements must be greater than zero.")
    else:
        total = 0
        for i in range(n):
            num = float(input("Enter number {}: ".format(i + 1)))
            total += num
        mean = total / n
        print("The mean is:", mean)

except ValueError as e:
    print("Invalid input:", e)