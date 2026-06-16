import mathops as mo

def display_menu():
    print("\n" + "="*50)
    print("     SCIENTIFIC CALCULATOR")
    print("="*50)
    print("1.  Addition (+)")
    print("2.  Subtraction (-)")
    print("3.  Multiplication (*)")
    print("4.  Division (/)")
    print("5.  Power (^)")
    print("6.  Square Root (√)")
    print("7.  Factorial (!)")
    print("8.  Sine (sin)")
    print("9.  Cosine (cos)")
    print("10. Tangent (tan)")
    print("11. Logarithm (log)")
    print("12. Exit")
    print("="*50)

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-12): ")
        
        if choice == '12':
            print("\nThank you for using Scientific Calculator!")
            break
        
        if choice in ['1', '2', '3', '4', '5']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if choice == '1':
                    print(f"Result: {num1} + {num2} = {mo.add(num1, num2)}")
                elif choice == '2':
                    print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"Result: {num1} × {num2} = {mo.multiply(num1, num2)}")
                elif choice == '4':
                    result = mo.divide(num1, num2)
                    print(f"Result: {num1} ÷ {num2} = {result}")
                elif choice == '5':
                    print(f"Result: {num1} ^ {num2} = {mo.power(num1, num2)}")
            except ValueError:
                print("Error: Invalid input. Please enter numeric values.")
        
        elif choice == '6':
            try:
                num = float(input("Enter a number: "))
                result = mo.square_root(num)
                print(f"Result: √{num} = {result}")
            except ValueError:
                print("Error: Invalid input. Please enter a numeric value.")
        
        elif choice == '7':
            try:
                num = float(input("Enter a number: "))
                result = mo.factorial(num)
                print(f"Result: {num}! = {result}")
            except ValueError:
                print("Error: Invalid input. Please enter a numeric value.")
        
        elif choice == '8':
            try:
                angle = float(input("Enter angle in degrees: "))
                result = mo.sine(angle)
                print(f"Result: sin({angle}°) = {result}")
            except ValueError:
                print("Error: Invalid input. Please enter a numeric value.")
        
        elif choice == '9':
            try:
                angle = float(input("Enter angle in degrees: "))
                result = mo.cosine(angle)
                print(f"Result: cos({angle}°) = {result}")
            except ValueError:
                print("Error: Invalid input. Please enter a numeric value.")
        
        elif choice == '10':
            try:
                angle = float(input("Enter angle in degrees: "))
                result = mo.tangent(angle)
                print(f"Result: tan({angle}°) = {result}")
            except ValueError:
                print("Error: Invalid input. Please enter a numeric value.")
        
        elif choice == '11':
            try:
                num = float(input("Enter a number: "))
                base = input("Enter base (press Enter for base 10): ")
                if base == "":
                    result = mo.logarithm(num, 10)
                else:
                    base = float(base)
                    result = mo.logarithm(num, base)
                print(f"Result: log({num}) = {result}")
            except ValueError:
                print("Error: Invalid input. Please enter numeric values.")
        
        else:
            print("Invalid choice. Please select a valid option (1-12).")

if __name__ == "__main__":
    main()
