var head;

class Node {
    constructor(val) {
        this.data = val;
        this.next = null;
    }
}

/* Function to reverse the linked list */
function reverse(head, m, n) {
    var current = head;
    var start = head;
    var position = 1;

    while (position < m) {
        start = current;
        current = current.next;
        position++;
    }

    let tail = current, newList = null;

    while (position >= m && position <= n) {
        const next = current.next;
        current.next = newList;
        newList = current;
        current = next;
        position++;
    }

    start.next = newList;
    tail.next = current;

    if (m > 1) {
        return start;
    } else {
        return newList;
    }

}

// prints content of double linked list
function printList(node) {
    while (node != null) {
        console.log(node.data + " ");
        node = node.next;
    }
}

// Driver Code

head = new Node(1);
head.next = new Node(2);
head.next.next = new Node(3);
head.next.next.next = new Node(4);
head.next.next.next.next = new Node(5);

console.log("Given linked list");
printList(head);
head = reverse(head, 2, 4);
console.log("Reversed linked list");
printList(head);

