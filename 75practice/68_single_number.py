def singleNumber(nums: int) -> int:
    curr = 0
    for num in nums:
        curr ^= num
    return curr


answer = singleNumber(nums=[4, 1, 2, 1, 2])
print("answer is")
print(answer)
