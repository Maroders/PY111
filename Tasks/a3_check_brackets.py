def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "(()(()()))", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    if not brackets_row:  # сложность O(1)
        return True

    stack = []

    for i in range(len(brackets_row)):  # сложность O(n)
        if not stack:
            stack.append(brackets_row[i])  # сложность O(1)

            if stack[0] == ")":  # сложность O(1)
                return False

        else:
            if stack[-1] == brackets_row[i]:  # сложность O(1)
                stack.append(brackets_row[i])  # сложность O(1)

            else:
                del stack[-1]  # сложность O(1)

    if not stack:
        return True  # сложность O(1)

    else:
        return False  # сложность O(1)

# Общая сложность O(n)
