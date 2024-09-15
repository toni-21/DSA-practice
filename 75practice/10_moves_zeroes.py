def moveZeroes(nums: list[int]) -> list[int]:
   anchor = 0
   for i in range(len(nums)):
      if nums[i] != 0:
         nums[i], nums[anchor] = nums[anchor], nums[i]
         anchor += 1
   return nums

answer = moveZeroes(nums=[0,9,9,0,9,4,5,0])
print("answer is:")
print(answer)