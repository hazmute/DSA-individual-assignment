class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # each node has a reference to the next node in the list

class LinkedList:
    def __init__(self):
        self.head = None  # initially, the linked list is empty

    def insertAtPos(self, data, position):
        new_node = Node(data)  # create a new node with the given data
        if position == 1:
            # if the position is 1, insert the new node at the beginning of the list
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        # this traverses the list to find the node at the (position - 1)th position
        for _ in range(position - 2):
            if current is None:
                raise IndexError("Position out of bounds")
            current = current.next
        # insert the new node after the (position - 1)th node
        if current is None:
            raise IndexError("Position out of bounds")
        new_node.next = current.next
        current.next = new_node

    def deleteAtPosition(self, position):
        if self.head is None:
            raise IndexError("List is empty")
        if position == 1:
            # if position is 1, delete the first node by moving head to the next node
            self.head = self.head.next
            return
        current = self.head
        # traverse the list to find the node at the (position - 1)th position
        for _ in range(position - 2):
            if current is None or current.next is None:
                raise IndexError("Position out of bounds")
            current = current.next
        if current.next is None:
            raise IndexError("Position out of bounds")
        # delete the node at the given position by adjusting pointers
        current.next = current.next.next

    def deleteAfterNode(self, prev_node):
        if prev_node is None or prev_node.next is None:
            raise ValueError("Invalid previous node")
        # delete the node after the given previous node by adjusting pointers
        prev_node.next = prev_node.next.next

    def searchNode(self, value):
        current = self.head
        position = 1
        # traverse the list to find the node with the given value
        while current:
            if current.data == value:
                return position  # return the position if the value is found
            current = current.next
            position += 1
        return -1  # return -1 if the value is not found

    def printList(self):
        current = self.head
        # this traverses the list and print each node's data
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # print "None" to indicate the end of the list

# Examples
ll = LinkedList()
ll.insertAtPos(5, 1)
ll.insertAtPos(10, 2)
ll.insertAtPos(15, 3)
ll.insertAtPos(10, 2) 
ll.printList() 
ll.deleteAtPosition(2) 
ll.printList()
ll.deleteAfterNode(ll.head)
ll.printList()
print(ll.searchNode(10)) 
print(ll.searchNode(50)) 