# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True

    if not p or not q:
        return False

    if p.val == q.val:
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

    return False


answer = isSameTree(p=TreeNode(1, 2, 3), q=TreeNode(1, 2, 3))
print("answer is", answer)
