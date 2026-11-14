
# Dynamic Programming Programs in Python

# 1. Fibonacci using Dynamic Programming
def fibonacci(n):
    dp = [0] * (n + 1)

    if n >= 1:
        dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# 2. Factorial using Dynamic Programming
def factorial(n):
    dp = [1] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = i * dp[i - 1]

    return dp[n]


# 3. 0/1 Knapsack using Dynamic Programming
def knapsack(weights, values, capacity):
    n = len(weights)

    # Create DP table
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):

            # If item weight exceeds capacity
            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]

            else:
                # Choose maximum of including or excluding item
                dp[i][w] = max(
                    dp[i - 1][w],
                    values[i - 1] + dp[i - 1][w - weights[i - 1]]
                )

    return dp[n][capacity]


# 4. Minimum Coins using Dynamic Programming
def minimum_coins(coins, amount):
    # Initialize DP array with infinity
    dp = [float('inf')] * (amount + 1)

    # Zero coins are needed for amount zero
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:

            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[amount] == float('inf'):
        return -1

    return dp[amount]


# Main function
def main():

    while True:
        print("\n--- DYNAMIC PROGRAMMING ---")
        print("1. Fibonacci")
        print("2. Factorial")
        print("3. 0/1 Knapsack")
        print("4. Minimum Coins")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                n = int(input("Enter a number: "))

                if n < 0:
                    print("Error: Enter a non-negative number.")
                else:
                    print("Fibonacci Result:", fibonacci(n))

            elif choice == 2:
                n = int(input("Enter a number: "))

                if n < 0:
                    print("Error: Enter a non-negative number.")
                else:
                    print("Factorial Result:", factorial(n))

            elif choice == 3:
                n = int(input("Enter number of items: "))

                if n <= 0:
                    print("Error: Number of items must be positive.")
                    continue

                weights = []
                values = []

                for i in range(n):
                    weight = int(input(f"Enter weight of item {i + 1}: "))
                    value = int(input(f"Enter value of item {i + 1}: "))

                    if weight <= 0 or value < 0:
                        raise ValueError("Weight must be positive and value non-negative.")

                    weights.append(weight)
                    values.append(value)

                capacity = int(input("Enter knapsack capacity: "))

                if capacity < 0:
                    print("Error: Capacity cannot be negative.")
                else:
                    print("Maximum Value:", knapsack(weights, values, capacity))

            elif choice == 4:
                coins = list(map(int, input("Enter coin values separated by spaces: ").split()))
                amount = int(input("Enter target amount: "))

                if not coins or any(coin <= 0 for coin in coins):
                    print("Error: Coin values must be positive.")
                elif amount < 0:
                    print("Error: Amount cannot be negative.")
                else:
                    result = minimum_coins(coins, amount)

                    if result == -1:
                        print("Amount cannot be formed.")
                    else:
                        print("Minimum Coins Required:", result)

            elif choice == 5:
                print("Program terminated.")
                break

            else:
                print("Invalid choice! Select between 1 and 5.")

        except ValueError as e:
            print("Input Error:", e)


# Start program execution
if __name__ == "__main__":
    main()




