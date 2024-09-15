from collections import deque


def orangesRotting(grid: list[list[int]]) -> int:
    q = deque()
    l = len(grid)
    b = len(grid[0])
    sP = []
    count = 0
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    for i in range(l):
        for j in range(b):
            if grid[i][j] == 2:
                sP.append([i,j,0])
    if len(sP) > 0:
        q.extend(sP)
    
    while q:
        row, col, h = q.popleft()

        count = max(count, h)

        for dir in directions:
            r, c = row + dir[0], col + dir[1]
            if r < 0 or c < 0 or r == l or c == b or grid[r][c] == 0:
                continue
            else:
                if grid[r][c] == 1:
                    q.append([r, c, h + 1])
                    grid[r][c] = 2

    for i in range(l):
        for j in range(b):
            if grid[i][j] == 1:
                return -1
    
    return count


answer = orangesRotting(grid=[[2, 1, 1], [1, 1, 0], [0, 1, 1]])
print("answer is")
print(answer)
