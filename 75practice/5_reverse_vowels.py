def reverseVowels(s: str) -> str:
    s = list(s)
    low = 0
    high = len(s)-1
    vowels = set("aeiouAEIOU")
    while low < high:
        while low < high and s[low] not in vowels:
            low += 1
        while low < high and s[high] not in vowels:
            high -= 1
        s[low], s[high] = s[high], s[low]
        low += 1
        high -= 1
    return "".join(s)


answer = reverseVowels(s="hello")
print("answer is", answer)
