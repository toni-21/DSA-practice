def findPeakElement(nums: list[int]) -> int:
    n = len(nums)
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        print(mid)
        if (mid == 0 or nums[mid] >= nums[mid - 1]) and (
            mid == n - 1 or nums[mid] >= nums[mid + 1]
        ):
            return mid
        elif nums[mid] <= nums[mid + 1]:
            left = mid + 1
        else:
            right = mid - 1
    return -1


answer = findPeakElement(nums=[1, 2, 1, 3, 5, 6, 4])
print("answer is")
print(answer)
