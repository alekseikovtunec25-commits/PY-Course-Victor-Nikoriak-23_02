#Task1

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


def reverse_sequence(sequence: str) -> str:
    stack = Stack()

    # кладём все символы в стек
    for char in sequence:
        stack.push(char)

    # достаём в обратном порядке
    reversed_chars = []
    while not stack.is_empty():
        reversed_chars.append(stack.pop())

    return "".join(reversed_chars)


if __name__ == "__main__":
    text = input("Введите последовательность символов: ")
    result = reverse_sequence(text)
    print("Результат:", result)

#Task2

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]


def is_balanced(sequence: str) -> bool:
    stack = Stack()

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in sequence:
        # если открывающая скобка → кладём в стек
        if char in "([{":
            stack.push(char)

        # если закрывающая → проверяем соответствие
        elif char in ")]}":
            if stack.is_empty():
                return False

            top = stack.pop()
            if top != pairs[char]:
                return False

    # если стек пуст → всё сбалансировано
    return stack.is_empty()


if __name__ == "__main__":
    text = input("Введите последовательность: ")

    if is_balanced(text):
        print("Скобки сбалансированы ✅")
    else:
        print("Скобки НЕ сбалансированы ❌")

#Task3

# Решение Stack
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def get_from_stack(self, e):
        temp_stack = []

        found = False

        # разбираем стек
        while not self.is_empty():
            item = self.pop()

            if item == e and not found:
                found = True
                result = item

            temp_stack.append(item)

        # возвращаем элементы обратно
        while temp_stack:
            self.push(temp_stack.pop())

        if not found:
            raise ValueError(f"Element {e} not found in stack")

        return result

# Решение Queue

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def get_from_stack(self, e):
        size = len(self.items)
        found = False
        result = None

        for _ in range(size):
            item = self.dequeue()

            if item == e and not found:
                found = True
                result = item

            self.enqueue(item)

        if not found:
            raise ValueError(f"Element {e} not found in queue")

        return result
