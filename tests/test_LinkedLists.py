import pytest
from Implementations.LinkedLists import Node, SinglyLL


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

    def test_pop(self) -> None:
        lst = SinglyLL()

        assert (
            lst.pop() == lst
        ), "popping from an empty list should return the same list without modification"

        lst.insert(1).pop(0)
        assert (
            lst.head is lst.tail is None
        ), f"lst must be empty after pop, instead head is {lst.head} and tail is {lst.tail}"

        for i in [1, 2, 3, 4, 5]:
            lst.insert(i)

        lst.pop(0)
        assert lst.head == Node(2), f"new head node must be Node(2), not {lst.head}"

        lst.pop()
        assert lst.tail == Node(4), f"new tail node must be Node(4), not {lst.tail}"
        assert lst.tail.next is None, f"tail.next should be None, not {lst.tail.next}"

        lst.pop(1)
        assert lst.head.next == lst.tail

        for i in [2.5, -7.8, "a"]:
            error_msg = f"Invalid type {type(i)}. Index must be int"
            with pytest.raises(TypeError, match=error_msg):
                lst.pop(i)

        for i in [2, 3, 4, 5]:
            error_msg = f"Index out of bound, please specify an index between 0 and {len(lst)-1}"
            with pytest.raises(IndexError, match=error_msg):
                lst.pop(i)

        # Test circular list:
        circular_lst = SinglyLL([1, 2, 3, 4, 5], circular=True)

        circular_lst.pop(0)
        assert circular_lst.head == Node(
            2
        ), f"new head node must be Node(2), not {circular_lst.head}"

        circular_lst.pop()
        assert circular_lst.tail == Node(
            4
        ), f"new tail node must be Node(4), not {circular_lst.tail}"
        assert (
            circular_lst.tail.next == circular_lst.head
        ), f" tail.next should refer to head ({circular_lst.head}, not {circular_lst.tail.next})"

    def test_remove(self) -> None:
        lst = SinglyLL()

        assert (
            lst.remove(1) == lst
        ), "removing from an empty list should return the same list without modification"

        lst = SinglyLL([1])
        lst.remove(1)
        assert (
            lst.head is lst.tail is None
        ), f"empty list head and tail must be None, not {lst.head} or {lst.tail}"

        lst = SinglyLL([1, 2, 3, 4, 5])

        lst.remove(1)
        assert lst.head == Node(2), f"new head node must be Node(2), not {lst.head}"

        lst.remove(5)
        assert lst.tail == Node(4), f"new tail node must be Node(4), not {lst.tail}"
        assert lst.tail.next is None, f"tail.next should be None, not {lst.tail.next}"

        lst.remove(3)
        assert len(lst) == 2, f"list length should be 2, not {len(lst)}"

        for i in [1, 3, 5, "a", 12, -2, -4]:
            error_msg = f"'{i}' does not exists in the list."
            with pytest.raises(ValueError, match=error_msg):
                lst.remove(i)

        # Test circular list:
        circular_lst = SinglyLL([1, 2, 3, 4, 5], circular=True)

        circular_lst.remove(1)
        assert circular_lst.head == Node(
            2
        ), f"new head node must be Node(2), not {circular_lst.head}"

        circular_lst.remove(5)
        assert circular_lst.tail == Node(
            4
        ), f"new tail node must be Node(4), not {circular_lst.tail}"
        assert (
            circular_lst.tail.next == circular_lst.head
        ), f" tail.next should refer to head ({circular_lst.head}, not {circular_lst.tail.next})"

    def test_delete(self) -> None:
        lst = SinglyLL([1, 2, 3, 4, 5, 6])
        circular_lst = SinglyLL([1, 2, 3, 4, 5, 6, 7, 8])

        lst.delete()
        circular_lst.delete()

        assert (
            lst.head is lst.tail is None
        ), f"list head and tail must be None, not {lst.head} or {lst.tail}"
        assert len(lst) == 0, f"list length must be 0, not {len(lst)}"

        assert (
            circular_lst.head is circular_lst.tail is None
        ), f"list head and tail must be None, not {circular_lst.head} or {circular_lst.tail}"
        assert len(circular_lst) == 0, f"list length must be 0, not {len(circular_lst)}"

    def test_iteration(self) -> None:
        elements = [1, 2, 3, 4, 5, 6, 7, 8]
        lst = SinglyLL(elements)
        circular_lst = SinglyLL(elements)

        for node, val in zip(lst, elements):
            assert node.data == val

        for node, val in zip(circular_lst, elements):
            assert node.data == val

    def test_getitem(self) -> None:
        vals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        lst = SinglyLL(vals)
        circular_lst = SinglyLL(vals, circular=True)

        for l in [lst, circular_lst]:
            for i in range(-10, 10):
                assert l[i].data == vals[i]

            for i in range(10, 15):
                error_msg = f"Index out of bound, please specify an index between 0 and {len(lst)-1}"
                with pytest.raises(IndexError, match=error_msg):
                    l[i]

            for i in [1.5, -8.5, -12.5, "a"]:
                error_msg = f"Invalid type {type(i)}. Index must be int"
                with pytest.raises(TypeError, match=error_msg):
                    l[i]

    def test_contains(self) -> None:
        vals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        lst = SinglyLL(vals)
        circular_lst = SinglyLL(vals, circular=True)

        for l in [lst, circular_lst]:
            for i in vals:
                assert i in l

            for i in [-1, -2, "a", "b", "c"]:
                assert i not in l

