from collections import defaultdict


def equalPairs(grid: list[list[int]]) -> int:
    d = defaultdict(int)
    sum = 0
    for row in grid:
        d[tuple(row)] += 1

    transp = zip(*grid)
    for col in transp:
        sum += d[tuple(col)]

    return sum


answer = equalPairs(grid=[[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]])
print("answer is:")
print(answer)
