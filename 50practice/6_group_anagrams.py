from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    groups = defaultdict(list)

    for s in strs:
        key = "".join(sorted(s))
        groups[key].append(s)

    return list(groups.values())


answer = groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"])
print("answer is", answer)