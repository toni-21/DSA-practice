def combinationSum3(k: int, n: int) -> list[list[int]]:
    num_list = [(i + 1) for i in range(9)]
    res = []

    def backtrack(i, sub):
        if sum(sub) == n:
            if len(sub) == k:
                res.append(sub)
            return
        for num in num_list[i:]:
            if sub and num < sub[-1]:
                continue
            if num not in sub:
                backtrack(i + 1, sub + [num])

    backtrack(0, [])
    return res


answer = combinationSum3(k=3, n=15)
print("answer is")
print(answer)
