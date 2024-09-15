from typing import Optional


def reverseBetween(head: Optional[ListNode], left: int, right: int):  # type: ignore
    if not head or not head.next:
        return head

    dummy = ListNode(0, head)  # type: ignore
    prev = dummy

    for _ in range(left - 1):
        # traverse till just before left marker
        prev = prev.next

    curr = prev.next
    for _ in range(right - left):
        # pop the temp value to be removed from curr list
        temp = curr.next
        curr.next = temp.next
        # slot the removed value right revesal begins
        temp.next = prev.next
        prev.next = temp

    return dummy.next


answer = reverseBetween(head=[1, 2, 3, 4, 5], left=2, right=4)
print("answer is", answer)
