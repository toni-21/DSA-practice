def pacificAtlantic(heights: list[list[int]]) -> list[list[int]]:
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    rows, cols = len(heights), len(heights[0])
    pac, atl = set(), set()

    def traverse(row, col, ocean, prevHeight):
        if (
            row < 0
            or col < 0
            or row >= rows
            or col >= cols
            or (row, col) in ocean
            or heights[row][col] < prevHeight
        ):
            return
        ocean.add((row, col))
        for dir in directions:
            r, c = row + dir[0], col + dir[1]
            traverse(r, c, ocean, heights[row][col])

    for c in range(cols):
        traverse(0, c, pac, heights[0][c])
        traverse(rows - 1, c, atl, heights[rows - 1][c])

    for r in range(rows):
        traverse(r, 0, pac, heights[r][0])
        traverse(r, cols - 1, atl, heights[r][cols - 1])

    results = list[pac.intersection(atl)]

    return results


answer = pacificAtlantic(
    heights=[
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ]
)
print("answer is", answer)
