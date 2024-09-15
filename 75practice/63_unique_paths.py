import math


def uniquePaths(m: int, n: int) -> int:
    return math.comb(m + n - 2, n - 1)


answer = uniquePaths(m=3, n=7)
print("answer is")
print(answer)
