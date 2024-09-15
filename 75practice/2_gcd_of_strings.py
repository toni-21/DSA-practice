import math


def gcdOfStrings(str1: str, str2: str) -> str:
    # check the concatenation of the 2 strings is cummutative in nature
    if str1 + str2 != str2 + str1:
        return ""
    # return a substring of length equal to the highest common factor of the length of both strings 
    return str1[:math.gcd(len(str1),len(str2))]


answer = gcdOfStrings(str1="ABABAB", str2="ABAB")
print("answer is", answer)
