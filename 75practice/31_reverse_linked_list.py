from utils import ListNode, populateNode
from typing import Optional


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    # using stacks
    # stack = []
    # curr = head
    # while curr:
    #     stack.append(curr.val)
    #     curr = curr.next

    # reversedList = ListNode()
    # curr = reversedList
    # while stack:
    #     curr.next = ListNode(stack.pop())
    #     curr = curr.next
    # return reversedList.next.val

    #using in-place method
    prev = None
    curr = head

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    head = prev
    return head.val



input = populateNode(nodes=[2, 1, 3, 5, 6, 4, 7])
answer = reverseList(head=input)
print("answer is")
print(answer)
