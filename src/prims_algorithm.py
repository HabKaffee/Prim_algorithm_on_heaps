'''
File contains implementations of different Prim's algorithms for MST search
'''
from src.binary_heap import BinaryHeap
from src.fibonacci_heap import FibonacciHeap

def prim_algorith_on_labels(graph):
    '''Naive implementation of Prim's algorithm for MST'''
    start_vertex = 0
    label = [0] * len(graph)
    length_projections = [float("inf")] * len(graph)
    second_ends = [len(graph)]*len(graph)
    mst = []

    label[start_vertex] = 1
    for neighbour in graph[start_vertex]:
        length_projections[neighbour[0]] = neighbour[1]
        second_ends[neighbour[0]] = start_vertex

    while len(mst) < (len(graph) - 1):
        min_value = float('inf')
        next_vertex = None
        for vert, weight in enumerate(length_projections):
            if label[vert] == 0 and weight < min_value:
                next_vertex = vert
                min_value = weight

        label[next_vertex] = 1
        mst.append((second_ends[next_vertex], next_vertex, min_value))
 
        for neighbour in graph[next_vertex]:
            if label[neighbour[0]] == 0:
                if length_projections[neighbour[0]] > neighbour[1]:
                    length_projections[neighbour[0]] = neighbour[1]
                    second_ends[neighbour[0]] = next_vertex
    return mst

def prim_algorith_on_binary_heap(graph):
    '''Prim's algorithm using binary heap'''
    start_vertex = 0
    label = [0] * len(graph)
    length_projections = BinaryHeap(weight_array=[float("inf")] * len(graph), vertex_array=None)
    second_ends = [len(graph)]*len(graph)
    mst = []

    label[start_vertex] = 1
    length_projections.delete_min_vertex()

    for neighbour in graph[start_vertex]:
        index = length_projections.vertex_array.index(neighbour[0])
        length_projections.decrease_weight(index, neighbour[1])
        second_ends[neighbour[0]] = start_vertex

    while len(mst) < (len(graph) - 1):
        next_vertex = length_projections.vertex_array[0]
        min_weight = length_projections.weight_array[0]
        mst.append((second_ends[next_vertex], next_vertex, min_weight))

        label[next_vertex] = 1
        length_projections.delete_min_vertex()

        for neighbour in graph[next_vertex]:
            if label[neighbour[0]] == 0:
                index = length_projections.vertex_array.index(neighbour[0])
                if length_projections.weight_array[index] > neighbour[1]:
                    length_projections.decrease_weight(index, neighbour[1])
                    second_ends[neighbour[0]] = next_vertex
    return mst

def prim_algorith_on_fibonacci_heap(graph):
    '''Prim's algorighm using Fibonacci heap'''
    start_vertex = 0
    label = [0]*len(graph)
    length_projections = FibonacciHeap()

    nodes_list = []

    for vertex in graph.keys():
        if vertex != 0:
            nodes_list.append(length_projections.insert(float('inf'), vertex))
        else:
            nodes_list.append(length_projections.insert(0, vertex))

    second_ends = [len(graph)]*len(graph)
    mst = []

    label[start_vertex] = 1
    length_projections.delete_min()

    for neighbour in graph[start_vertex]:

        length_projections.decrease_key(nodes_list[neighbour[0]], neighbour[1])
        second_ends[neighbour[0]] = start_vertex

    while len(mst) < (len(graph) - 1):

        next_vertex = length_projections.find_min()

        label[next_vertex.value] = 1
        length_projections.delete_min()

        mst.append((second_ends[next_vertex.value], next_vertex.value, next_vertex.key))

        for neighbour in graph[next_vertex.value]:
            if label[neighbour[0]] == 0:
                index = neighbour[0]
                if nodes_list[index].key > neighbour[1]:
                    length_projections.decrease_key(nodes_list[neighbour[0]], neighbour[1])
                    second_ends[neighbour[0]] = next_vertex.value
    return mst
