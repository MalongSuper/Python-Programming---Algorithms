# 0/1 Knapsack Problem using Dynamic Programming (Bottom-Up Approach)


def knapsack_tabulation(values, weights, capacity):
    n = len(values)
    table = [[0]*(capacity + 1) for y in range(n + 1)]

    for i in range(1, n+1):
        for w in range(1, capacity+1):
            if weights[i-1] <= w:
                include_item = values[i-1] + table[i-1][w-weights[i-1]]
                exclude_item = table[i-1][w]
                table[i][w] = max(include_item, exclude_item)
            else:
                table[i][w] = table[i-1][w]
    
    for row in table:
        print(row)
    return table[n][capacity]


values = [300, 200, 400, 500]
weights = [2, 1, 5, 3]
capacity = 10
print("\nMaximum value in Knapsack =", knapsack_tabulation(values, weights, capacity))