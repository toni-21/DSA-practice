def dailyTemperatures(temperatures: list[int]) -> list[int]:
    res = [0 for _ in temperatures]
    stack = []

    for i in range(len(temperatures)):
        temp = temperatures[i]

        while stack and temp > stack[-1][0]:
            (tmp, ind) = stack.pop()
            res[ind] = i - ind
        stack.append((temp, i))
        
    return res


answer = dailyTemperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 73])
print("answer is")
print(answer)
