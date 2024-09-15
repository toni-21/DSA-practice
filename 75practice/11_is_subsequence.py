def isSubsequence(s: str, t: str) -> bool:
    s_len = len(s)
    if s_len == 0:
        return True
    
    t_len = len(t)
    j = 0
    for i in range(t_len):
        if t[i] == s[j]:
            j += 1
            if j == s_len:
                return True

    return False


answer = isSubsequence(s="abc", t="cadnfvnbndfcnf")
print("answer is:")
print(answer)
