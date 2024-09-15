import heapq


def findKthLargest(nums: list[int], k: int) -> int:
    k = len(nums) - k

    # heapq.heapify(nums)
    # for i in range(k):
    #     heapq.heappop(nums)
    # return heapq.heappop(nums)
    def quickSelect(l, r):
        p, pivot = l, nums[r]
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[i], nums[p] = nums[p], nums[i]
                p += 1
            nums[r], nums[p] = nums[p], nums[r]
            if k > p:
                return quickSelect(p + 1, r)
            elif k < p:
                return quickSelect(l, p - 1)
            else:
                return nums[k]

    return quickSelect(0, len(nums) - 1)


answer = findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2)
print("answer is")
print(answer)
