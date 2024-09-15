var head;

class Node {
    constructor(val) {
        this.data = val;
        this.next = null;
    }
}

/* Function to check if linked list is a palindrome*/

var isPalindrome = function (head) {
    var slow = head;
    var fast = head;
    while (fast && fast.next) {
        slow = slow.next;
        fast = fast.next.next;
    }

    var curr = slow;
    var prev = null;
    while (curr) {
        const next = curr.next;
        curr.next = prev;
        prev = curr;
        curr = next;
    }

    let p1 = head;
    let p2 = prev;
    while (p2) {
        if (p1.data !== p2.data) {
            return false;
        }

        p1 = p1.next;
        p2 = p2.next;
    }
    return true;
};

// prints content of double linked list
function printList(node) {
    while (node != null) {
        console.log(node.data + " ");
        node = node.next;
    }
}

// Driver Code

head = new Node(1);
head.next = new Node(1);
head.next.next = new Node(2);
head.next.next.next = new Node(1);

console.log("Given linked list");
printList(head);
var result = isPalindrome(head);
console.log("is linked list palindrome");
console.log(result);
