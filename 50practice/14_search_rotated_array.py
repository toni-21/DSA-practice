def search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = right + left // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] >= nums[left]:
            # left part is sorted
            if target >= nums[left] and target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            #right part is sorted
            if target > nums[mid] and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


answer = search(nums=[4, 5, 6, 7, 0, 1, 2], target=0)
print("answer is", answer)
