from collections import deque


class TreeNode(object):
    def __init__(self, x) -> None:
        self.val = x
        self.left = None
        self.right = None

class Codec:
    # encode tree to string
    def serialize(self, root):
        def rserialize(root, result):
            if not root:
                return result + "None,"

            result += str(root.val) + ","
            result = rserialize(root.left, result)
            result = rserialize(root.right, result)
            return result

        return rserialize(root, "")

    # decodes string to tree
    def deserialize(self, data):
        def rdeserialize(treeList):
            if treeList[0] == "None":
                treeList.pop()
                return None
            node = TreeNode(treeList[0])
            treeList.pop(0)
            node.left = rdeserialize(treeList)
            node.right = rdeserialize(treeList)
            return node

        treeList = data.split(",")
        return rdeserialize(treeList)


ser = Codec()
deser = Codec()

ans = ser.serialize(deser.deserialize())
