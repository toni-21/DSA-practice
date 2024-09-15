def containsDuplicate(nums: list[int]) -> bool:
    seen = {}
    for num in nums:
        if num in seen:
            return True
        else:
            seen[num] = 1

    return False


answer = containsDuplicate(nums=[1, 2, 3, 1])
print("answer is", answer)
