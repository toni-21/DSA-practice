from utils import TreeNode, populateNode
from typing import Optional
from collections import defaultdict


def pathSum(root: Optional[TreeNode], targetSum: int) -> int:
    lookup = defaultdict(int)
    lookup[0] = 1

    def dfs(node, currSum) -> int:
        if not node:
            return 0

        currSum += node.val
        count = lookup[currSum - targetSum]

        lookup[currSum] += 1
        count += dfs(node.left, currSum) + dfs(node.right, currSum)
        lookup[currSum] -= 1
        return count

    return dfs(root, 0)


answer = pathSum(root=[10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], targetSum=8)
print("answer is")
print(answer)
