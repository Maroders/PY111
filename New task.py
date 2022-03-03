from typing import Optional

def tile_cost(point: (int, int), matrix) -> int:
    """
    Ищем минимальную стоимость пути из начальной точки в заданную (point).
    :param matrix: передаваемое в функцию поле
    :param point: конечная точка
    :return: стоимость самого дешевого маршрута
    """

    def count(i: int, j: int) -> Optional[int, float]:

        if i == 0 and j == 0:
            return matrix[0][0]

        if i < 0:
            return float("inf")

        if j < 0:
            return float("inf")

        return matrix[i][j] + min(count(i, j - 1), count(i - 1, j))

    return count(point[0], point[1])


if __name__ == "__main__":

    print(tile_cost((2, 2), [[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(tile_cost((4, 4), [[2, 4, 3, 1, 7], [1, 3, 4, 5, 6], [4, 2, 7, 3, 2], [8, 6, 1, 4, 2], [7, 3, 5, 1, 2]]))




