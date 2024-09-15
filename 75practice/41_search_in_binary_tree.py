from utils import TreeNode
from typing import Optional


def searchBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    # recursive
    # if not root:
    #     return None

    # if val == root.val:
    #     return root
    # elif val < root.val:
    #     return searchBST(root.left, val)
    # elif val > root.val:
    #     return searchBST(root.right, val)

    # iterative
    stack, res = [root], None
    while stack:
        node = stack.pop()
        if node.val == val:
            res = node
            break
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res
re = {}


answer = searchBST(root=[4, 2, 7, 1, 3], val=2)
print("answer is")
print(answer)
