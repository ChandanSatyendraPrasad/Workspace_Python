# # Menu-driven Calculator

# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# def multiply(x, y):
#     return x * y

# def divide(x, y):
#     if y == 0:
#         return "Error: Division by zero"
#     return x / y

# def main():
#     while True:
#         print("\n=== Calculator Menu ===")
#         print("1. Add")
#         print("2. Subtract")
#         print("3. Multiply")
#         print("4. Divide")
#         print("5. Exit")
        
#         choice = input("Enter your choice (1/2/3/4/5): ")
        
#         if choice == '5':
#             print("Thank you for using the calculator!")
#             break
        
#         if choice in ['1', '2', '3', '4']:
#             try:
#                 num1 = float(input("Enter first number: "))
#                 num2 = float(input("Enter second number: "))
                
#                 if choice == '1':
#                     print(f"Result: {num1} + {num2} = {add(num1, num2)}")
#                 elif choice == '2':
#                     print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
#                 elif choice == '3':
#                     print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
#                 elif choice == '4':
#                     result = divide(num1, num2)
#                     if isinstance(result, str):
#                         print(result)
#                     else:
#                         print(f"Result: {num1} / {num2} = {result}")
#             except ValueError:
#                 print("Invalid input! Please enter valid numbers.")
#         else:
#             print("Invalid choice! Please select a valid option.")

# if __name__ == "__main__":
#     main()
# Menu-driven Calculator

def add(x, y):
    # This function adds two numbers
    return x + y

def subtract(x, y):
    # This function subtracts one number from another
    return x - y

def multiply(x, y):
    # This function multiplies two numbers
    return x * y

def divide(x, y):
    # This function divides one number by another
    # It returns an error message if the divisor is zero
    if y == 0:
        return "Error: Division by zero"
    return x / y

def main():
    # This is the main program loop
    while True:
        # Print the menu options
        print("\n=== Calculator Menu ===")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        # Ask the user for their choice
        choice = input("Enter your choice (1/2/3/4/5): ")
        
        # If the user chooses to exit, break out of the loop
        if choice == '5':
            print("Thank you for using the calculator!")
            break
        
        # If the user's choice is valid, ask for the numbers to perform the calculation
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                # Perform the calculation based on the user's choice
                if choice == '1':
                    print(f"Result: {num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"Result: {num1} - pt{num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    result = divide(num1, num2)
                    # If the result is an error message, print it
                    if isinstance(result, str):
                        print(result)
                    # Otherwise, print the result of the calculation2           
                    else:
                        print(f"Result: {num1} / {num2} = {result}")
            except ValueError:
                # If the user enters invalid input, print an error message
                print("Invalid input! Please enter valid numbers.")