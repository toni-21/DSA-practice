def minDistance(word1: str, word2: str) -> int:
    dp = [[float("inf") for j in range(len(word2) + 1)] for i in range(len(word1) + 1)]

    for j in range(len(word2) + 1):
        dp[len(word1)][j] = len(word2) - j
    for i in range(len(word1) + 1):
        dp[i][len(word2)] = len(word1) - i

    for i in range(len(word1) - 1, -1, -1):
        for j in range(len(word2) - 1, -1, -1):
            if word1[i] == word2[j]:
                dp[i][j] = dp[i + 1][j + 1]
            else:
                dp[i][j] = 1 + min(dp[i + 1][j + 1], dp[i + 1][j], dp[i][j + 1])
                # where [i+1][j] -> delete
                # where [i][j+1] -> insert
                # where [i+1][j+1] -> replace

    return dp[0][0]


answer = minDistance(word1="horse", word2="ros")
print("answer is")
print(answer)
