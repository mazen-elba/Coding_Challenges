class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # O(1) time | O(1) space
    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    # O(1) time | O(1) space
    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
            return
        self.insertAfter(self.tail, node)

    # O(1) time | O(1) space
    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    # O(1) time | O(1) space
    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    # O(P) time | O(1) space
    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        node = self.head
        currentPosition = 1
        while node is not None and currentPosition != position:
            node = node.next
            currentPosition += 1
        if node is not None:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    # O(N) time | O(1) space
    def removeNodesWithValue(self, value):
        node = self.head
        while node is not None:
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)

    # O(1) time | O(1) space
    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        self.removeNodeBindings(node)

    # O(N) time | O(1) space
    def containsNodeWithValue(self, value):
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        return node is not None

    def removeNodeBindings(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None


def removeNodes(linkedList, nodes):
    for node in nodes:
        linkedList.remove(node)


# --- Test Cases --- #
print("---------- Test Case 1 ------------")
linkedList = DoublyLinkedList()
node = Node(1)
print(linkedList.setHead(node))
print(linkedList.remove(node))
print(linkedList.setTail(node))
print(linkedList.removeNodesWithValue(1))
print(linkedList.insertAtPosition(1, node))

print("---------- Test Case 2 ------------")
linkedList = DoublyLinkedList()
first = Node(1)
second = Node(2)
nodes = [first, second]
print(linkedList.setHead(first))
print(linkedList.setTail(second))
print(removeNodes(linkedList, nodes))
print(linkedList.setHead(first))
print(linkedList.insertAfter(first, second))
print(removeNodes(linkedList, nodes))
print(linkedList.setHead(first))
print(linkedList.insertBefore(first, second))
print(removeNodes(linkedList, nodes))
print(linkedList.insertAtPosition(1, first))
print(linkedList.insertAtPosition(2, second))
print(removeNodes(linkedList, nodes))
print(linkedList.insertAtPosition(2, first))
print(linkedList.insertAtPosition(1, second))

print("---------- Test Case 3 ------------")
linkedList = DoublyLinkedList()
first = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
print(linkedList.setHead(first))
print(linkedList.insertAfter(first, second))
print(linkedList.insertAfter(second, third))
print(linkedList.insertAfter(third, fourth))
print(linkedList.removeNodesWithValue(3))
print(linkedList.remove(first))
print(linkedList.removeNodesWithValue(4))
print(linkedList.remove(second))

print("---------- Test Case 4 ------------")
linkedList = DoublyLinkedList()
first = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(3)
fifth = Node(3)
sixth = Node(6)
seventh = Node(7)
print(linkedList.setHead(first))
print(linkedList.insertAfter(first, second))
print(linkedList.insertAfter(second, third))
print(linkedList.insertAfter(third, fourth))
print(linkedList.insertAfter(fourth, fifth))
print(linkedList.insertAfter(fifth, sixth))
print(linkedList.insertAfter(sixth, seventh))
print(linkedList.remove(second))
print(linkedList.removeNodesWithValue(1))
print(linkedList.removeNodesWithValue(3))
print(linkedList.removeNodesWithValue(7))

print("---------- Test Case 5 ------------")
linkedList = DoublyLinkedList()
first = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)
sixth = Node(6)
seventh = Node(7)
print(linkedList.setHead(first))
print(linkedList.insertAfter(first, second))
print(linkedList.insertAfter(second, third))
print(linkedList.insertAfter(third, fourth))
print(linkedList.insertAfter(fourth, fifth))
print(linkedList.insertAfter(third, fifth))
print(linkedList.insertAfter(third, first))
print(linkedList.insertAfter(fifth, second))
print(linkedList.insertAfter(second, first))
print(linkedList.insertAfter(fourth, sixth))
print(linkedList.insertAfter(second, seventh))

print("---------- Test Case 6 ------------")
linkedList = DoublyLinkedList()
first = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)
sixth = Node(6)
seventh = Node(7)
print(linkedList.setHead(first))
print(linkedList.insertBefore(first, second))
print(linkedList.insertBefore(second, third))
print(linkedList.insertBefore(third, fourth))
print(linkedList.insertBefore(fourth, fifth))
print(linkedList.insertBefore(third, first))
print(linkedList.insertBefore(fifth, second))
print(linkedList.insertBefore(fifth, fourth))
print(linkedList.insertBefore(second, sixth))
print(linkedList.insertBefore(first, seventh))

print("---------- Test Case 7 ------------")
linkedList = DoublyLinkedList()
first = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)
sixth = Node(6)
seventh = Node(7)
print(linkedList.setHead(first))
print(linkedList.insertAtPosition(1, second))
print(linkedList.insertAtPosition(1, third))
print(linkedList.insertAtPosition(1, fourth))
print(linkedList.insertAtPosition(1, fifth))
print(linkedList.insertAtPosition(2, first))
print(linkedList.insertAtPosition(1, second))
print(linkedList.insertAtPosition(2, fourth))
print(linkedList.insertAtPosition(1, sixth))
print(linkedList.insertAtPosition(5, seventh))
print(linkedList.insertAtPosition(8, fourth))
