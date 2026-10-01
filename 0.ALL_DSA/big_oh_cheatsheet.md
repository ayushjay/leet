| Data Structure         |             Access |             Search |          Insertion |           Deletion |
| ---------------------- | -----------------: | -----------------: | -----------------: | -----------------: |
| **Array**              |               O(1) |               O(n) |               O(n) |               O(n) |
| **Stack**              |               O(n) |               O(n) |               O(1) |               O(1) |
| **Queue**              |               O(n) |               O(n) |               O(1) |               O(1) |
| **Singly Linked List** |               O(n) |               O(n) |              O(1)* |              O(1)* |
| **Doubly Linked List** |               O(n) |               O(n) |              O(1)* |              O(1)* |
| **Skip List**          |      O(log n) avg. |      O(log n) avg. |      O(log n) avg. |      O(log n) avg. |
| **Hash Table**         |                N/A |          O(1) avg. |          O(1) avg. |          O(1) avg. |
| **Binary Search Tree** |      O(log n) avg. |      O(log n) avg. |      O(log n) avg. |      O(log n) avg. |
| **Cartesian Tree**     |                N/A |               O(n) |      O(log n) avg. |      O(log n) avg. |
| **B-Tree**             |           O(log n) |           O(log n) |           O(log n) |           O(log n) |
| **Red-Black Tree**     |           O(log n) |           O(log n) |           O(log n) |           O(log n) |
| **Splay Tree**         | O(log n) amortized | O(log n) amortized | O(log n) amortized | O(log n) amortized |
| **AVL Tree**           |           O(log n) |           O(log n) |           O(log n) |           O(log n) |
| **KD Tree**            |      O(log n) avg. |      O(log n) avg. |      O(log n) avg. |      O(log n) avg. |

* For linked lists, insertion/deletion is **O(1)** when you already have the relevant node/pointer; finding that position first takes **O(n)**.

**Quick memory rule:**

* Array → access **O(1)**
* Hash table → search/insert/delete **O(1) average**
* Balanced BSTs → search/insert/delete **O(log n)**
* Linked list → access/search **O(n)**
* Stack/Queue → insert/delete at their ends **O(1)**
