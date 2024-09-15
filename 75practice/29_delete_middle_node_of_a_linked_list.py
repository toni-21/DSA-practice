from utils import ListNode, populateNode
from typing import Optional


def deleteMiddle(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    prev = ListNode(0, head)
    slow = fast = head
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    prev.next = slow.next
    return head.val


input = populateNode(nodes=[1, 3, 4, 7, 1, 2, 6])
answer = deleteMiddle(head=input)
print("answer is")
print(answer)
