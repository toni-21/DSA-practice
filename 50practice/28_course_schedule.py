from collections import deque


def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    # indicates all the destinations (mainCourses) for each node (precourse)
    adjacents = [[] for _ in range(numCourses)]
    # indicates how many origin nodes are pointing to this node as its main course
    # absence of any origin node indicates that the node is a leaf node
    origins = [0] * numCourses

    for pre in prerequisites:
        # add all the detinations that lead out from a precourse in the precourse's adj list
        adjacents[pre[1]].append(pre[0])
        # increase the number of origins pointing to the maincourse node
        origins[pre[0]] += 1

    queue = deque()
    for i in range(numCourses):
        # add node to queue if it is a leaf node
        if origins[i] == 0:
            queue.append(i)

    nodesVisited = 0
    # bfs traversal
    while queue:
        # get all the origins that the node is connected to and mark node as visited
        neighbours = adjacents[queue.popleft()]
        nodesVisited += 1

        for n in neighbours:
            # remove connection from this origin
            origins[n] -= 1
            # if the origin is a leaf node, append to queue
            if origins[n] == 0:
                queue.append(n)

    return nodesVisited == numCourses


answer = canFinish(numCourses=2, prerequisites=[[1, 0]])
print("answer is", answer)
