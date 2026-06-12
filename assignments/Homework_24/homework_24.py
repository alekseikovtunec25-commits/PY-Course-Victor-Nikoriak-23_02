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