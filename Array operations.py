
import time

# Creating an array (list)
arr = [10, 20, 30, 40, 50]

# Display array
print("Array:", arr)

# 1. Basic Array Operations

# Insertion
arr.append(60)
print("After Insertion:", arr)

# Deletion
arr.remove(30)
print("After Deletion:", arr)

# Searching
print("Searching 40:", arr.index(40))

# Traversal
print("Array Elements:")
for i in arr:
    print(i)


