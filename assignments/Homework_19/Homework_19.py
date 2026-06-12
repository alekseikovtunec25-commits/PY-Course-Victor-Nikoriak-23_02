#Task 1

def with_index(iterable, start=0):
    for item in iterable:
        yield start, item
        start += 1


if __name__ == "__main__":
    names = ["Alex", "John", "Kate"]

    for index, name in with_index(names):
        print(index, name)

    print()

    for index, name in with_index(names, start=10):
        print(index, name)