from utils import TreeNode
from typing import Optional
from collections import deque


def levelOrder(root: Optional[TreeNode]) -> int:
    if not root:
        return []

    temp = []
    res = []
    q = deque()
    q.extend([root, None])

    while q:
        node = q.popleft()
        if not node:
            # if you change level, append the last temp value to result
            q.append(None)
            res.append(list(temp))

            if q[0] == None:
                break
            else:
                temp.clear()
                continue
        else:
            # create a list of non-null values
            temp.append(node.val)

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    return res


answer = levelOrder(root=[1, 2, 3, None, 5, None, 4])
print("answer is")
print(answer)
