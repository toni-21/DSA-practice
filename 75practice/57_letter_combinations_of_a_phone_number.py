def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    res = []
    n = len(digits)
    letter_map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def backtrack(i, comb):
        if i == n:
            res.append(comb)
            return 

        for letter in letter_map[digits[i]]:
            backtrack(i + 1, comb + letter)

    backtrack(0, "")
    return res


answer = letterCombinations(digits="23")
print("answer is")
print(answer)
