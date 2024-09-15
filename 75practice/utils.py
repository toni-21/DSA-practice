# this file serves as a storage for commonly used classes
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.right = right
        self.left = left

    def insert(self, val):
        newNode = TreeNode(val)
        # check if no root and insert root first
        if not self.val:
            self.val = val
        else:
            curr = self
            while True:
                if val < curr.val:
                    # left
                    if not curr.left:
                        curr.left = newNode
                        return

                    curr = curr.left
                elif val > curr.val:
                    # right
                    if not curr.right:
                        curr.right = newNode
                        return

                    curr = curr.right


def populateNode(nodes: list) -> ListNode:
    if not nodes:
        return None

    head = ListNode(nodes[0])
    curr = head
    n = len(nodes)

    for i in range(1, n):
        curr.next = ListNode(nodes[i])
        curr = curr.next

    return head
