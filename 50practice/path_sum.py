# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    def dfs(root, currSum):
        if not root:
            return False

        newSum = root.val + currSum
        if not root.left and not root.right:
            if newSum == targetSum:
                return True
            else:
                return False
        return dfs(root.left, newSum) or dfs(root.right, newSum)

    return dfs(root, 0)


answer = hasPathSum(root=TreeNode(), targetSum=22)
print("answer is", answer)
