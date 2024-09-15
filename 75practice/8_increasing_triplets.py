def increasingTriplet(nums: list[int]) -> bool:
    first  = second = float('inf')
    for num in nums:
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            return True
    return False

answer = increasingTriplet(nums=[9,9,9,4,5])
print("answer is:")
print(answer)