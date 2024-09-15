def maxProfit(prices: list[int], fee: int) -> int:
    sell = 0
    buy = -prices[0]

    for price in prices:
        buy = max(buy, sell - price)
        sell = max(sell, buy + price - fee)

    return sell


answer = maxProfit(prices=[1, 3, 2, 8, 4, 9], fee=2)
print("answer is")
print(answer)
