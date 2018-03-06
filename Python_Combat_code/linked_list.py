# coding=utf-8
'''
数据结构:链表
'''


class Node():
    def __init__(self, element, the_next=None):
        self._el = element
        self.next = the_next

    @property
    def element(self):
        return self._el


class LinkedList():
    def __init__(self):
        self._head = None
        self._size = 0

    # 集合方法
    def __len__(self):
        return self._size

    def get_head(self):
        return self._head

    def is_empty(self):
        return self._size == 0

    def add_first(self, element):
        newest = Node(element)
        newest.next = self._head
        self._head = newest
        self._size = self._size + 1

    def add_last(self, element):
        newest = Node(element)
        newest.last = None
        tail = self.find_tail()
        if tail is None:
            self._head = newest
        else:
            tail.next = newest
        self._size = self._size + 1

    def find_tail(self):
        if self._head is None:
            return None
        else:
            tmp = self._head
            while tmp.next:
                tmp = tmp.next
            return tmp

    def remove_first(self):
        if self._head is None:
            raise ('List is empty')
        else:
            tmp = self._head
            self._head = self._head.next
            return tmp.element

    # zero based

    def get(self, index):
        if index < 0 or index > self._size:
            raise ('Index out of range')
        else:
            tmp = self._head
            while index > 0:
                tmp = tmp.next
                index = index - 1
            return tmp.element
