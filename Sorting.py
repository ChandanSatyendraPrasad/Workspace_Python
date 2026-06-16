def bubble_sort(arr):
    # Get the length of the list to sort
    n = len(arr)
    # Iterate over the list n times
    for i in range(n):
        # Track if any swaps happen during this pass
        swapped = False
        # Compare adjacent elements and swap if out of order
        for j in range(0, n - i - 1):
            print(f"Comparing {arr[j]} and {arr[j + 1]}")
            if arr[j] > arr[j + 1]:
                print(f"Swapping {arr[j]} and {arr[j + 1]}")
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(f"List after swap: {arr}")
                swapped = True
        # If no swaps happened, the list is already sorted
        if not swapped:
            break
    return arr


def selection_sort(arr):
    # Determine the length of the list
    n = len(arr)
    # Iterate over each position in the list
    for i in range(n):
        # Assume the current position is the minimum
        min_index = i
        # Find the minimum element in the remainder of the list
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the current element with the found minimum
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def insertion_sort(arr):
    # Iterate over the list starting from the second element
    for i in range(1, len(arr)):
        # Save the current value to insert in the sorted portion
        key = arr[i]
        # Start comparing with the previous element
        j = i - 1
        # Shift elements to the right until the correct spot is found
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        # Insert the saved value into the correct position
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    # If the list is one element or empty, it is already sorted
    if len(arr) <= 1:
        return arr
    # Split the list into two halves
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    merged = []
    i = j = 0
    # Merge the two sorted halves
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    # Add any remaining elements from either half
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def quick_sort(arr):
    # If the list is one element or empty, return it as-is
    if len(arr) <= 1:
        return arr
    # Choose the middle element as the pivot
    pivot = arr[len(arr) // 2]
    # Partition the list into elements less than, equal to, and greater than the pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    # Recursively sort the partitions and combine them
    return quick_sort(left) + middle + quick_sort(right)


def get_numbers(prompt_text):
    # Keep asking the user until valid input is provided
    while True:
        user_input = input(prompt_text).strip()
        if not user_input:
            print("Please enter at least one number.")
            continue
        try:
            # Convert the entered values into integers
            return [int(item) for item in user_input.split()]
        except ValueError:
            print("Invalid input. Enter numbers separated by spaces.")


def main():
    # Define the menu text shown to the user
    menu = (
        "\nSorting Algorithm Menu:\n"
        "1. Bubble Sort\n"
        "2. Selection Sort\n"
        "3. Insertion Sort\n"
        "4. Merge Sort\n"
        "5. Quick Sort\n"
        "6. Exit\n"
    )

    # Main program loop
    while True:
        print(menu)
        choice = input("Choose an algorithm (1-6): ").strip()
        if choice == "6":
            print("Exiting.")
            break
        if choice not in {"1", "2", "3", "4", "5"}:
            print("Invalid choice. Please enter a number between 1 and 6.")
            continue

        # Get the list of numbers from the user
        arr = get_numbers("Enter numbers to sort, separated by spaces: ")

        # Run the selected sorting algorithm
        if choice == "1":
            result = bubble_sort(arr.copy())
            algorithm = "Bubble Sort"
        elif choice == "2":
            result = selection_sort(arr.copy())
            algorithm = "Selection Sort"
        elif choice == "3":
            result = insertion_sort(arr.copy())
            algorithm = "Insertion Sort"
        elif choice == "4":
            result = merge_sort(arr)
            algorithm = "Merge Sort"
        elif choice == "5":
            result = quick_sort(arr)
            algorithm = "Quick Sort"

        # Display the original and sorted lists
        print(f"\n{algorithm} result:\nOriginal: {arr}\nSorted:   {result}\n")


if __name__ == "__main__":
    # Run the main function when the script is executed directly
    main()
