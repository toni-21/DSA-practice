def eraseOverlapIntervals(intervals: list[list[int]]) -> int:
    intervals.sort(key=lambda x: x[1])
    count, prevEnd = 0, intervals[0][1]

    for start, end in intervals[1:]:
        if start < prevEnd:
            count += 1
        else:
            prevEnd = end
    return count


answer = eraseOverlapIntervals(intervals=[[1, 100], [11, 22], [1, 11], [2, 12]])
print("answer is")
print(answer)
