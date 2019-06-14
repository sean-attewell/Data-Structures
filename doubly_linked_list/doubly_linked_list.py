"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        if self.length == 0:
            self.head = ListNode(value)
            self.tail = self.head
        else:
            self.head.insert_before(value)
            self.head = self.head.prev  # LOOK HERE
        self.length += 1

    def remove_from_head(self):
        removed_head_copy = self.head
        self.head.delete()
        self.length -= 1
        if self.length >= 1:
            self.head = removed_head_copy.next
        else:
            self.head = None
            self.tail = None
        return removed_head_copy.value

    def add_to_tail(self, value):
        if self.length == 0:
            self.tail = ListNode(value)
            self.head = self.tail
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next
        self.length += 1

    def remove_from_tail(self):
        removed_tail_copy = self.tail
        self.tail.delete()
        self.length -= 1
        if self.length >= 1:
            self.tail = removed_tail_copy.prev
        else:
            self.tail = None
            self.head = None
        return removed_tail_copy.value

    def move_to_front(self, node):
        if node == self.head:
            return
        else:
            self.delete(node)
            self.add_to_head(node.value)

    def move_to_end(self, node):
        if node == self.tail:
            return
        else:
            self.delete(node)
            self.add_to_tail(node.value)

    def delete(self, node):
        if self.length == 0:
            return
        if self.length == 1:
            node.delete()
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            if node == self.head:
                self.remove_from_head()
            elif node == self.tail:
                self.remove_from_tail()
            else:
                node.delete()
                self.length -= 1

    def get_max(self):
        current_node = self.head
        max_val = 0
        while current_node:
            if current_node.value > max_val:
                max_val = current_node.value
                current_node = current_node.next
            else:
                current_node = current_node.next
        return max_val
