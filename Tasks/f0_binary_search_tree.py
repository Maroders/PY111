"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, value: 123, 'left': {...}, 'right':{...}})
"""

from typing import Any, Optional, Tuple
# import networkx as nx

root = {'key': 8,  # корневой узел
        'value': 8,
        'left': {
            'key': 3,  # левый потомок
            'value': 3,
            'left': None,
            'right': None
        },
        'right': {
            'key': 10,  # правый потомок
            'value': 10,
            'left': None,
            'right': None
        },
        }


class BinarySearchTree:
    @staticmethod
    def _create_node(key, value: Any, left: Optional[dict] = None, right: Optional[dict] = None):
        """
        Фабричный метод
        :param key: ключ узла
        :param value: значение узла
        :param left: левый узел
        :param right: правый узел
        :return:
        """

        return {
            'key': key,
            'value': value,
            'left': left,
            'right': right
        }

    def __init__(self):
        self.root = None

    def insert(self, key: int, value: Any) -> None:
        """
        Insert (key, value) pair to binary search tree

        :param key: key from pair (key is used for positioning node in the tree)
        :param value: value associated with key
        :return: None
        """
        if self.root is None:
            self.root = self._create_node(key, value)

        else:
            node = self.root
            while True:

                if key > node["key"]:
                    if node["right"] is None:
                        node["right"] = self._create_node(key, value)
                        break
                    else:
                        node = node["right"]

                elif key < node["key"]:
                    if node["left"] is None:
                        node["left"] = self._create_node(key, value)
                        break
                    else:
                        node = node["left"]

                else:
                    node["value"] = value
                    break

    def remove(self, key: int) -> Optional[Tuple[int, Any]]:
        """
        Remove key and associated value from the BST if exists

        :param key: key to be removed
        :return: deleted (key, value) pair or None
        """

        def _remove(deleted_node: Optional[dict]):

            if deleted_node["right"] is None and deleted_node["left"] is None:
                deleted_node_value = deleted_node["value"]
                deleted_node = None
                return deleted_node_value
            if deleted_node["right"] is None or deleted_node["left"] is None:
                insert_node = deleted_node["right"] if deleted_node["right"] is not None else deleted_node["left"]
                deleted_node_value = deleted_node["value"]
                deleted_node = None
                self.insert(insert_node["key"], insert_node["value"])
                return deleted_node_value
            else:
                insert_node = find_min(deleted_node["right"])
                deleted_node_value = deleted_node["value"]
                deleted_node = None
                self.insert(insert_node["key"], insert_node["value"])
                return deleted_node_value

        def find_min(node):
            if node is None:
                return None
            return min(node["key"], find_min(node["right"]), find_min(node["left"]))

        return _remove(self.find(key))

    def find(self, key: int) -> Optional[Any]:
        """
        Find value by given key in the BST

        :param key: key for search in the BST
        :return: value associated with the corresponding key
        """
        def _find(node: Optional[dict]):

            if node is None:  # базовый случай
                raise KeyError()

            if key == node["key"]:
                # return node["value"]
                return node

            # next_node = node["right"] if key > node["key"] else node["left"]
            # return _find(next_node)

            if key > node["key"]:
                return _find(node["right"])

            if key < node["key"]:
                return _find(node["left"])

        return _find(self.root)


    def clear(self) -> None:
        """
        Clear the tree

        :return: None
        """
        self.root = None

if __name__ == '__main__':
    bst = BinarySearchTree()
    # bst.insert(42, 'The meaning of life, the universe and everything.')
    # bst.insert(0, 'ZERO!')
    # bst.insert(13, "Devil's sign here")
    # bst.insert(13, "Oh no, devil's sign again Oo")


    bst.insert(42, "Predictable")
    bst.insert(13, "And again")
    bst.insert(-999, "Nobody expects spanish inquisition!")
    # print(bst.root)
    # print(bst.find(13))
    print(bst.remove(13))
    print(bst.root)
