from utils import TreeNode
from typing import Optional


def longestZigZag(root: Optional[TreeNode]) -> int:
    maxLen = 0

    def dfs(node, leftLen, rightLen):
        maxLen = max(maxLen, leftLen, rightLen)

        if node.left:
            dfs(node.left, rightLen + 1, 0)
        if node.right:
            dfs(node.right, 0, leftLen + 1)

    dfs(root, 0, 0)
    return maxLen


answer = longestZigZag(
    root=[1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1]
)
print("answer is")
print(answer)
