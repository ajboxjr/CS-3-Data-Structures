
#!python


class BinaryTreeNode(object):

    def __init__(self, data):
        """Initialize this binary tree node with the given data."""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r})'.format(self.data)

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        # TODO: Check if both left child and right child have no value
        return self.left == None and self.right == None

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        # TODO: Check if either left child or right child has a value
        return self.left != None or self.right != None

    def height(self):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node).
        TODO: Best and worst case running time: ??? under what conditions?"""
        max_height = 0

        #Base Case
        node = self
        if node: # if node exists
            #Base Case
            if node.is_leaf(): # has no left & right
                print("leaf: {}: {}".format(node, max_height))
                return max_height

            elif node.is_branch: # has left or right
                #add to height for branches
                max_height +=1
                left_height = 0
                right_height = 0
                if node.left:
                    left_height = node.left.height()
                if node.right:
                    right_height = node.right.height()

                print("parent {} (left: {} h:{}) (right {} h:{})".format(node, node.left, left_height, node.right, right_height))
                if left_height > right_height: # choose the longer height (left)
                    node = node.left
                    max_height +=left_height
                elif left_height < right_height:
                    node = node.right
                    max_height += right_height
                else:
                    max_height += right_height# equal so chose on to return
        return max_height
        # TODO: Check if left child has a value and if so calculate its height
        ...
        # TODO: Check if right child has a value and if so calculate its height
        ...
        # Return one more than the greater of the left height and right height
        ...


class BinarySearchTree(object):

    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items."""
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this binary search tree is empty (has no nodes)."""
        return self.root is None

    def height(self):
        """Return the height of this tree (the number of edges on the longest
        downward path from this tree's root node to a descendant leaf node).
        TODO: Best and worst case running time:
        Worst: O(logn) TODO
        Best: O(1) 1 node under tree under what conditions?"""
        # TODO: Check if root node has a value and if so calculate its height
        if self.is_empty is True:
            return 0
        else:
            return self.root.height()

    def contains(self, item):
        """Return True if this binary search tree contains the given item.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Find a node with the given item, if any
        node = self._find_node(item)
        # Return True if a node was found, or False
        return node is not None

    def search(self, item):
        """Return an item in this binary search tree matching the given item,
        or None if the given item is not found.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Find a node with the given item, if any
        node = self._find_node(item)
        # TODO: Return the node's data if found, or None
        return node.data if node else None



    def insert(self, item):
        """Insert the given item in order into this binary search tree.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Handle the case where the tree is empty
        if self.is_empty():
            # TODO: Create a new root node
            self.root = BinaryTreeNode(item)
            # TODO: Increase the tree size
            self.size +=1
            return
        # Find the parent node of where the given item should be inserted
        parent = self._find_parent_node(item)

        if parent:
            # TODO: Check if the given item should be inserted left of parent node
            if parent.data > item:
                parent.left = BinaryTreeNode(item)
            # TODO: Create a new node and set the parent's left child
            # TODO: Check if the given item should be inserted right of parent node
            if parent.data < item:
                parent.right = BinaryTreeNode(item)
                # TODO: Create a new node and set the parent's right child
            # TODO: Increase the tree size
        else:
            if self.root is not None:
                if self.root.data > item:
                    self.root.left = BinaryTreeNode(item)
            if self.root is not None:
                if self.root.data < item:
                    self.root.right =  BinaryTreeNode(item)
        self.size +=1

    def _find_node(self, item):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Start with the root node
        assert type(item) == type(self.root.data)
        node = self.root
        # Loop until we descend past the closest leaf node
        while node is not None:
            # TODO: Check if the given item matches the node's data
            if node.data == item:
                # Return the found node
                return node
            # TODO: Check if the given item is less than the node's data
            elif node.data > item:
                node = node.left
            elif node.data < item:
                node = node.right
        return None

    def _find_parent_node(self, item):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Start with the root node and keep track of its parent
        node = self.root
        parent = None
        # Base God Says don't touch this
        # if node is None:
        #     return parent
        # Loop until we descend past the closest leaf node

        while node is not None:
            # TODO: Check if the given item matches the node's data
            if node.data == item:
                # Return the parent of the found node
                return parent
            # TODO: Check if the given item is less than the node's data
            # if node.left is not None:
            elif node.data > item:
                # TODO: Update the parent and descend to the node's left child
                parent = node           #   O
                node = node.left        #  / \ IF left is None
                                        # O   O
            # TODO: Check if the given item is greater than the node's data
            # elif node.right is not None:
            elif node.data < item:
                # TODO: Update the parent and descend to the node's right child
                parent = node
                node = node.right
        return parent

    # This space intentionally left blank (please do not delete this comment)

    def items_in_order(self):
        """Return an in-order list of all items in this binary search tree."""
        pass
        items = []
        if not self.is_empty():
            # Traverse tree in-order from root, appending each node's item
            self._traverse_in_order_recursive(self.root, items.append)
        # Return in-order list of all items in tree
        return items

    def _traverse_in_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        #if it is a leaf append(visit)
        #else: check recursive left then right
        if node:
            if node.is_leaf():
                return visit(node.data)
            if node.is_branch():
                self._traverse_in_order_recursive(node.left, visit)
                visit(node.data)
                self._traverse_in_order_recursive(node.right, visit)
        # TODO: Traverse left subtree, if it exists
        ...
        # TODO: Visit this node's data with given function
        ...
        # TODO: Traverse right subtree, if it exists
        ...

    # def _traverse_in_order_iterative(self, node, visit):
    #     """Traverse this binary tree with iterative in-order traversal (DFS).
    #     Start at the given node and visit each node with the given function.
    #     TODO: Running time: ??? Why and under what conditions?
    #     TODO: Memory usage: ??? Why and under what conditions?"""
    #     # TODO: Traverse in-order without using recursion (stretch challenge)
    #     while node:
    #
    #         if node.is_branch():
    #             if node.left is not None:


    def items_pre_order(self):
        """Return a pre-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree pre-order from root, appending each node's item
            self._traverse_pre_order_recursive(self.root, items.append)
        # Return pre-order list of all items in tree
        return items

    def _traverse_pre_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        if node:
            visit(node.data)
            self._traverse_pre_order_recursive(node.left, visit)
            self._traverse_pre_order_recursive(node.right, visit)


        # TODO: Visit this node's data with given function
        ...
        # TODO: Traverse left subtree, if it exists
        ...
        # TODO: Traverse right subtree, if it exists
        ...

    def _traverse_pre_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse pre-order without using recursion (stretch challenge)

    def items_post_order(self):
        """Return a post-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree post-order from root, appending each node's item
            self._traverse_post_order_recursive(self.root, items.append)
        # Return post-order list of all items in tree
        return items

    def _traverse_post_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse left subtree, if it exists
        if node:
            self._traverse_post_order_recursive(node.left,visit)
            self._traverse_post_order_recursive(node.right, visit)
            visit(node.data)
        # TODO: Traverse right subtree, if it exists
        ...
        # TODO: Visit this node's data with given function
        ...

    def _traverse_post_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse post-order without using recursion (stretch challenge)

    # def items_level_order(self):
    #     """Return a level-order list of all items in this binary search tree."""
    #     items = []
    #     if not self.is_empty():
    #         # Traverse tree level-order from root, appending each node's item
    #         self._traverse_level_order_iterative(self.root, items.append):
    #     # Return level-order list of all items in tree
    #     return items

    def _traverse_level_order_iterative(self, start_node, visit):
        """Traverse this binary tree with iterative level-order traversal (BFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Create queue to store nodes not yet traversed in level-order
        queue = ...
        # TODO: Enqueue given starting node
        ...
        # TODO: Loop until queue is empty
        while ...:
            # TODO: Dequeue node at front of queue
            node = ...
            # TODO: Visit this node's data with given function
            ...
            # TODO: Enqueue this node's left child, if it exists
            ...
            # TODO: Enqueue this node's right child, if it exists
            ...


def test_binary_search_tree():
    # Create a complete binary search tree of 3, 7, or 15 items in level-order
    # items = [2, 1, 3]
    # items = [4, 2, 6, 1, 3, 5, 7]

    items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    # items = ['h','d','i','b','e','a','f','c','j','g']
    # items = ['B','A','C']
    print('items: {}'.format(items))

    tree = BinarySearchTree()
    print('tree: {}'.format(tree))
    print('root: {}'.format(tree.root))

    print('\nInserting items:')
    for item in items:
        tree.insert(item)
        print('insert({}), size: {}'.format(item, tree.size))
    print(tree.height())
    print('root: {} left: {} right: {}'.format(tree.root.data, tree.root.left,tree.root.right ))


    print('\nSearching for items:')
    for item in items:
        result = tree.search(item)
        print('search({}): {}'.format(item, result))
    # item = 123
    # result = tree.search(item)
    print('search({}): {}'.format(item, result))
    #
    # print('\nTraversing items:')
    print('items in-order:    {}'.format(tree.items_in_order()))
    print('items pre-order:   {}'.format(tree.items_pre_order()))
    print('items post-order:  {}'.format(tree.items_post_order()))
    # print('items level-order: {}'.format(tree.items_level_order()))


if __name__ == '__main__':
    test_binary_search_tree()
