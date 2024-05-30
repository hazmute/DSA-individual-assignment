# first we import the tabulate library for formatting output
from tabulate import tabulate

# task class to represent individual tasks
class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def getTitle(self):
        return self.title

    def getDescription(self):
        return self.description

    def isCompleted(self):
        return self.completed

    def markCompleted(self):
        self.completed = True

# node class to represent a node in the linked list
class Node:
    def __init__(self, task):
        self.task = task
        self.next = None

# toDoList class to manage the list of tasks
class ToDoList:
    def __init__(self):
        self.head = None

    def addToDo(self, task):
        new_node = Node(task)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def markToDoAsCompleted(self, title):
        current = self.head
        while current is not None:
            if current.task.getTitle() == title:
                current.task.markCompleted()
                print(f'Task "{title}" marked as completed.')
                return
            current = current.next
        print(f'Task "{title}" not found.')

    def viewToDoList(self):
        current = self.head
        if current is None:
            print("The to-do list is empty.")
        else:
            tasks = []
            while current is not None:
                tasks.append([current.task.getTitle(), current.task.getDescription(), current.task.isCompleted()])
                current = current.next
            print(tabulate(tasks, headers=["Title", "Description", "Completed"], tablefmt="grid"))

# main section to interact with the ToDoList
if __name__ == "__main__":
    todo_list = ToDoList()

    while True:
        title = input("enter task title (or 'q' to quit, 'v' to view list): ")
        if title == 'q':
            break
        elif title == 'v':
            todo_list.viewToDoList()
            completion = input("enter task title to be marked as complete (or 'b' to go back): ")
            if completion == 'b':
                continue
            elif completion == 'q':
                break
            todo_list.markToDoAsCompleted(completion)
            continue

        description = input("Enter task description: ")
        task = Task(title, description)
        todo_list.addToDo(task)

    print("Final To-Do List:")
    todo_list.viewToDoList()