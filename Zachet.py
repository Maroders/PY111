# a = len(arr) - 1  # O(1)
# out = list()  # O(1)
# while a > 0:  # O (log n)
#     out.append(arr[a])  # O(1) + O(1)
#     a = a // 1.7  # O(1)
# out.merge_sort()  # O(log n * log(log n))

# log n + n log n -> n log n


# Дано N человек, считалка из K слогов. Считалка начинает считать с первого человека.
# Когда считалка досчитывает до k-го слога, человек, на котором она остановилась, вылетает.
# Игра происходит до тех пор, пока не останется последний человек.
# Для данных N и К дать номер последнего оставшегося человека.

def game(N, K):  # K - машинный

    list_ = [human for human in range(N)]  # O(n)

    def _game(human_list):
        if len(human_list) == 1:
            return human_list

        queue = []
        i = 0
        while True:
            queue.append(list_[i])  # O(1)
            human_list.append(queue.pop())  # O(1) + O(1)

            i += 1  # O(1)
            if i == K:  # O(1)
                new_list = human_list[i + 1:]  # O(k)

                return _game(new_list)

    return _game(list_)


if __name__ == '__main__':
    N = 5
    K = 2
    print(game(N, K))


orders = [
    (1, 4),
    (7, 10),
    (3, 10)
]

HOURS_IN_DAY = 24
def task():

    busy_hours = [0] * HOURS_IN_DAY

    for order in orders:
        for busy_hour in range(*order):
            busy_hours[busy_hour] += 1

    return not any(hour > 1 for hour in busy_hours)

from collections import deque

def task_2(players: int, counter: int):
    players_deque = deque(range(players))

    for _ in range(players - 1):
        for _ in range(counter - 1):
            players_deque.append(players_deque.popleft())
        players_deque.popleft()
