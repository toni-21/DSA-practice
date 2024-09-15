def maxVowels(s: str, k: int) -> int:
    vowels = set('aeiouAEIOU')
    curr_count = 0
    max_count = 0

    for i in range(k):
        if s[i] in vowels:
            curr_count += 1
    max_count = curr_count

    for i in range(k, len(s)):
        prev = s[i-k]
        curr = s[i]
        if prev in vowels:
            curr_count -= 1
        if curr in vowels:
            curr_count += 1
        max_count = max(curr_count, max_count)

    return max_count

answer = maxVowels(s='abciiidef', k=3)
print('answer is')
print(answer)