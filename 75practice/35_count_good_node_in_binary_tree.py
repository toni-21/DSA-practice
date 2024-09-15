from utils import TreeNode, populateNode
from typing import Optional


def goodNodes(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return 0
    count = 0
    stack = [(root)]
    while stack:
        node, currMax = stack.pop()
        count += 1 if node.val >= currMax else 0
        if node.left:
            stack.append((node, max(node.left.val, currMax)))
        if node.right:
            stack.append((node, max(node.right.val, currMax)))
    return count


answer = goodNodes(head=[3, 9, 20, None, None, 15, 7])
print("answer is")
print(answer)
