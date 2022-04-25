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
