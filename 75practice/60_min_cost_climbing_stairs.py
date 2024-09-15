def minCostClimbingStairs(cost: list[int]) -> int:
    n = len(cost)
    m = [None for _ in cost]

    def minCost(i, cost, memo):
        if i < 0:
            return 0
        elif i == 0 or i == 1:
            return cost[i]
        elif memo[i] != None:
            return memo[i]
        memo[i] = cost[i] + min(minCost(i - 1, cost, memo), minCost(i - 2, cost, memo))
        return memo[i]

    return min(minCost(n - 1, cost, m), minCost(n - 2, cost, m))


answer = minCostClimbingStairs(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
print("answer is")
print(answer)
