def deleteGreatestValue(grid: list[list[int]]) -> int:
    rowsSorted = map(sorted, grid)
    trnsp = zip(*rowsSorted)

    return sum(map(max, trnsp))


answer = deleteGreatestValue(grid=[[1, 2, 4], [3, 3, 1]])
print("answer is:")
print(answer)
