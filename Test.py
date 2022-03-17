dict_ = {"a": 1}

print(dict_)
print(dict_.keys())
print(list(dict_))

# def game(N, K):
#     start_human_list = {human: True for human in range(N)}
#
#     def _game(human_list):
#         if len(human_list) == 1:
#             return list(human_list)
#
#         human_list[K - 1] = False
#         new_human_list = {key: value for key, value in human_list.items() if value == True}
#
#         return _game(new_human_list)
#
#     return _game(start_human_list)

N = 5
K = 3
start_human_list = {human: True for human in range(N)}

print(start_human_list)

start_human_list[K - 1] = False

print(start_human_list)

new_human_list = {key: value for key, value in start_human_list.items() if value == True}

print(new_human_list)

new_human_list[K - 1] = False
print(new_human_list)
new_human_list = {key: value for key, value in start_human_list.items() if value == True}
print(new_human_list)


N = 5
K = 2

start_human_list = [human for human in range(N)]
stack = []

start_human_list[K]
stack.append(start_human_list[K + 1])
new_start = stack.pop()
new_human_list = start_human_list[new_start:] + start_human_list[:K]

print(new_start)
print(new_human_list)
print(len(new_human_list))

from collections import deque

queue = []

list_ = [1, 2, 3, 4, 5]
i = 0
def _game(human_list):
    while True:
        queue.append(list_[i])
        print(queue)
        list_.append(queue.pop())
        print(list_)
        i += 1
        if i == 2:
            new_list = list_[i + 1:]
            print(new_list)
            break


