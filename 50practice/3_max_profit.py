def maxProfit(prices: list[int]) -> int:
    n = len(prices)
    profit = 0
    l,r = 0,1

    while r < n:
        curr = prices[r] - prices[l]
        if prices[r] > prices[l]:
            profit = max(profit, curr)
        else:
            l = r
        r += 1
    
    return profit
    

answer = maxProfit(prices=[7,1,5,3,6,4])
print("answer is", answer)
