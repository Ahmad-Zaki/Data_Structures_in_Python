import pytest
from Implementations.LinkedLists import DoublyLL, Node, SinglyLL


class TestNode:
    def test_repr(self) -> None:
        a = Node("a")
        b = Node()
        assert repr(a) == "Node(a)"
        assert repr(b) == "Node(None)"

    def test_equality(self) -> None:
        node = Node()
        node_1 = Node(1)
        node_2 = Node(2)
        node_a = Node("a")

        assert node == Node()
        assert node_1 == Node(1)
        assert node_1 != 1
        assert node_1 != node_a
        assert node_1 != node_2


class TestSinglyLL:
    def test_repr(self) -> None:
        empty_sll = repr(SinglyLL())
        filled_sll = repr(SinglyLL([1, "a", 2.5]))
        assert (
            empty_sll == ""
        ), f"repr output ('{empty_sll}') doesn't match expected output ('')"
        assert (
            filled_sll == "1->a->2.5"
        ), f"repr output ('{filled_sll}') doesn't match expected output ('1->a->2.5')"

    def test_len(self) -> None:
        lst = SinglyLL([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        assert len(lst) == 10, f"list length should be 10, not {len(lst)}"

        lst.pop()
        assert len(lst) == 9, f"list length should be 9, not {len(lst)}"

        lst.insert(10)
        assert len(lst) == 10, f"list length should be 10, not {len(lst)}"

        empty_lst = SinglyLL()
        assert len(empty_lst) == 0, f"list length should be 0, not {len(lst)}"

        empty_lst.insert(1)
        assert len(empty_lst) == 1, f"list length should be 1, not {len(lst)}"

        empty_lst.pop()
        assert len(empty_lst) == 0, f"list length should be 0, not {len(lst)}"
