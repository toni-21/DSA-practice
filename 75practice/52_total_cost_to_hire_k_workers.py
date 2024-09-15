from heapq import heapify, heappop, heappush

def totalCost(costs: list[int], k: int, candidates: int) -> int:
    firstPart = costs[:candidates]
    lastPart = costs[max(candidates, len(costs) - candidates) :]
    heapify(firstPart)
    heapify(lastPart)

    res = 0
    i, j = candidates, len(costs) - candidates - 1

    for _ in range(k):
        if not lastPart or (firstPart and firstPart[0] <= lastPart[0]):
            res += heappop(firstPart)
            if i <= j:
                # Only refill the queue if there are workers outside the two queues.
                heappush(firstPart, costs[i])
                i += 1
        else:
            res += heappop(lastPart)
            if i <= j:
                heappush(lastPart, costs[j])
                j -= 1
    return res


answer = totalCost(
    costs=[31, 25, 72, 79, 74, 65, 84, 91, 18, 59, 27, 9, 81, 33, 17, 58],
    k=11,
    candidates=2,
)
print("answer is")
print(answer)
