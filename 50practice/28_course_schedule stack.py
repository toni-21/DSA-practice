from collections import deque


def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    adj = [[] for _ in numCourses]
    org = [0] * numCourses

    for pre in prerequisites:
        adj[pre[1]].append(pre[0])
        org[pre[0]] += 1

    queue = deque()
    nodesVisited = 0

    for i in range(numCourses):
        if org[i] == 0:
            queue.append(i)

    while queue:
        neighbours = adj[queue.popleft()]
        nodesVisited += 1

        for n in neighbours:
            org[n] -= 1
            if org[n] == 0:
                queue.append(n)

    return nodesVisited == numCourses


answer = canFinish(numCourses=2, prerequisites=[[1, 0]])
print("answer is", answer)
