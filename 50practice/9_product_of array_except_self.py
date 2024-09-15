def productExceptSelf(nums: list[int]) -> list[int]:
    n = len(nums)
    left = 1
    right = 1
    answer = [1] * n

    #left prefix sum
    for i in range(n):
        answer[i] *= left
        left *= nums[i]
        
    #right suffix sum
    for i in range(n - 1, -1, -1):
        answer[i] += right
        right *= nums[i]

    return answer


answer = productExceptSelf(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4])
print("answer is", answer)
