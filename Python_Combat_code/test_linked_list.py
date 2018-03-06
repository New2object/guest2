import unittest
from Python_Combat_code.linked_list import LinkedList


class LinkedListTestCase(unittest.TestCase):
    def setUp(self):
        self.list = LinkedList()

        self.list.add_first(1)
        self.list.add_first(3)
        self.list.add_first(5)

    def test_is_empty(self):
        tmp_list = LinkedList()
        self.assertTrue(tmp_list.is_empty())

    def test_is_frist(self):
        self.assertEqual(3, len(self.list))
        self.assertEqual(5, self.list.get_head().element)
        self.assertEqual(1, self.list.find_tail().element)

    def test_add_last(self):
        tmp_list = LinkedList()
        tmp_list.add_last(1)
        tmp_list.add_last(3)
        tmp_list.add_last(5)

        self.assertEqual(3, len(self.list))
        self.assertEqual(5, self.list.get_head().element)
        self.assertEqual(1, self.list.find_tail().element)

    def test_remove_first(self):
        self.assertEqual(5, self.list.remove_first())
        self.assertEqual(3, self.list.remove_first())
        self.assertEqual(1, self.list.remove_first())

    def test_get(self):
        self.assertEqual(5, self.list.get(0))
        self.assertEqual(3, self.list.get(1))
        self.assertEqual(1, self.list.get(2))

    def test_find_tail(self):
        self.assertEqual(1, self.list.find_tail().element)

        self.list.add_last(9)
        self.assertEqual(9, self.list.find_tail().element)

        tmp_list = LinkedList()
        self.assertTrue(tmp_list.find_tail() is None)


if __name__ == '__main__':
    unittest.main()
