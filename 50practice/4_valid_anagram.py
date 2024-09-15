from collections import defaultdict

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    store  = defaultdict(int)

    for letter in s:
        store[letter] += 1
    for letter in t:
        if letter in store and store[letter] != 0:
            store[letter] -= 1
        else:
            return False
    
    return True


answer = isAnagram(s="rat", t="tar")
print("answer is", answer)