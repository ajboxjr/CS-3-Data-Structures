#!python

from linkedlist import LinkedList


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):
    # Bottom [7],[6],[5],[4],[3],[2],[1] Top
    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # TODO: Check if empty
        return self.length() is 0

    def length(self):
        """Return the number of items in this stack."""
        # TODO: Count number of items
        return self.list.size

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) – Add to the head of the stack"""
        # TODO: Push given item
        self.list.prepend(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty. O(1) """
        # TODO: Return top item, if any
        top = self.list.head
        if self.is_empty():
            return None
        else:
            return top.data

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) – Removing first element from the top of stack"""
        # TODO: Remove and return top item, if any
        top = self.list.head
        if self.is_empty():
            raise ValueError('No items in the list')
        else:
            return self.list.delete(top.data)



# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # TODO: Check if empty
        return self.length() is 0

    def length(self):
        """Return the number of items in this stack."""
        # TODO: Count number of items
        return len(self.list)

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) – Insert element to the first index of the array"""
        # TODO: Insert given item
        self.list.insert(0,item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # TODO: Return top item, if any
        if self.is_empty():
            return None
        else:
            return self.list[0]


    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) – remove 1st element at the top of stack"""
        # TODO: Remove and return top item, if any
        if self.is_empty():
            raise ValueError
        else:
            return self.list.pop(0)
# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
Stack = LinkedStack
#Stack = ArrayStack
