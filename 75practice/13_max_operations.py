def maxOperations(nums: list[int], k: int) -> int:
    max_count = 0
    i = 0
    j = len(nums)-1
    nums.sort()

    while i < j:
        curr_sum = nums[i] + nums[j]
        if curr_sum == k:
            max_count += 1
            i += 1
            j -= 1
        elif curr_sum < k:
            i += 1
        else:
            j -= 1
    return max_count


answer = maxOperations([1, 8, 6, 2, 5, 4, 8, 3, 7], 5)
print("answer is:")
print(answer)