from collections import defaultdict


def characterReplacement(s: str, k: int) -> int:
    l, maxLen, maxFreq = 0, 0, 0
    freq = defaultdict(int)

    for r in range(len(s)):
        freq[s[r]] += 1
        maxFreq = max(maxFreq, freq[s[r]])

  
        if (r - l + 1 - maxFreq) > k:
            freq[s[l]] -= 1
            l += 1

        maxLen = max(maxLen, r - l + 1)

    return maxLen


answer = characterReplacement(s="AABABBA", k=1)
print("answer is", answer)
