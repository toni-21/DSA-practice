def findMaxAverage(nums: list[int], k: int):
    max_sum = curr_sum = sum(nums[:k])

    for i in range(k, len(nums)):
        curr_sum += nums[i] - nums[i - k]
        max_sum = max(curr_sum, max_sum)
    return max_sum/k


answer = findMaxAverage([1,12,-5,-6,50,3], 4)
print("answer is:")
print(answer)