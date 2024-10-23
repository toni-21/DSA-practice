# Definition for a binary tree node.
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(new_node: Optional["Node"]) -> Optional["Node"]:
    visited = {}

    def dfs(node):
        if not node:
            return node

        if node in visited:
            return visited[node]

        clone_node = Node(node.val, [])
        visited[node] = clone_node

        if node.neighbors:
            clone_node.neighbors = [dfs(n) for n in node.neighbors]

        return clone_node

    return dfs(new_node)


answer = cloneGraph()
print("answer is", answer)
