
# Fractional Knapsack using Greedy Algorithm

# Taking number of items
n = int(input("Enter number of items: "))

items = []

# Taking weight and value of each item
for i in range(n):
    value = int(input("Enter value: "))
    weight = int(input("Enter weight: "))

    ratio = value / weight

    items.append([value, weight, ratio])

# Taking knapsack capacity
capacity = int(input("Enter knapsack capacity: "))

# Sorting items by value/weight ratio (highest first)
items.sort(key=lambda x: x[2], reverse=True)

total_profit = 0

# Selecting items
for item in items:

    value = item[0]
    weight = item[1]

    if capacity >= weight:
        total_profit = total_profit + value
        capacity = capacity - weight

    else:
        fraction = capacity / weight
        total_profit = total_profit + (value * fraction)
        capacity = 0
        break

# Displaying maximum profit
print("Maximum Profit:", total_profit)
