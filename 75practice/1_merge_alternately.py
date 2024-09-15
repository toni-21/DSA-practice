def mergeAlternately(word1: str, word2: str) -> str:
    i = 0
    res = ""
    len1 = len(word1)
    len2 = len(word2)
    while i < len1:
        res += word1[i]
        if i < len2:
            res += word2[i]
        i += 1
    else:
        if i < len2:
            res += word2[i:]
    return res


answer = mergeAlternately(word1="abcd", word2="pq")
print("answer is", answer)
