from typing import Optional


def hasCycle(head: Optional[ListNode]) -> Optional[ListNode]:  # type: ignore
    fast = head
    while fast and fast.next:
        head = head.next
        fast = fast.next.next
        if head is fast:
            return True
        
    return False


answer = hasCycle(head=[1, 2, 3, 4, 5])
print("answer is", answer)
