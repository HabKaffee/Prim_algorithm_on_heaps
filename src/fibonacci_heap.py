'''This file contains implementation of Fibonacci heap with all required objects'''

from numpy import log2


class FibonacciHeap:
    '''Fibonacci heap implementation'''
    class Node:
        '''Fibonacci heap node'''
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.parent = None
            self.child = None
            self.left = self
            self.right = self
            self.degree = 0
            self.marked = False

    def __init__(self):
        self.min = None
        self.num_of_nodes = 0

    def find_min(self):
        '''Returns heap minimum element in O(1) time'''
        return self.min

    def insert(self, key, value=None):
        '''Inserts new node to the heap in O(1) time'''
        n = self.Node(key, value)

        if self.num_of_nodes == 0:
            self.min = n
        else:
            self.add_root(n)

        self.num_of_nodes += 1

        return n

    # O(log n)
    def delete(self, node):
        '''Provides element deletion by decreasing key of min element and deleting min'''
        self.decrease_key(node, self.min.key - 1)
        self.delete_min()

    # O(log n)
    def delete_min(self):
        '''Deletes minumum element'''
        prev_min = self.min
        if prev_min is None:
            return prev_min
        # move children to root
        if prev_min.child is not None:
            n = stop = prev_min.child
            first_loop = True
            while first_loop or n != stop:
                first_loop = False
                next_node = n.right
                self.add_node_left(n, self.min)
                n.parent = None
                n = next_node

        if self.min.right != self.min:
            self.min = prev_min.right
            self.remove_node(prev_min)
            self.consolidate()
        # no nodes left
        else:
            start_for_newmin = prev_min.right
            self.remove_node(prev_min)
            self.find_new_min(start_for_newmin)

        self.num_of_nodes -= 1
        return prev_min

    def find_new_min(self, start_for_newmin):
        '''Find new mininum element'''
        node = stop = start_for_newmin
        flag = False
        min_value = float('inf')
        while True:
            if node == stop and flag is True:
                break
            elif node == stop:
                flag = True
            if node.key < min_value:
                self.min = node
                min_value = node.key
            node = node.right


    def consolidate(self):
        '''Make the degrees of root elements unique, fibonacci sequence'''
        degree_arr = [None for _ in range(int(log2(self.num_of_nodes)) + 2)]
        root_items = self.layer_as_list(self.min)
        for n in root_items:

            degree = n.degree
            # combine nodes until no same root degrees exists
            while degree_arr[degree] is not None:
                m = degree_arr[degree]
                # make sure that n is always smaller
                if m.key < n.key:
                    n, m = self.swap_vars(n, m)
                self.remove_node(m)
                self.add_child(m, n)
                degree_arr[degree] = None
                degree += 1

            degree_arr[degree] = n

        self.update_root_min()

    def update_root_min(self):
        '''Updates minimum element to lowest value from the root'''
        top = self.find_root_item()
        root_layer = self.layer_as_list(top)
        self.min = min(root_layer, key=lambda n: n.key)

    def find_root_item(self):
        '''Returns an item from root layer'''
        top_item = self.min
        while top_item.parent is not None:
            top_item = top_item.parent
        return top_item

    # O(1)
    def decrease_key(self, node, new_key):
        '''Changes node key to new_key'''

        node.key = new_key
        parent = node.parent

        # root element, simple case
        if parent is None:
            if node.key < self.min.key:
                self.min = node
        elif node.key < parent.key:
            self.cut(node)
            self.cascading_cut(parent)

        return node

    def cut(self, node):
        '''Moves the node root level'''
        parent = node.parent
        parent.degree -= 1

        # if parent has only 1 child
        if parent.child == node and node.right == node:
            parent.child = None
            self.remove_node(node)
        else:
            parent.child = node.right
            self.remove_node(node)

        # add to the root level
        node.marked = False
        self.add_node_left(node, self.min)
        if node.key < self.min.key:
            self.min = node

    def cascading_cut(self, node):
        '''Reorganizes the heap to keep in optimal form'''
        parent = node.parent
        if parent is not None:
            if parent.marked:
                self.cut(node)
                self.cascading_cut(parent)
            else:
                parent.marked = True

    def merge(self, heap):
        '''Merges two heaps in O(1) time'''
        assert isinstance(heap, FibonacciHeap)

        # if either of heaps is empty
        if heap.min is None:
            return
        if self.min is None:
            self.min = heap.min
            return
        first = self.min
        last = self.min.right
        second = heap.min
        second_last = heap.min.left

        first.right = second
        second.left = first
        last.left = second_last
        second_last.right = last

        self.num_of_nodes += heap.num_of_nodes
        if heap.min.key < self.min.key:
            self.min = heap.min

    def add_node_left(self, node, right_node):
        '''add node to left side of given right node'''
        node.right = right_node
        node.left = right_node.left
        right_node.left.right = node
        right_node.left = node

    def add_root(self, node):
        '''Adds node to the left side of minumum element'''
        self.add_node_left(node, self.min)
        if node.key < self.min.key:
            self.min = node

    def add_child(self, child, parent):
        '''Adds child to another node'''
        if parent.child is None:
            parent.child = child
            child.parent = parent
        else:
            self.add_node_left(child, parent.child)
            child.parent = parent
        parent.degree += 1

    def swap_vars(self, var1, var2):
        '''Swaps variables'''
        return (var2, var1)

    # Remove element from the double linked list
    def remove_node(self, node):
        '''Remove element from the doubly linked list'''
        node.left.right = node.right
        node.right.left = node.left
        node.left = node
        node.right = node
        node.parent = None

    def layer_as_list(self, node):
        '''
        Return the whole layer as a list.
        input -> one node in the layer
        outout -> layer
        '''
        items = []
        n = stop = node
        first_loop = True
        while first_loop or n != stop:
            first_loop = False
            items.append(n)
            n = n.right
        return items
