def removeStars(s: str) -> str:
    stack = []
    for char in s:
        if char != '*':
            stack.append(char)
        else:
            stack.pop()
    return ''.join(stack)

answer = removeStars(s="leet**cod*e")
print("answer is:")
print(answer)
