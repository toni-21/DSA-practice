def decodeString(s: str) -> str:
    stack = []
    k = 0
    curr = ""

    for char in s:
        if char == "[":
            stack.append((curr, k))
            curr, k = "", 0
        elif char == "]":
            words, n = stack.pop()
            curr = words + (n * curr)
        elif char.isdigit():
            k = (k * 10) + int(char)
        else:
            curr += char
    return curr


answer = decodeString(s="3[a2[c]]")
print("answer is:")
print(answer)
