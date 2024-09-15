def reverseWords(s: str) -> str:
    wrdLst = s.strip().split()
    return " ".join(wrdLst[::-1])


answer = reverseWords(s="a good   example")
print("answer is:")
print(answer)
