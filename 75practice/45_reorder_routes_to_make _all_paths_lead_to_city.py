from collections import defaultdict


def minReorder(n: int, connections: list[list[int]]) -> int:
    links = defaultdict(list)
    r_links = defaultdict(list)
    outskirts = set()
    seen = set()
    seen.add(0)
    for connection in connections:
        if connection[1] == 0:
            outskirts.add(connection[0])
            seen.add(connection[0])
        if connection[0] == 0:
            outskirts.add(0)
        links[connection[0]].append(connection[1])
        links[connection[0]].append(connection[1])

    count = 0
    while len(outskirts) > 0:
        new_outskirts = set()
        for number in outskirts:
            for n in links[number]:
                if n in seen:
                    continue
                seen.add(n)
                new_outskirts.add(n)
                count += 1
            for n in r_links[number]:
                if n in seen:
                    continue
                seen.add(n)
                new_outskirts.add(n)
        outskirts = new_outskirts

    return count


answer = minReorder(n=5,connections=[[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]])
print("answer is")
print(answer)
