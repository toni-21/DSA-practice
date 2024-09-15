from collections import Counter


def uniqueOccurrences(arr: list[int]) -> bool:
    s = set()
    count = Counter(arr)
    for i in count.keys():
        if count[i] in s:
            return False
        s.add(count[i])
    return True


answer = uniqueOccurrences(arr=[-3, 0, 1, -3, 1, 1, 1, -3, 10, 0])
print("answer is:")
print(answer)
