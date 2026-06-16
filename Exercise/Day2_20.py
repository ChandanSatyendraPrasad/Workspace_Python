def add(a,b):
    return (a+b)
def sub(a,b):
    return (a-b)
def mul(a,b):
    return (a*b)
def div(a,b):
    if b != 0:
        return (a/b)
    else:
        return "Error: Division by zero"
def mod(a,b):
    if b != 0:
        return (a%b)
    else:
        return "Error: Division by zero"
def power(a,b):
    return (a**b)  
while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")   
    print("4. Divide")
    print("5. Modulus")
    print("6. Power")
    print("7. Exit")
    choice = input("Enter choice (1/2/3/4/5/6/7): ")
    if choice == '7':
        print("Exiting the calculator. Goodbye!")
        break
    elif choice not in ['1', '2', '3', '4', '5', '6']:
        print("Invalid choice. Please select a valid operation.")
        continue
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        break
    except ValueError:
        print("Invalid input: please enter a number")
if choice == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print(f"{num1} - {num2} = {sub(num1, num2)}")    
elif choice == '3': 
    print(f"{num1} * {num2} = {mul(num1, num2)}")
elif choice == '4':
    print(f"{num1} / {num2} = {div(num1, num2)}")
elif choice == '5': 
    print(f"{num1} % {num2} = {mod(num1, num2)}")
elif choice == '6':
    print(f"{num1} ** {num2} = {power(num1, num2)}")   
else:
    print("Invalid choice. Please select a valid operation.")