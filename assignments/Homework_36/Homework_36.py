#Task1

#Asyncio
import asyncio
import time


async def fibonacci(n):
    if n <= 1:
        return n

    a, b = 0, 1

    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


async def factorial(n):
    result = 1

    for i in range(2, n + 1):
        result *= i

    return result


async def square(n):
    return n ** 2


async def cube(n):
    return n ** 3


async def main():
    numbers = list(range(1, 11))

    start = time.perf_counter()

    fibonacci_results = await asyncio.gather(
        *(fibonacci(n) for n in numbers)
    )

    factorial_results = await asyncio.gather(
        *(factorial(n) for n in numbers)
    )

    square_results = await asyncio.gather(
        *(square(n) for n in numbers)
    )

    cube_results = await asyncio.gather(
        *(cube(n) for n in numbers)
    )

    end = time.perf_counter()

    print("Fibonacci:", fibonacci_results)
    print("Factorial:", factorial_results)
    print("Square:", square_results)
    print("Cube:", cube_results)

    print(f"\nAsyncio time: {end - start:.6f} sec")


if __name__ == "__main__":
    asyncio.run(main())

#Multiprocessing

from multiprocessing import Pool
import time


def fibonacci(n):
    if n <= 1:
        return n

    a, b = 0, 1

    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


def factorial(n):
    result = 1

    for i in range(2, n + 1):
        result *= i

    return result


def square(n):
    return n ** 2


def cube(n):
    return n ** 3


if __name__ == "__main__":

    numbers = list(range(1, 11))

    start = time.perf_counter()

    with Pool() as pool:

        fibonacci_results = pool.map(
            fibonacci,
            numbers
        )

        factorial_results = pool.map(
            factorial,
            numbers
        )

        square_results = pool.map(
            square,
            numbers
        )

        cube_results = pool.map(
            cube,
            numbers
        )

    end = time.perf_counter()

    print("Fibonacci:", fibonacci_results)
    print("Factorial:", factorial_results)
    print("Square:", square_results)
    print("Cube:", cube_results)

    print(
        f"\nMultiprocessing time: "
        f"{end - start:.6f} sec"
    )
