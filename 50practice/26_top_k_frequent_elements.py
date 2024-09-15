from collections import Counter, defaultdict
import heapq


def topKFrequent(nums: list[int], k: int) -> list[int]:
    # return [i[0] for i in Counter(nums).most_common(k)]
    counter = defaultdict(int)
    heap = []
    res = []

    for n in nums:
        counter[n] += 1

    for key, val in counter.items():
        heapq.heappush(heap, (-val, key))

    for _ in range(k):
        res.append(heapq.heappop(heap)[1])

    return res


answer = topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2)
print("answer is", answer)
