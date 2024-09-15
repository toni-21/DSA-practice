from math import ceil

pick = 6


def guess(num: int) -> int:
    if num == pick:
        return 0
    elif num < pick:
        return 1
    else:
        return -1


def guessNumber(n: int) -> int:
    left, right = 0, n
    while left <= right:
        mid = ceil((left + right) / 2)
        g = guess(mid)
        if g == 0:
            return mid
        elif g == 1:
            left = mid
        else:
            right = mid
    return -1


answer = guessNumber(n=10)
print("answer is")
print(answer)
print(bool(7%7) + 1)
