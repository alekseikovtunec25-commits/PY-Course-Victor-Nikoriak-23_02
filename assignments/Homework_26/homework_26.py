#Task 1
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid

    if target < arr[mid]:
        return binary_search_recursive(arr, target, left, mid - 1)

    return binary_search_recursive(arr, target, mid + 1, right)


if __name__ == "__main__":
    numbers = [1, 3, 5, 7, 9, 11, 13, 15]

    target = 9

    result = binary_search_recursive(
        numbers,
        target,
        0,
        len(numbers) - 1
    )

    print(f"Element found at index: {result}")

def fibonacci_search(arr, target):
    n = len(arr)

    fib2 = 0
    fib1 = 1
    fib = fib1 + fib2

    while fib < n:
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2

    offset = -1

    while fib > 1:

        i = min(offset + fib2, n - 1)

        if arr[i] < target:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i

        elif arr[i] > target:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1

        else:
            return i

    if fib1 and offset + 1 < n and arr[offset + 1] == target:
        return offset + 1

    return -1


if __name__ == "__main__":
    numbers = [1, 3, 5, 7, 9, 11, 13, 15]

    target = 11

    result = fibonacci_search(numbers, target)

    print(f"Element found at index: {result}")
