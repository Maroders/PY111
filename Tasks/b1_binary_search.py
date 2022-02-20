from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    # middle_index = len(arr) // 2
    # left_border_index = 0
    # print(left_border_index)
    # right_border_index = len(arr)
    # print(right_border_index)
    #
    # while True:
    #     if elem == arr[middle_index]:
    #         while True:
    #             middle_index = middle_index - 1
    #             if elem != arr[middle_index]:
    #                 return middle_index + 1
    #         return middle_index
    #     if elem < arr[middle_index]:
    #         right_border_index = middle_index
    #         middle_index = middle_index - len(arr[left_border_index:right_border_index]) // 2
    #         print(middle_index)
    #     if elem > arr[middle_index]:
    #         left_border_index = middle_index
    #         print(arr[left_border_index:right_border_index])
    #         middle_index = middle_index + len(arr[left_border_index:right_border_index]) // 2
    #         print(middle_index)
    #     if len(arr[left_border_index:right_border_index]) == 2:
    #         if elem < arr[middle_index]:
    #             middle_index = middle_index - 1
    #         if elem > arr[middle_index]:
    #             middle_index = middle_index + 1
    #     if len(arr[left_border_index:right_border_index]) == 1:
    #         if elem < arr[middle_index]:
    #             middle_index = middle_index - 1
    #             if [elem] != arr[left_border_index:right_border_index]:
    #                 return None
    #             else:
    #                 return middle_index
    #         if elem > arr[middle_index]:
    #             middle_index = middle_index + 1
    #             if [elem] != arr[left_border_index:right_border_index]:
    #                 return None
    #             else:
    #                 return middle_index
    #     # if len(arr[left_border_index:right_border_index]) == 1 and [elem] != arr[left_border_index:right_border_index]:
    #     #     return None
    #     # if len(arr[left_border_index:right_border_index]) == 1:
    #     #     return middle_index
    #     if not arr[left_border_index:right_border_index]:
    #         return None
    #     if middle_index == len(arr):
    #         return None


    left_border = 0
    right_border = len(arr) - 1

    while left_border <= right_border:
        middle_index = left_border + (right_border - left_border) // 2
        middle_value = arr[middle_index]

        if middle_value == elem:
            return middle_index
        elif elem < middle_value:
            right_border = middle_index - 1

        elif elem > middle_value:
            left_border = middle_index + 1



# sequence = [i for i in range(100)] + [101]
# print(sequence)
# element = 5
# print(binary_search(element, sequence))

# sequence = [i for i in range(100)] + [101]
# print(sequence)
# element = 54
# print(binary_search(element, sequence))

# sequence = [i for i in range(100)] + [101]
# print(sequence)
# element = 101
# print(binary_search(element, sequence))

# sequence = [i for i in range(100)] + [101]
# print(sequence)
# element = 0
# print(binary_search(element, sequence))

# sequence = [i for i in range(100)] + [101]
# print(sequence)
# element = -1
# print(binary_search(element, sequence))

# sequence = [i for i in range(100)] + [101]
# print(sequence)
# element = 100
# print(binary_search(element, sequence))

sequence_2 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]  # вот эта последовательноть работает только с моим кодом
element_2 = 2
print(binary_search(element_2, sequence_2))  # expect 5

# sequence_2 = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
# element_2 = 2
# print(binary_search(element_2, sequence_2))

# sequence_2 = [8, 9, 10]
# element_2 = 11
# print(binary_search(element_2, sequence_2))

# sequence_2 = [1, 2, 3]
# element_2 = 3
# print(binary_search(element_2, sequence_2))


# Прошу прокомментировать 2 вопроса:
# Вопрос № 1:
# правильно ли я понимаю, что проверку и возвращение первого из нескольких элементов невозможно без рекурсии
# если без рекурсии, то только простым перебором, примерно так:
#         if elem == arr[middle_index]:
#             while True:
#                 middle_index = middle_index - 1
#                 if elem != arr[middle_index]:
#                     return middle_index + 1
#             return middle_index
# Вопрос № 2:
# не слишком ли много костылей? По сути вводил условие за условием под каждый юнит-тест. Но в итоге все тесты проходит.


