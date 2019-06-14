class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        i = len(self.storage) - 1
        self._bubble_up(i)

    def delete(self):
        # save max to be delted for returning
        deleted_max = self.storage[0]
        # swap root with the last leaf
        self.storage[0], self.storage[-1] = self.storage[-1], self.storage[0]
        # delete the last leaf
        self.storage.pop()
        # sift
        self._sift_down(0)
        # test wants deleted value returned
        return deleted_max

    def get_max(self):
        if len(self.storage) == 0:
            return None
        else:
            return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        # in worst case elem will need to make way to top of heap
        while index > 0:
            # get parent elem of this index
            parent = (index - 1) // 2
            # check if elem at index is higher priority than parent elem
            if self.storage[index] > self.storage[parent]:
                # if it is then swap them
                self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]

                # update index to be new spot that swapped elem now resides at
                index = parent
            else:
                # otherwise, our elem is at a valid spot in the heap
                # we no longer need to bubble up
                break

    def _sift_down(self, index):
        while index < len(self.storage):
            # get child indexes
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            left_child_value = self.storage[left_child_index] if left_child_index < len(
                self.storage) else None
            right_child_value = self.storage[right_child_index] if right_child_index < len(
                self.storage) else None

            # if no children
            if left_child_value == None and right_child_value == None:
                break

            # if only left child then set left as highest child index
            elif right_child_value == None:
                highest_child_index = left_child_index

            # if only right child then set right as highest child index
            elif left_child_value == None:
                highest_child_index = right_child_index

            # if both children exist, find highest child index
            else:
                if self.storage[left_child_index] > self.storage[right_child_index]:
                    highest_child_index = left_child_index
                else:
                    highest_child_index = right_child_index

            if self.storage[index] >= self.storage[highest_child_index]:
                break
            else:
                self.storage[index], self.storage[highest_child_index] = self.storage[highest_child_index], self.storage[index]
                index = highest_child_index
