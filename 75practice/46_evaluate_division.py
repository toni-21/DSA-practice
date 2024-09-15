from collections import defaultdict


def calcEquation(
    equations: list[list[str]], values: list[float], queries: list[list[str]]
) -> list[float]:
    store = defaultdict(dict)
    for (x, y), v in zip(equations, values):
        store[x][y] = v
        store[y][x] = 1 / v

    def bfs(src, dst):
        if src not in store or dst not in store:
            return -1
        query = [(src, 1)]
        seen = set()
        for x, v in query:
            if x == dst:
                return v
            seen.add(x)
            for y in store[x]:
                if y not in seen:
                    query.append((y, store[x][y]))
        return -1

    return [bfs(s, d) for (s, d) in queries]


answer = calcEquation(
    equations=[["a", "b"], ["b", "c"]],
    values=[2.0, 3.0],
    queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
)
print("answer is")
print(answer)
