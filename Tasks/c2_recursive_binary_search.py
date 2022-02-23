from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence, left_border: Optional[int] = None, right_border: Optional[int] = None) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    if left_border is None:
        left_border = 0
    if right_border is None:
        right_border = len(arr) - 1

    middle_index = (left_border + right_border) // 2

    if len(arr[left_border:right_border]) == 1 and elem == arr[right_border]:
        return right_border
    if len(arr[left_border:right_border]) == 0:
        return None
    if len(arr[left_border:right_border]) == 1 and elem != arr[middle_index]:
        return None
    if elem == arr[middle_index]:
        return middle_index
    if elem < arr[middle_index]:

        right_border = middle_index
        return binary_search(elem, arr, left_border, right_border)
    if elem > arr[middle_index]:

        left_border = middle_index
        return binary_search(elem, arr, left_border, right_border)


arr = [i for i in range(100)] + [101]
# print(binary_search(5, arr))

# print(binary_search(-1, arr))

# print(binary_search(100, arr))

print(binary_search(0, arr))

print(binary_search(101, arr))