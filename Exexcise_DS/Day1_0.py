def validate_arrays(a, b):
    if not isinstance(a, list) or not isinstance(b, list):
        raise TypeError("Both operands must be lists")
    if len(a) != len(b):
        raise ValueError("Arrays must have the same length")


def add_arrays(a, b):
    validate_arrays(a, b)
    return [x + y for x, y in zip(a, b)]


def subtract_arrays(a, b):
    validate_arrays(a, b)
    return [x - y for x, y in zip(a, b)]


def multiply_arrays(a, b):
    validate_arrays(a, b)
    return [x * y for x, y in zip(a, b)]


def divide_arrays(a, b):
    validate_arrays(a, b)
    result = []
    for x, y in zip(a, b):
        if y == 0:
            raise ZeroDivisionError("Division by zero in array element")
        result.append(x / y)
    return result


def basic_operations(a, b):
    return {
        "add": add_arrays(a, b),
        "subtract": subtract_arrays(a, b),
        "multiply": multiply_arrays(a, b),
        "divide": divide_arrays(a, b),
    }


if __name__ == "__main__":
    try:
        array1 = [float(x) if "." in x else int(x)
                  for x in input("Enter first array elements separated by commas: ").split(",")
                  if x.strip()]
        array2 = [float(x) if "." in x else int(x)
                  for x in input("Enter second array elements separated by commas: ").split(",")
                  if x.strip()]

        print("Array 1:", array1)
        print("Array 2:", array2)

        while True:
            print("\nMenu:")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Basic operations")
            print("6. Exit")
            choice = input("Choose an option (1-6): ").strip()

            if choice == "1":
                print("Add:", add_arrays(array1, array2))
            elif choice == "2":
                print("Subtract:", subtract_arrays(array1, array2))
            elif choice == "3":
                print("Multiply:", multiply_arrays(array1, array2))
            elif choice == "4":
                print("Divide:", divide_arrays(array1, array2))
            elif choice == "5":
                results = basic_operations(array1, array2)
                for operation, value in results.items():
                    print(f"{operation.capitalize()}: {value}")
            elif choice == "6":
                print("Exiting.")
                break
            else:
                print("Invalid option. Please choose a number between 1 and 6.")
    except Exception as e:
        print("Error:", e)
