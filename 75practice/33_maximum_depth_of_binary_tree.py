from utils import TreeNode, populateNode
from typing import Optional


def maxDepth(head: Optional[TreeNode]) -> Optional[TreeNode]:
    # recursive
    # if not head:
    #     return 0
    # return 1 + max(maxDepth(head.left), maxDepth(head.right))

    # dfs
    res = 0
    stack = [(head, 1)]
    while stack:
        root, depth = stack.pop()
        if root:
            res = max(res, depth)
            stack.append((root.left, depth + 1))
            stack.append((root.right, depth + 1))

    return res


answer = maxDepth(head=[3, 9, 20, None, None, 15, 7])
print("answer is")
print(answer)
