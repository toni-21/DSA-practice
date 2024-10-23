# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowestCommonAncestor(
    root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]
) -> Optional[TreeNode]:
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root
    return


node = TreeNode()
answer = lowestCommonAncestor(root=node, p=node, q=node)
print("answer is", answer)
