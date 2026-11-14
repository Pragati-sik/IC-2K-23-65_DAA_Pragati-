
# Python Program for Array Operations

# Function to display the array
def display_array(arr):
    print("Current Array:", arr)


# Function to insert an element
def insert_element(arr):
    try:
        value = int(input("Enter element to insert: "))
        arr.append(value)
        print("Element inserted successfully!")
    except ValueError:
        print("Error: Please enter a valid integer.")


# Function to delete an element
def delete_element(arr):
    try:
        value = int(input("Enter element to delete: "))

        if value in arr:
            arr.remove(value)
            print("Element deleted successfully!")
        else:
            print("Error: Element not found.")

    except ValueError:
        print("Error: Please enter a valid integer.")


# Function to update an element
def update_element(arr):
    try:
        index = int(input("Enter index to update: "))

        if 0 <= index < len(arr):
            value = int(input("Enter new value: "))
            arr[index] = value
            print("Element updated successfully!")
        else:
            print("Error: Invalid index.")

    except ValueError:
        print("Error: Please enter valid integers.")


# Function to search an element
def search_element(arr):
    try:
        value = int(input("Enter element to search: "))

        if value in arr:
            print("Element found at index:", arr.index(value))
        else:
            print("Element not found.")

    except ValueError:
        print("Error: Please enter a valid integer.")


# Function to sort the array
def sort_array(arr):
    arr.sort()
    print("Array sorted successfully!")


# Function to traverse the array
def traverse_array(arr):
    print("Array Elements:")
    for element in arr:
        print(element)


# Main function
def main():
    arr = [10, 20, 30, 40, 50]

    while True:
        print("\n--- ARRAY OPERATIONS ---")
        print("1. Display Array")
        print("2. Insert Element")
        print("3. Delete Element")
        print("4. Update Element")
        print("5. Search Element")
        print("6. Sort Array")
        print("7. Traverse Array")
        print("8. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                display_array(arr)

            elif choice == 2:
                insert_element(arr)

            elif choice == 3:
                delete_element(arr)

            elif choice == 4:
                update_element(arr)

            elif choice == 5:
                search_element(arr)

            elif choice == 6:
                sort_array(arr)

            elif choice == 7:
                traverse_array(arr)

            elif choice == 8:
                print("Program terminated.")
                break

            else:
                print("Invalid choice! Enter a number from 1 to 8.")

        except ValueError:
            print("Error: Please enter a valid menu number.")


# Program execution starts here
if __name__ == "__main__":
    main()



