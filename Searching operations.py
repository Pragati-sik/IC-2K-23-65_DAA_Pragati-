


# 2. Iterative Binary Search

def iterative_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid

        elif arr[mid] < key:
            low = mid + 1

        else:
            high = mid - 1

    return -1



# Sorting array before binary search
arr.sort()

key = int(input("Enter element to search: "))

# Iterative Search
result1 = iterative_search(arr, key)
print("Iterative Search Result:", result1)

# Recursive Search
result2 = recursive_search(arr, 0, len(arr)-1, key)
print("Recursive Search Result:", result2)


# 4. Measuring Execution Time

sizes = [100, 1000, 5000, 10000]

print("\nExecution Time:")

for n in sizes:

    test_arr = list(range(n))

    start = time.time()
    iterative_search(test_arr, n-1)
    end = time.time()

    print("Size:", n, "Time:", end-start, "seconds")
