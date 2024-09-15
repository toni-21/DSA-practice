from utils import TreeNode
from typing import Optional
from collections import deque


def rightSideView(root: Optional[TreeNode]) -> list[int]:
    if not root:
        return []

    temp = []
    res = []
    q = deque()
    q.append(root)
    q.append(None)

    while q:
        node = q.popleft()
        if node == None:
            #if you change level, append the last temp value to result
            res.append(temp[-1])
            q.append(None)
            if q[0] == None:
                break
            else:
                continue
        else:
            #create a list of non-null values
            temp.append(node.val)

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    return res


answer = rightSideView(root=[1, 2, 3, None, 5, None, 4])
print("answer is")
print(answer)
