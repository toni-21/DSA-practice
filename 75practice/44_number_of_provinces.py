def findCircleNum(isConnected: list[list[int]]) -> int:
    visited = set()
    provinces = 0
    n = len(isConnected)

    def dfs(i):
        visited.add(i)
        for j in range(n):
            if j not in visited and isConnected[i][j] == 1:
                visited.add(j)
                dfs(j)

    for i in range(n):
        if i not in visited:
            dfs(i)
            provinces += 1
    return provinces


answer = findCircleNum(isConnected=[[1,0,0],[0,1,0],[0,0,1]])
print("answer is")
print(answer)
