from typing import Optional


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:  # type: ignore
    if not head or not head.next:
        return head
    prev, curr = None, head

    while curr:
        # curr.next, prev, curr = prev, curr, curr.next
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev


answer = reverseList(head=[1, 2, 3, 4, 5])
print("answer is", answer)
