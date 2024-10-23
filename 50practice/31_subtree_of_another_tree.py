# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSametree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    if not root and not subRoot:
        return True

    if not root or not subRoot:
        return False

    return (
        root.val == subRoot.val
        and isSametree(root.left, subRoot.left)
        and isSametree(root.right, subRoot.right)
    )


def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    if not root:
        return False

    if isSametree(root, subRoot):
        return True

    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)


node = TreeNode()
answer = isSubtree(root=node, subRoot=node)
print("answer is", answer)
