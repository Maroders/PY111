def factorial_recursive(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in recursive way
    :param n: int > 0
    :return: factorial of n
    """
    # if n < 0:
    #     raise ValueError()
    # if n == 1:
    #     return 1
    # for i in range(2, n + 1):
    #     f_num = factorial_recursive(n - 1) * n
    #
    # return f_num

    if n == 1:
        return 1

    return factorial_recursive(n - 1) * n

# почему работает и в цикле и просто с return?

def factorial_iterative(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in iterative way

    :param n: int > 0
    :return: factorial of n
    """
    if n < 0:
        raise ValueError()
    f_num = 1
    for i in range(2, n + 1):
        f_num *= i

    return f_num

print(factorial_recursive(5))