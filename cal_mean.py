try:
    n=int(input("How many numbers?"))

    if n<=0:
        raise ValueError("Number must be greater than zero.")

    total=0

    for i in range(n):
        num=float(input("Enter number {}: ".format(i+1)))
        total+=num

    mean=total/n
    print("The mean of the numbers is:", mean)

except ValueError as e:
    print("Invalid input:", e)