from utils import TreeNode, populateNode
from typing import Optional


def leafSimilar(r1: Optional[TreeNode], r2: Optional[TreeNode]) -> bool:
    if not r1 and not r2:
        return False
    res1 = []
    stack = [r1]
    while stack:
        node = stack.pop()
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
        if not node.right and not node.left:
            res1.append(node.val)

    res2 = []
    stack = [r2]
    while stack:
        node = stack.pop()
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
        if not node.right and not node.left:
            res2.append(node.val)

        return res1 == res2


answer = leafSimilar(head=[3, 9, 20, None, None, 15, 7])
print("answer is")
print(answer)
