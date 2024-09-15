def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:  # type: ignore
    if not root:
        return root

    root.left, root.right = root.right, root.left

    invertTree(root.left)
    invertTree(root.right)

    return root


answer = invertTree(root=[])
print("answer is", answer)
