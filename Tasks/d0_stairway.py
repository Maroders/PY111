from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:  # прямой порядок
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    count_stairs = len(stairway)
    print(stairway)
    print("------")
    for i in range(2, count_stairs):
        stairway[i] = stairway[i] + min(stairway[i - 1], stairway[i - 2])
        print(stairway)
    return stairway[-1]

print(stairway_path([1, 3, 1, 5, 2, 7, 7, 8, 9, 4, 6, 3]))  #26


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:  # обратный порядок
    print(stairway)
    print("------")
    for index, value in enumerate(stairway):
        if index < len(stairway) - 2:

            stairway[index + 2] = stairway[index + 2] + min(stairway[index], stairway[index + 1])
            print(stairway)
    return stairway[-1]

print(stairway_path([1, 3, 1, 5, 2, 7, 7, 8, 9, 4, 6, 3]))  #26


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:  #рекурсия

    total_costs = {}
    def lazy(stair_number: int) -> Union[float, int]:
        if stair_number in total_costs:
            return total_costs[stair_number]
        if stair_number == 0:
            total_costs[stair_number] = stairway[stair_number]
            return total_costs[stair_number]
        if stair_number == 1:
            total_costs[stair_number] = stairway[stair_number]
            return total_costs[stair_number]


        current_cost = stairway[stair_number] + min(lazy(stair_number - 1), lazy(stair_number - 2))
        total_costs[stair_number] = current_cost
        print(total_costs)
        return total_costs[stair_number]

    return lazy(len(stairway) - 1)

print(stairway_path([1, 3, 1, 5, 2, 7, 7, 8, 9, 4, 6, 3]))  #26