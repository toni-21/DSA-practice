def numIslands(grid: list[list[str]]) -> int:
    if not grid:
        return 0

    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    count = 0
    seen = set()

    def traverse(i, j):
        if (
            i < 0
            or j < 0
            or i >= len(grid)
            or j >= len(grid[0])
            or (i, j) in seen
            or grid[i][j] == "0"
        ):
            return
        else:
            seen.add((i, j))
        for d in directions:
            r, c = i + d[0], j + d[1]
            traverse(r, c)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) not in seen and grid[i][j] != "0":
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
print("answer is", answer)
