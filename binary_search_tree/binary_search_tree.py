class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Check new node val < current nodes val
        if value < self.value:
            # if no left child place new node
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                # otherwise repeat process
                self.left.insert(value)
        # check new node val >= current nodes val
        if value >= self.value:
            # if no right child place new node
            if not self.right:
                self.right = BinarySearchTree(value)
            # otherwise repeat process
            else:
                self.right.insert(value)

    def contains(self, target):
        # import pdb
        # pdb.set_trace()
        if self.value == target:
            return True
        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        else:
            if self.right:
                return self.right.contains(target)
            else:
                return False

    # returns None which is a falsy expression
    # def contains(self, target):
    #     if target == self.value:
    #         return True
    #     if target < self.value:
    #         if self.left:
    #             return self.left.contains(target)
    #     else:
    #         if self.right:
    #             return self.right.contains(target)

    def get_max(self):
        if self.right != None:
            return self.right.get_max()
        else:
            return self.value

    def for_each(self, cb):
        cb(self.value)
        if self.left != None:
            self.left.for_each(cb)
        if self.right != None:
            self.right.for_each(cb)


# OK so with 'contains' and 'get_max' the tests are expecting something back
# so the recursive function needs to return when it calls itself
# to spit out whatever from the nested loops

# insert and for_each are just modifying the tree, tests just
# test that the tree has been modified.
