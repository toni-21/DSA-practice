def check(s: str, l: int, r: int) -> int:
    count = 0
    while l >= 0 and r < len(s) and s[l] == s[r]:
        count += 1
        l -= 1
        r += 1

    return count


def countSubstrings(s: str) -> int:
    res = 0
    for i in range(len(s)):
        res += check(s, i, i)
        res += check(s, i, i + 1)

    return res


answer = countSubstrings(s="abc")
print("answer is", answer)
