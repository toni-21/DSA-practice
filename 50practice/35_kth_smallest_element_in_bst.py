# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    array = []

    def dfs(node: TreeNode) -> None:
        if not node:
            return None

        dfs(node.left)
        array.append(node.val)
        dfs(node.right)

    dfs(root)
    return array[k - 1]


node = TreeNode(3)
node.left = TreeNode(1)
node.right = TreeNode(4)
node.left.right = TreeNode(2)
answer = kthSmallest(root=node, k=1)
print("answer is", answer)
