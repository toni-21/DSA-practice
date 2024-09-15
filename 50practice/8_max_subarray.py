def maxSubArray(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0
    curr_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        #curr_sum represents  the sum for a comtinuos array
        curr_sum = max(nums[i], nums[i]+curr_sum)
        max_sum = max(curr_sum, max_sum)
    
    return max_sum


answer = maxSubArray(nums=[-2,1,-3,4,-1,2,1,-5,4])
print("answer is", answer)
