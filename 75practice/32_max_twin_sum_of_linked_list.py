from utils import ListNode, populateNode
from typing import Optional


def pairSum(head: Optional[ListNode]) -> Optional[ListNode]:
    maxSum = 0
    if not head or not head.next:
        return head

    # get the middle point
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse the second part of the linked list
    prev, curr = None, slow
    while curr:
        curr.next, prev, curr = prev, curr, curr.next

    # get the max sum of the value[index] at both sides
    while prev:
        maxSum = max(maxSum, prev.val + head.val)
        prev = prev.next
        head = head.next

    return maxSum


input = populateNode(nodes=[5, 4, 2, 1])
answer = pairSum(head=input)
print("answer is")
print(answer)
