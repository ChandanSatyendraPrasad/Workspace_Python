def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num - 1)
number = int(input("Enter a number to find its factorial: "))
result = fact(number)
print(f"The factorial of {number} is {result}")