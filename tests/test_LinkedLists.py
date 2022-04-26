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

    def test_insert(self) -> None:
        # Non circular list:
        lst = SinglyLL(circular=False)
        assert (
            lst.head is lst.tail is None
        ), f"head and tail must be None, not {lst.head} or {lst.tail}"

        lst.insert("a")
        assert (
            lst.head == lst.tail == Node("a")
        ), f"head and tail must be Node(a), not {lst.head} or {lst.tail}"

        lst.insert("b")
        assert lst.head == Node("a"), f"head must be Node(a), not {lst.head}"
        assert lst.tail == Node("b"), f"tail must be Node(b), not {lst.tail}"
        assert (
            lst.head.next == lst.tail
        ), f"head.next must be {lst.tail}, not {lst.head.next}"
        assert lst.tail.next == None, f"tail.next must be None, not {lst.tail.next}"

        lst.insert(1, 0)
        assert lst.head == Node(1), f"head must be Node(1), not {lst.head}"
        assert lst.head.next == Node("a"), f"head must be Node(a), not {lst.head}"

        lst.insert(5, 2)
        assert (
            lst[-2].next == lst.tail
        ), f"inserted_node.next must be {lst.tail}, not {lst[-2].next}"

        lst.insert(-5.5, 1)
        assert lst.head.next == Node(
            -5.5
        ), f"head.next must be Node(-5.5), not {lst.head.next}"

        for i in [2.5, -7.8, "a"]:
            error_msg = f"Invalid type {type(i)}. Index must be int"
            with pytest.raises(TypeError, match=error_msg):
                lst.insert("foo", i)

        for i in [-1, -10, 6, 12]:
            error_msg = (
                f"index out of bound, please specify an index between 0 and {len(lst)}"
            )
            with pytest.raises(IndexError, match=error_msg):
                lst.insert("foo", i)

        # Circular list:
        circular_lst = SinglyLL(circular=True)

        for i in [1, 2, 3]:
            circular_lst.insert(i)
            assert (
                circular_lst.tail.next == circular_lst.head
            ), f"tail.next must be the list head ({lst.head}, not {lst.tail.next})"
