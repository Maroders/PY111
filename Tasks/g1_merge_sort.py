from typing import List
import random


def merge_func(sorted_left: List[int], sorted_right: List[int]) -> List[int]:
    merged_list = []
    one = sorted_left
    two = sorted_right
    i = 0
    j = 0
    while True:

        if sorted_left[i] > sorted_right[j]:
            merged_list.append(sorted_right[j])
            j += 1
        elif sorted_left[i] < sorted_right[j]:
            merged_list.append(sorted_left[i])
            i += 1
        else:
            merged_list += [(sorted_left[i])] + [(sorted_right[j])]
            i += 1
            j += 1

        if i >= len(sorted_left):
            merged_list += sorted_right[j:]
            break
        if j >= len(sorted_right):
            merged_list += sorted_left[i:]
            break

    return merged_list

    # sorted_result = []
    #
    # current_left_index = 0  # i
    # current_right_index = 0  # j
    #
    # while True:
    #     current_left_value = sorted_left[current_left_index]
    #     current_right_value = sorted_right[current_right_index]
    #
    #     if current_left_value <= current_right_value:
    #         sorted_result.append(current_left_value)
    #         current_left_index += 1
    #
    #     else:
    #         sorted_result.append(current_right_value)
    #         current_right_index += 1
    #
    #     if current_left_index == len(sorted_left):
    #         sorted_result.extend(sorted_right[current_right_index:])
    #         break
    #
    #     if current_right_index == len(sorted_right):
    #         sorted_result.extend(sorted_left[current_left_index:])
    #         break
    #
    # return sorted_result


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with merge sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if len(container) == 1:
        return container

    middle_index = len(container) // 2
    left_part = sort(container[:middle_index])
    right_part = sort(container[middle_index:])

    return merge_func(left_part, right_part)

arr = [random.randint(-100, 100) for _ in range(30)]
print(sort(arr))
