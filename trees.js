class Node {
    constructor(val) {
        this.value = val;
        this.left = null;
        this.right = null;
    }
}

class BinarySearchTree {
    constructor() {
        this.root = null;
    }

    insert(value) {
        const newNode = new Node(value);
        //check if no root and insert root first
        if (this.root === null) {
            this.root = newNode;
        } else {
            let currentNode = this.root;
            while (true) {
                if (value < currentNode.value) {
                    //left
                    if (!currentNode.left) {
                        currentNode.left = newNode;
                        return this;
                    }
                    currentNode = currentNode.left;
                } else if (value > currentNode.value) {
                    //right
                    if (!currentNode.right) {
                        currentNode.right = newNode;
                        return this;
                    }
                    currentNode = currentNode.right;
                }
            }
        }
    }

    lookup(value) {
        if (!this.root) {
            return false;
        }
        let currentNode = this.root;
        while (currentNode) {
            if (value > currentNode) {
                currentNode = currentNode.right;
            } else if (value < currentNode) {
                currentNode = currentNode.left;
            } else {
                return currentNode;
            }
        }
        return false;
    }

    remove(value) {
        if (!this.root) {
            return false;
        }
        let currentNode = this.root;
        let parentNode = null;
        while (currentNode) {
            if (value < currentNode.value) {
                parentNode = currentNode;
                currentNode = currentNode.left;
            } else if (value > currentNode.value) {
                parentNode = currentNode;
                currentNode = currentNode.right;
            } else if (currentNode.value === value) {
                //We have a match, get to work!

                //Option 1: No right child:
                if (currentNode.right === null) {
                    if (parentNode === null) {
                        this.root = currentNode.left;
                    } else {
                        //if parent > current value, make current left child a child of parent
                        if (currentNode.value < parentNode.value) {
                            parentNode.left = currentNode.left;

                            //if parent < current value, make left child a right child of parent
                        } else if (currentNode.value > parentNode.value) {
                            parentNode.right = currentNode.left;
                        }
                    }

                    //Option 2: Right child which doesnt have a left child
                } else if (currentNode.right.left === null) {
                    currentNode.right.left = currentNode.left;
                    if (parentNode === null) {
                        this.root = currentNode.right;
                    } else {
                        //if parent > current, make right child of the left the parent
                        if (currentNode.value < parentNode.value) {
                            parentNode.left = currentNode.right;

                            //if parent < current, make right child a right child of the parent
                        } else if (currentNode.value > parentNode.value) {
                            parentNode.right = currentNode.right;
                        }
                    }

                    //Option 3: Right child that has a left child
                } else {
                    //find the Right child's left most child
                    let leftmost = currentNode.right.left;
                    let leftmostParent = currentNode.right;
                    while (leftmost.left !== null) {
                        leftmostParent = leftmost;
                        leftmost = leftmost.left;
                    }

                    //Parent's left subtree is now leftmost's right subtree
                    leftmostParent.left = leftmost.right;
                    leftmost.left = currentNode.left;
                    leftmost.right = currentNode.right;

                    if (parentNode === null) {
                        this.root = leftmost;
                    } else {
                        if (currentNode.value < parentNode.value) {
                            parentNode.left = leftmost;
                        } else if (currentNode.value > parentNode.value) {
                            parentNode.right = leftmost;
                        }
                    }
                }
                return true;
            }
        }
    }
}

function traverse(node) {

    const tree = new Node(node.value)
    tree.left = node.left === null ? null : traverse(node.left);
    tree.right = node.right === null ? null : traverse(node.right);
    return tree;
}

//     9
//  4    20
//1  6  15 170
function BFS(root) {
    var queue = [root];
    while(queue.length > 0){
        const current = queue.shift()
        console.log(current.value,"")
        if(current.left) queue.push(current.left)
        if(current.right) queue.push(current.right)
    }
}

function DFSInOrder(root) {
    let stack = [root];
    let current = root.value;
    while (stack.length) {
        while (current.left) {
            current = current.left
            stack.push(current)
        }
        current = stack.pop()
        console.log('current is ', current);
        if (current.right) {
            current = current.right
            stack.push(current)
        }
    }

    //given two tree root nodes
    // let stack = [[p, q]];
    // while (stack.length > 0) {
    //     const [p, q] = stack.pop()
    //     if (!p && !q) {
    //         return true
    //     }
    //     if (!p || !q || p.val !== q.val) {
    //         return false
    //     }
    //     if (p.left || q.left) {
    //         stack.push([p.left, q.left]);
    //     }
    //     if (p.right || q.right) {
    //         stack.push([p.right, q.right]);
    //     }
    // }
    // return true
}



const tree = new BinarySearchTree();
tree.insert(9);
tree.insert(4);
tree.insert(6);
tree.insert(20);
tree.insert(170);
tree.insert(15);
tree.insert(1);
// DFSInOrder(tree.root);
BFS(tree.root);
//     9
//  4    20
//1  6  15 170

// tree.insert(1);
// tree.remove(170);
// console.log(`${JSON.stringify(traverse(tree.root))}`);
// console.log(tree.lookup(230));