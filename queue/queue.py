class Node:
    def __init__(self, value=None, next_node=None):
        # set value at this node
        self.value = value
        # set ref to the next node in the chain
        self.next_node = next_node

    # get the value of current node
    def get_value(self):
        return self.value

    # get the ref to the next node in the chain
    def get_next(self):
        return self.next_node

    # set the ref to the next node in the chain
    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # set initial ref to head
        self.head = None
        # set initial rer to tail
        self.tail = None

    def add_to_tail(self, value):
        # wrap the val inside a node
        new_node = Node(value, None)
        # 1. the lists empty
        if not self.head:
            # check if no head
            # set head and tail to new node
            self.head = new_node
            self.tail = new_node
        # 2. if not empty
        else:
            # add a new node to the tail
            self.tail.set_next(new_node)
            # set tails next ref to our new node
            self.tail = new_node

    def remove_head(self):
        # return None if there is no head (empty List)
        if not self.head:
            return None
        # if single node list
        if not self.head.get_next():
            # get ref to head
            head = self.head
            # del head from list
            self.head = None
            # del tail from list
            self.tail = None
            # return the head to the caller
            return head.get_value()

        # otherwise store value
        value = self.head.get_value()
        # set heads ref to current heads next node in the list
        self.head = self.head.get_next()
        return value

    def contains(self, value):
        if not self.head:
            return False

        # get ref to node we are currently at; update as we traverse list
        current = self.head

        # check to see if valid node
        while current:
            # if current node matches return true
            if current.get_value() == value:
                return True

            # update our current node to the next node in the list
            current = current.get_next()
        # if we are here. then the target value is not in the list
        return False


class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?

        self.storage = LinkedList()

    def enqueue(self, item):
        self.storage.add_to_tail(item)
        self.size += 1
    
    def dequeue(self):
        head_removed = self.storage.remove_head()
        if head_removed == None:
            return None
        else:
            self.size -= 1
            return head_removed

    def len(self):
        return self.size
