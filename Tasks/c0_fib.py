from typing import Iterator

def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm
    Запрашиваем человекочитаемый индекс
    :param n: number of item
    :return: Fibonacci number
    """
    if n == 1:
        return 0
    if n == 2:
        return 1

    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n == 1:
        fib_num_1 = 0
        return fib_num_1
    if n == 2:
        fib_num_2 = 1
        return fib_num_2
    else:
        fib_num_1 = 0
        fib_num_2 = 1

        for i in range(n - 2):
            fib_num_1, fib_num_2 = fib_num_2, fib_num_1 + fib_num_2

    return fib_num_2


def fib_generator(n: int) -> Iterator[int]:

    yield 0
    yield 1
    if n > 2:

        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b
            yield b



print(fib_recursive(5))
print(fib_iterative(5))
fib_gen = fib_generator(5)
# print(list(fib_gen))
for _ in range(5):
    fg = next(fib_gen)
print(fg)

