def suggestedProducts(products: list[str], searchWord: str) -> list[list[str]]:
    n = len(products)

    products.sort()
    res = []
    startIdx, endIdx = 0, n - 1
    for i, c in enumerate(searchWord):
        while startIdx <= endIdx and (
            i >= len(products[startIdx]) or products[startIdx][i] < c
        ):
            startIdx += 1
        while startIdx <= endIdx and (
            i >= len(products[endIdx]) or products[endIdx][i] > c
        ):
            endIdx -= 1
        if startIdx <= endIdx:
            res.append(products[startIdx : min(startIdx + 3, endIdx + 1)])
        else:
            res.append([])
    return res


answer = suggestedProducts(
    products=["mobile", "mouse", "moneypot", "monitor", "mousepad"], searchWord="mouse"
)
print("answer is")
print(answer)
