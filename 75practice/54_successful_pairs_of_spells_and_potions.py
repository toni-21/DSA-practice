from bisect import bisect_left
from math import ceil


def successfulPairs(spells: list[int], potions: list[int], success: int) -> list[int]:
    potions.sort()
    res = []
    n = len(potions)

    for s in spells:
        num = ceil(success / s)
        idx = bisect_left(potions, num)
        res.append(n - idx)

    return res


answer = successfulPairs(spells=[5, 1, 3], potions=[1, 2, 3, 4, 5], success=7)
print("answer is")
print(answer)
