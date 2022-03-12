from typing import List
import random


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with quick sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """

    # if not container:
    #     return container
    # base_element = random.choice(container)
    # left_container = [element for element in container if element < base_element]
    # right_container = [element for element in container if element > base_element]
    # central_container = [element for element in container if element == base_element]
    #
    #
    #
    # return sort(left_container) + central_container + sort(right_container)

    def _sort(left_border, right_border):
        if left_border >= right_border:
            return None

        i, j = left_border, right_border
        pivot_index = random.randint(left_border, right_border)
        pivot = container[pivot_index]

        while i <= j:
            while container[i] < pivot:
                i += 1
            while container[j] > pivot:
                j -= 1

            if i <= j:
                container[i], container[j] = container[j], container[i]
                i += 1
                j -= 1

        _sort(left_border, j)
        _sort(i, right_border)

    _sort(0, len(container) - 1)
    return container