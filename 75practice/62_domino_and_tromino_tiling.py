def numTilings(n: int) -> int:
    if n < 3:
        return n

    nums = [0] * (n + 1)
    nums[1] = 1
    nums[2] = 2
    nums[3] = 5

    for i in range(4, n + 1):
        nums[i] = (2 * nums[i - 1] + nums[i - 3]) % (10**9 + 7)

    return nums[n]


answer = numTilings(n=4)  # 11
print("answer is")
print(answer)
