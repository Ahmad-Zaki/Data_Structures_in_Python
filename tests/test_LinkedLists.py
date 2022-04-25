from Implementations.LinkedLists import Node


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
