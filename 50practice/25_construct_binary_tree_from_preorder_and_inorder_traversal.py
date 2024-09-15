# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def printTree(root: TreeNode) -> str:
    def traverse(root: Optional[TreeNode], res: list[int]):
        if not root:
            # res.append(None)
            return

        print("val is", root.val)
        res.append(root.val)
        traverse(root.left, res)
        traverse(root.right, res)

        return str(res)

    return traverse(root, [])


def buildTree(preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
    # create inorder map
    inorder_map = {val: idx for idx, val in enumerate(inorder)}
    preorder_idx = 0

    def build(left, right):
        if left > right:
            return None
        nonlocal preorder_idx
        # get the position of the current node in preorder list and shift the tracking index
        node_val = preorder[preorder_idx]
        root = TreeNode(node_val)
        preorder_idx += 1

        # build a left subtree at the node by looking left from the its position in the inorder list
        # and repeat for right subtree
        inorder_idx = inorder_map[node_val]
        root.left = build(left, inorder_idx - 1)
        root.right = build(inorder_idx + 1, right)

        return root

    return build(0, len(inorder) - 1)


tree_res = buildTree(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7])
answer = printTree(tree_res)
print("answer is", answer)
