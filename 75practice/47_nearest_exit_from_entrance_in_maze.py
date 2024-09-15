from collections import deque


def nearestExit(maze: list[list[str]], entrance: list[int]) -> int:
    q = deque()
    q.append([entrance[0], entrance[1], 0])
    l = len(maze)
    b = len(maze[0])
    steps = float("inf")
    while q:
        row, col, h = q.popleft()

        if h != 0 and (row == 0 or col == 0 or row == l - 1 or col == b - 1):
            steps = min(steps, h)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for dir in directions:
            r, c = row + dir[0], col + dir[1]
            if r < 0 or c < 0 or r == l or c == b or maze[r][c] == "+":
                continue
            else:
                q.append([r, c, h + 1])
                maze[r][c] = "+"
    return steps if steps != float("inf") else -1


answer = nearestExit(
    maze=[["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]],
    entrance=[1, 2],
)
print("answer is")
print(answer)
