def binary_search(arr, low, high, key):

    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid

    elif arr[mid] > key:
        return binary_search(arr, low, mid - 1, key)

    else:
        return binary_search(arr, mid + 1, high, key)


arr = [10, 20, 30, 40, 50]

key = int(input("Enter element to search: "))

result = binary_search(arr, 0, len(arr) - 1, key)

if result == -1:
    print("Element not found")
else:
    print("Element found at position:", result + 1)




# maximjm and minimum using divide and conquer



def find_min_max(arr, low, high):

    if low == high:
        return arr[low], arr[low]

    if high == low + 1:
        return min(arr[low], arr[high]), max(arr[low], arr[high])

    mid = (low + high) // 2

    min1, max1 = find_min_max(arr, low, mid)
    min2, max2 = find_min_max(arr, mid + 1, high)

    minimum = min(min1, min2)
    maximum = max(max1, max2)

    return minimum, maximum


arr = [12, 5, 30, 8, 25, 2]

minimum, maximum = find_min_max(arr, 0, len(arr) - 1)

print("Minimum element:", minimum)
print("Maximum element:", maximum)
