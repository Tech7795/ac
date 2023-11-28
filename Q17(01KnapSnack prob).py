#@title Q17) 01KnapSnack prob
def knapsack_01(values, weights, capacity):
    n = len(values)
    dp = [0] * (capacity+1)

    for i in range(n):
        for w in range(capacity, 0, -1):
            if weights[i] <= w:
                dp[w] = max(values[i] + dp[w - weights[i]], dp[w])

    return dp[capacity]

# Example usage:
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

result = knapsack_01(values, weights, capacity)

print(f"Maximum value in the knapsack: {result}")
