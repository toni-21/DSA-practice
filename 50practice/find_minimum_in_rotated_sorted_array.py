def findMin(nums: list[int]) -> int:
    n = len(nums)
    left, right = 0, n - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]


answer = findMin(nums=[3, 4, 5, 1, 2])
print("answer is", answer)
