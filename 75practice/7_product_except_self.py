def productExceptSelf(nums: list[int]) -> list[int]:
    n = len(nums)
    left = [1] * n  
    right = [1] * n
    answer = []

    # calculate left prefix product
    for i in range(1, n):
        left[i] = left[i - 1] * nums[i - 1]

    # calculate right sufix product
    for i in range(n - 2, -1, -1):
        right[i] = right[i + 1] * nums[i + 1]

    # calculate the result
    for i in range(n):
        answer.append(left[i] * right[i])
    return answer


answer = productExceptSelf(nums=[1, 2, 3, 4])
print("answer is:")
print(answer)
