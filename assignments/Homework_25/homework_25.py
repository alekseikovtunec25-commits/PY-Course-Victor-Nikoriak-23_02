#Task1
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class UnsortedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self.head

        while current:
            if current.get_data() == item:
                return True
            current = current.get_next()

        return False

    def remove(self, item):
        current = self.head
        previous = None

        while current:
            if current.get_data() == item:
                break

            previous = current
            current = current.get_next()

        if current is None:
            raise ValueError(f"{item} not found")

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def append(self, item):
        new_node = Node(item)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.get_next():
            current = current.get_next()

        current.set_next(new_node)

    def index(self, item):
        current = self.head
        position = 0

        while current:
            if current.get_data() == item:
                return position

            position += 1
            current = current.get_next()

        raise ValueError(f"{item} is not in list")

    def pop(self, pos=None):
        if self.head is None:
            raise IndexError("pop from empty list")

        if pos is None:
            pos = self.size() - 1

        if pos < 0 or pos >= self.size():
            raise IndexError("pop index out of range")

        current = self.head
        previous = None

        for _ in range(pos):
            previous = current
            current = current.get_next()

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

        return current.get_data()

    def insert(self, pos, item):
        if pos < 0 or pos > self.size():
            raise IndexError("insert position out of range")

        new_node = Node(item)

        if pos == 0:
            new_node.set_next(self.head)
            self.head = new_node
            return

        current = self.head
        previous = None

        for _ in range(pos):
            previous = current
            current = current.get_next()

        previous.set_next(new_node)
        new_node.set_next(current)

    def slice(self, start, stop):
        if start < 0 or stop < start:
            raise IndexError("invalid slice indexes")

        result = UnsortedList()

        current = self.head
        position = 0

        while current and position < stop:
            if position >= start:
                result.append(current.get_data())

            current = current.get_next()
            position += 1

        return result

    def __str__(self):
        items = []
        current = self.head

        while current:
            items.append(str(current.get_data()))
            current = current.get_next()

        return "[" + ", ".join(items) + "]"

#Task 2
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")

        item = self.top.data
        self.top = self.top.next
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")

        return self.top.data

    def size(self):
        count = 0
        current = self.top

        while current:
            count += 1
            current = current.next

        return count

    def __str__(self):
        items = []
        current = self.top

        while current:
            items.append(str(current.data))
            current = current.next

        return "Stack(top -> bottom): " + " -> ".join(items)

#Task 3

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)

        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")

        item = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        return self.front.data

    def size(self):
        count = 0
        current = self.front

        while current:
            count += 1
            current = current.next

        return count

    def __str__(self):
        items = []
        current = self.front

        while current:
            items.append(str(current.data))
            current = current.next

        return "Queue(front -> rear): " + " -> ".join(items)