from math import ceil


def minEatingSpeed(piles: list[int], h: int) -> int:
    if h == len(piles):
        return max(piles)
    left, right = 1, max(piles)
    while left < right:
        mid = (left + right) // 2
        hrs = 0
        for p in piles:
            if p < mid:
                hrs += 1
            else:
                hrs += ceil(p / mid)
        if hrs <= h:
            right = mid
        else:
            left = mid + 1
    return left


answer = minEatingSpeed(piles=[30, 11, 23, 4, 20], h=6)
print("answer is")
print(answer)
