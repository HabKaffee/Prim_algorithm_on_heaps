'''This module contains utility functions for MST task'''

from random import randint
import networkx as nx

def get_random_simple_gnp_graph(n, seed=42):
    '''The function generates an undirected unweighted graph as an adjacency list'''
    edge_p = 1/2   ## probability of an edge between vertices 0.5
    g = nx.random_graphs.fast_gnp_random_graph(n,edge_p,seed)
    return nx.convert.to_dict_of_lists(g)

def get_graph(number_of_vertex):
    '''Generation of a weighted undirected graph with edge weights from 1 to 10'''
    graph_without_weights = get_random_simple_gnp_graph(number_of_vertex)
    weighted_graph = {}

    for node in graph_without_weights:
        weighted_graph[node] = {}
        for neighbour in graph_without_weights[node]:
            # Assigning a random weight to an edge
            weighted_graph[node][neighbour] = randint(1, 10)
            # Adding a back edge to an undirected graph
            if neighbour not in weighted_graph:
                weighted_graph[neighbour] = {}
            weighted_graph[neighbour][node] = weighted_graph[node][neighbour]

    for vert in weighted_graph:
        weighted_graph[vert]=list(weighted_graph[vert].items())

    return weighted_graph

def get_number_edges(graph):
    '''Returns number of edges in graph'''
    total_edges = 0
    for vert in graph:
        total_edges += len(graph[vert])
    return int(total_edges/2)

def adjacency_list_to_matrix(graph):
    '''Convert adjacency list representation to adjacency matrix'''
    nodes = list(graph.keys())
    n = len(nodes)
    adjacency_matrix = [[0 for _ in range(n)] for _ in range(n)]

    # Fill the matrix with edge weight values
    for i in range(n):
        node = nodes[i]
        for neighbour, weight in graph[node]:
            adjacency_matrix[i][nodes.index(neighbour)] = weight

    return adjacency_matrix

def test_solution(true_solution, given_solution):
    '''Test provided solution with scipy.sparse.csgraph.minimum_spanning_tree solution'''
    sum_true = sum(sum(row) for row in true_solution.toarray().astype(int))
    sum_given = sum(third for _, _, third in given_solution)
    return sum_true == sum_given
