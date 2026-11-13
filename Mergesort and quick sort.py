def merge_sort(arr):

    if len(arr) > 1:

        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1

            else:
                arr[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


arr = [38, 27, 43, 3, 9, 82, 10]

merge_sort(arr)

print("Sorted array:", arr)



# quick sort.  
def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left = []
    right = []

    for i in arr[1:]:

        if i <= pivot:
            left.append(i)
        else:
            right.append(i)

    return quick_sort(left) + [pivot] + quick_sort(right)


arr = [40, 20, 10, 50, 30, 60]

result = quick_sort(arr)

print("Sorted array:", result)
