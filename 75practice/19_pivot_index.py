def pivotIndex(nums: list[int]) -> int:
    total = sum(nums)
    count = 0

    for i in range(len(nums)):
        count += nums[i]
        if count == total:
            return i
        else:
            total -= 1

    return -1


answer = pivotIndex(nums=[2, 1, -1])
print("answer is:")
print(answer)
