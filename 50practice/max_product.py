def maxProduct(nums: list[int]) -> int:
    n = len(nums)
    left_prod, right_prod = 1, 1
    max_prod = nums[0]

    for i in range(n):
        j = n - i - 1
        #calculate the max array prod from the left side
        left_prod *= nums[i]
        max_prod = max(left_prod, max_prod)
        if left_prod == 0:
            left_prod = 1
        #and also from the right to atone and compare at each interval
        right_prod *= nums[j]
        max_prod = max(right_prod, max_prod)
        if right_prod == 0:
            right_prod = 1

    return max_prod


answer = maxProduct(nums=[-8, 5, 3, 1, 6])
print("answer is", answer)
