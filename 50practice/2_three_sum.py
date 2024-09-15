def threeSum(nums: list[int]) -> list[int]:
    n = len(nums)
    res = []
    nums.sort()

    for i, num in enumerate(nums):
        if i > 0 and num == nums[i - 1]:
            continue

        l, r = i + 1, n - 1
        while l < r:
            treeSum = num + nums[l] + nums[r]
            if treeSum < 0:
                l += 1
            elif treeSum > 0:
                r -= 1
            else:
                res.append([num, nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
    return res


answer = threeSum(nums=[-1,0,1,2,-1,-4])
print("answer is", answer)
