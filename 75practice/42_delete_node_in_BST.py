from utils import TreeNode
from typing import Optional


def deleteNode(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    if not root:
        return root
    if key == root.val:
        if not root.left or not root.right:
            return root.left if not root.right else root.right
        if root.left and root.right:
            temp = root.right
            while temp.left:
                temp = temp.left
            root.val = temp.val
            root.right = deleteNode(root.right, temp.val)
    elif key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    return root


answer = deleteNode(root=[5, 3, 6, 2, 4, None, 7], key=3)
print("answer is")
print(answer)
