'''
This file contains binary heap class implementation for Prim's algorithm
'''
from typing import List

class BinaryHeap:
    '''This class contains Binary minheap implementation'''
    def __init__(self, weight_array: List[float], vertex_array: List[int] | None):
        self.weight_array = weight_array
        if vertex_array is None:
            self.vertex_array = list(range(len(self.weight_array)))
        else:
            self.vertex_array = vertex_array


    def swap(self, vertex1: int, vertex2: int):
        '''Swaps two vertices in heap'''
        self.weight_array[vertex1], self.weight_array[vertex2] = self.weight_array[vertex2], self.weight_array[vertex1]
        self.vertex_array[vertex1], self.vertex_array[vertex2] = self.vertex_array[vertex2], self.vertex_array[vertex1]

    def find_parent(self, vertex):
        '''returns parent index for vertex'''
        if vertex == 0:
            return -1
        return (vertex - 1) // 2

    def insert_vertex(self, weight):
        '''Insert new node at the end of the list and call sift_up opetion for new node'''
        self.vertex_array.append(len(self.vertex_array))
        self.weight_array.append(weight)
        self.sift_up(len(self.vertex_array) - 1)

    def sift_up(self, vertex):
        '''Swaps vertex and parent until minheap constraints are satisfied'''
        
        weight_vertex = self.weight_array[vertex]
        name_vertex = self.vertex_array[vertex]
        
        parent = self.find_parent(vertex)
        while (vertex != 0) and (self.weight_array[vertex] < self.weight_array[parent]):
            self.swap(vertex, parent)
            vertex = parent
            parent = self.find_parent(vertex)
        
        self.weight_array[vertex] = weight_vertex
        self.vertex_array[vertex] = name_vertex

    def sift_down(self, vertex):
        '''Swaps min child with parent until minheap constraints are satisfied'''
        heap_size = len(self.vertex_array)
        while (2 * vertex + 1) < heap_size:
            left_child = 2 * vertex + 1
            right_child = 2 * vertex + 2
            min_child = left_child
            if (right_child < heap_size) and self.weight_array[right_child] < self.weight_array[left_child]:
                min_child = right_child
            self.swap(vertex, min_child)
            vertex = min_child

    def decrease_weight(self, vertex, delta):
        '''Decrease weight of vertex by passing non-negative delta'''
        self.weight_array[vertex] -= delta
        self.sift_up(vertex)

    def delete_min_vertex(self):
        '''Delete root of heap'''
        self.swap(0, len(self.vertex_array) - 1)
        self.vertex_array.pop()
        self.weight_array.pop()
        self.sift_down(0)

    def delete_vertex(self, vertex):
        '''Delete arbirtary element by decreasing it's weight to -inf and after delete min'''
        self.decrease_weight(vertex, float('inf'))
        self.delete_min_vertex()
