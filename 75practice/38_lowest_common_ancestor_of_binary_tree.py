from utils import TreeNode
from typing import Optional


def lowestCommonAncestor(root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
    if root in(None, p, q):
        return root
    
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right,p,q)
    
    if left and right:
        return root
    if not left and not right:
        return None
    return left or right


answer = lowestCommonAncestor(root=[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
print("answer is")
print(answer)
