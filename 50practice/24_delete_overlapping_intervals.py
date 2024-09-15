def eraseOverlapIntervals(intervals: list[list[int]]) -> int:
    if len(intervals) <= 1:
        return 0

    intervals.sort(key=lambda x: x[1])
    count = 0
    prevEnd = intervals[0][1]

    for start, end in intervals[1:]:
        if start < prevEnd:
            count += 1
        else:
            prevEnd = end

    return count


answer = eraseOverlapIntervals(intervals=[[1, 2], [2, 3], [3, 4], [1, 3]])
print("answer is", answer)
