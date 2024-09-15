def rob(nums: list[int]) -> int:
    prev, curr = 0, 0

    for n in nums:
        curr, prev = max(prev + n, curr), curr

    return curr


answer = rob(nums=[2, 7, 9, 3, 1])
print("answer is")
print(answer)
