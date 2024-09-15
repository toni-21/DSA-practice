def longestOnes(nums: list[int], k: int) -> bool:
    left = 0
    right = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            k -= 1
        if k < 0:
            if nums[left] == 0:
                k += 1
            left += 1
        print ('value is',nums[right],'left is', left, 'right is', right, 'k is', k, 'window is', right - left+1)
    return right - left


answer = longestOnes(nums=[1,1,1], k=1)
print("answer is:")
print(answer)
