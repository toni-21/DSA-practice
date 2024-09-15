def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key=lambda x: x[0])
    res = [intervals[0]]

    for i in range(1, len(intervals)):
        # check the current interval if is within the previously stacked interval and update it of so
        if intervals[i][0] >= res[-1][0] and intervals[i][0] <= res[-1][1]:
            temp = res.pop()
            res.append([temp[0], max(temp[1], intervals[i][1])])
        else:
            res.append(intervals[i])

    return res


answer = merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]])
print("answer is", answer)
