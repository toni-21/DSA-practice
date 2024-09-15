def twoSum(nums: list[int], target: int) -> list[int]:
    store = {}
    for i, num in enumerate(nums):
        if num in store:
            return [store[num], i]
        else:
            store[target - num] = i
    return []

answer = twoSum(nums=[2, 7, 11, 15], target=9)
print("answer is", answer)
