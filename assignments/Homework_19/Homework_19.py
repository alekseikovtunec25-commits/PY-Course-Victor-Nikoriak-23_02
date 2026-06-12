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

#Task 2

def in_range(start, end=None, step=1):

    if end is None:
        end = start
        start = 0

    if step == 0:
        raise ValueError("step не может быть равен 0")

    if step > 0:
        while start < end:
            yield start
            start += step
    else:
        while start > end:
            yield start
            start += step
print(list(in_range(10, 0, -1)))
