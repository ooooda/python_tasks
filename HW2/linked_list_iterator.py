class MyLinkedList:
    class Node:
        def __init__(self, prev, nxt, val):
            self.val = val
            self.nxt = nxt
            self.prev = prev

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = self.Node(None, None, None)
        self.tail = self.Node(self.head, None, None)
        self.head.nxt = self.tail
        self.cur = self.head

    def __iter__(self):
        self.cur = self.head
        return self

    def __next__(self):
        nxt = self.cur.nxt
        if nxt != self.tail:
            self.cur = nxt
            return nxt.val
        raise StopIteration

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        node = self._get_node(index)
        if node is None or node == self.tail:
            return -1
        return node.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        cur = self.head.nxt
        add = self.Node(self.head, cur, val)
        cur.prev = add
        self.head.nxt = add

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        cur = self.tail.prev
        add = self.Node(cur, self.tail, val)
        cur.nxt = add
        self.tail.prev = add

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        node = self._get_node(index)
        if node is None:
            return
        prev = node.prev
        add = self.Node(prev, node, val)
        prev.nxt = add
        node.prev = add

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        node = self._get_node(index)
        if node is None or node == self.tail:
            return
        prev = node.prev
        nxt = node.nxt
        prev.nxt = nxt
        nxt.prev = prev

    def _get_node(self, index):
        cur = self.head.nxt
        cnt = 0
        while cur is not None:
            if cnt == index:
                return cur
            cnt += 1
            cur = cur.nxt
        return None


if __name__ == "__main__":
    lst = MyLinkedList()
    lst.addAtTail(3)
    lst.addAtTail(5)
    lst.addAtTail(7)

    print(next(lst))
    print(next(lst))
    print(next(lst))
    print('-----')
    for num in lst:
        print(num)
