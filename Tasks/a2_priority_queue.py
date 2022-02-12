"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any


class PriorityQueue:
    def __init__(self):
        self.priority_queue = {
            0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: []
        }  # todo для очереди можно использовать python dict
        print(len(self.priority_queue)) # печатаю длину словаря
        print(self.priority_queue) # печатаю словарь

    def enqueue(self, elem: Any, priority: int = 0) -> None:
        """
        Operation that add element to the end of the queue

        :param priority:
        :param elem: element to be added
        :return: Nothing
        """
        print(len(self.priority_queue)) # печатаю длину словаря
        print(priority) # печатаю переданное значение приоритета
        if priority > len(self.priority_queue) - 1:
            # return None
            raise IndexError("Too much") # предлагаю возвращать не None, а ошибку

        self.priority_queue[priority].append(elem)
        print(self.priority_queue) # печатаю словарь
        print(self.priority_queue[priority]) # печатаю очередь из словаря согласно переданному приоритету
        return None

    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if not elements.

        :return: dequeued element
        """
        print("++++++++++")
        print(self.priority_queue) # поскольку при проверке в этой функции словарь, а следовательно и его длина обнуляются
        # печатаю сам словарь ...
        print("++++++++++")
        len_ = len(self.priority_queue)
        print("---------")
        print(len_) # ... и его длину
        print("---------")
        print(self.priority_queue) # еще раз печатаю словарь, чтобы проверить, что все на месте
        if not self.priority_queue:
            return None

        for i in range(len_):
            if self.priority_queue[i]:
                value = self.priority_queue[i][0]
                del self.priority_queue[i][0]
                print(self.priority_queue) # печатаю словарь
                print(value) # печатаю значение элемента, который уходит из очереди
                return value

    def peek(self, ind: int = 0, priority: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param priority:
        :param ind: index of element (count from the beginning)
        :return: peeked element
        """
        value = self.priority_queue[priority][ind]
        return value

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        self.priority_queue.clear()
        return None


# q = PriorityQueue()
# q.enqueue(3)
# q.dequeue()
