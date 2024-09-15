def numIslands(grid: list[list[str]]) -> int:
    if not grid:
        return 0

    visited = set()
    directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    l = len(grid)
    b = len(grid[0])
    count = 0

    def traverse(row, col):
        if (
            (row, col) in visited
            or row < 0
            or col < 0
            or row == l
            or col == b
            or grid[row][col] == "0"
        ):
            return
        visited.add((row, col))
        for dir in directions:
            r, c = row + dir[0], col + dir[1]
            traverse(r, c)

    for i in range(l):
        for j in range(b):
            if grid[i][j] == "1" and (i, j) not in visited:
                count += 1
                traverse(i, j)

    return count


answer = numIslands(
    grid=[
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
)
print("answer is:")
print(answer)
