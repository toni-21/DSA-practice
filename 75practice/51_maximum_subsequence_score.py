import heapq


def maxScore(nums1: list[int], nums2: list[int], k: int) -> int:
    n1Sum = 0
    heap = []
    res = 0
    pairs = [(n1, n2) for n1, n2 in zip(nums1, nums2)]
    pairs = sorted(pairs, key=lambda p: p[1], reverse=True)

    for n1, n2 in pairs:
        n1Sum += n1
        heapq.heappush(heap, n1)

        if len(heap) > k:
            nPop = heapq.heappop(heap)
            n1Sum -= nPop
        if len(heap) == k:
            res = max(res, n1Sum * n2)

    return res


answer = maxScore(nums1=[1, 3, 3, 2], k=3, nums2=[2, 1, 3, 4])
print("answer is")
print(answer)
