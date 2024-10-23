# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxPathSum(root: Optional[TreeNode]) -> bool:
    maxSum = float("-inf")

    def dfs(root: Optional[TreeNode]):
        nonlocal maxSum
        if not root:
            return 0

        leftSum = max(dfs(root.left), 0)
        rightSum = max(dfs(root.right), 0)

        currSum = root.val + leftSum + rightSum
        maxSum = max(currSum, maxSum)
        return root.val + max(leftSum, rightSum)

    dfs(root)
    return maxSum


node = TreeNode()
answer = maxPathSum(root=node)
print("answer is", answer)
