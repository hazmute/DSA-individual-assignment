class Node:
    def __init__(self, data):
        # each Node has a piece of data and a reference to the next Node in the list
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        # initialize an empty stack with a pointer to the top of the stack (head) and count of elements
        self.head = None
        self.count = 0

    def isEmpty(self):
        # check if the stack is empty
        return self.head is None

    def size(self):
        # return the size of the stack
        return self.count

    def push(self, data):
        # add a new element to the top of the stack
        new_node = Node(data)  # create a new node
        new_node.next = self.head  # point the new node to the current top of the stack
        self.head = new_node  # update the top of the stack to the new node
        self.count += 1  # increment the count of elements

    def pop(self):
        # remove and return the top element of the stack
        if self.isEmpty():
            print("Stack is empty")
            return None
        popped = self.head.data  # get the data from the top node
        self.head = self.head.next  # move the pointer to the next node
        self.count -= 1  # decrement the count of elements
        return popped

    def peek(self):
        # return the top element of the stack without removing it
        if self.isEmpty():
            print("Stack is empty")
            return None
        return self.head.data

    def display(self):
        # display all elements of the stack
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def clear(self):
        # clear the stack
        self.head = None
        self.count = 0

    def get_items(self):
        # this returns all elements of the stack as a list
        items = []
        current = self.head
        while current:
            items.append(current.data)
            current = current.next
        return items

# examples
stack = Stack()
stack.push(3)
stack.push(6)
stack.push(9)

print("Stack size:", stack.size())

print("Stack items:", stack.get_items())

print("Popped element:", stack.pop())

print("Top element:", stack.peek())

print("Items after popping:", stack.get_items())

stack.clear()
print("Items after clearing:", stack.get_items())
