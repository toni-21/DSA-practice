from utils import ListNode, populateNode
from typing import Optional


def oddEvenList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    odd = head #pointer to first odd node
    even = head.next #pointer to first even node
    even_head = even #pointer to the head of the even nodes

    while even and even.next:
        #connect the next odd node with the current odd node
        odd.next = odd.next.next
        odd = odd.next

        #connect the next even node with the current even node 
        even.next = even.next.next
        even = even.next

    odd.next = even_head
    return head.next.next.val


input = populateNode(nodes=[2, 1, 3, 5, 6, 4, 7])
answer = oddEvenList(head=input)
print("answer is")
print(answer)
