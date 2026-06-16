# num = int(input("Enter a number: "))
# print(num)
# if num >1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(f"{num} is not a prime number")
#             break
#         else:
#             print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")

try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input: please enter an integer")
else:
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print(f"{num} is not a prime number")
                break
        else:
            print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")