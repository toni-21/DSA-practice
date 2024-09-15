from utils import TreeNode
from typing import Optional
from collections import deque


def maxLevelSum(root: Optional[TreeNode]) -> int:
    if not root:
        return []

    temp = []
    level = 0
    maxLevel = 0
    maxSum = float("-inf")

    q = deque()
    q.append(root)
    q.append(None)

    while q:
        node = q.popleft()
        if node == None:
            # if you change level, append the last temp value to result
            level += 1
            q.append(None)

            #update maxlevel based on tempSum
            tempSum = sum(temp)
            if tempSum > maxSum:
                maxSum = tempSum
                maxLevel = level

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

    return maxLevel


answer = maxLevelSum(root=[1, 2, 3, None, 5, None, 4])
print("answer is")
print(answer)
