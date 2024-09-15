def findMinArrowShots(points: list[list[int]]) -> int:
    points.sort(key=lambda x: x[1])
    count, prevEnd = 1, points[0][1]

    for start, end in points[1:]:
        if start > prevEnd:
            count += 1
            prevEnd = end

    return count


answer = findMinArrowShots(points=[[10, 16], [2, 8], [1, 6], [7, 12]])
print("answer is")
print(answer)
