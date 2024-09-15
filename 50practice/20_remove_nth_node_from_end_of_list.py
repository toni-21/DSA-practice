from typing import Optional


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:  # type: ignore
    dummy = ListNode(0, head)  # type: ignore
    fast, slow = dummy, dummy

    for _ in range(n + 1):
        fast += fast.next

    while fast:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next

    return dummy.next


answer = removeNthFromEnd(head=[1, 2, 3, 4, 5], n=4)
print("answer is", answer)
