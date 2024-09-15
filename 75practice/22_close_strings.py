from collections import Counter


def closeStrings(word1: str, word2: str) -> bool:
    cnt1 = Counter(word1)
    cnt2 = Counter(word2)

    return cnt1.keys() == cnt2.keys() and sorted(cnt1.values()) == sorted(cnt2.values())


answer = closeStrings(word1="cabbba", word2="abbccc")
print("answer is:")
print(answer)
