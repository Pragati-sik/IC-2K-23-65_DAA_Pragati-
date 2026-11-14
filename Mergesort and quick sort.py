
# Quick Sort Algorithm in Python

def quick_sort(arr):

    # Base condition
    if len(arr) <= 1:
        return arr

    # Select first element as pivot
    pivot = arr[0]

    left = []
    right = []

    # Divide elements into left and right lists
    for i in arr[1:]:

        if i <= pivot:
            left.append(i)
        else:
            right.append(i)

    # Recursively sort both lists
    return quick_sort(left) + [pivot] + quick_sort(right)


# Main program
try:
    # Take array input from user
    arr = list(map(int, input("Enter array elements separated by spaces: ").split()))

    if not arr:
        print("Error: Array cannot be empty.")
    else:
        print("Original array:", arr)

        # Call Quick Sort function
        result = quick_sort(arr)

        # Display sorted array
        print("Sorted array:", result)

except ValueError:
    print("Error: Please enter only integer values.")
