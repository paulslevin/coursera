from itertools import combinations
from graph.graphs import make_complete_graph
import random
import matplotlib.pyplot as plt
from connected import *
import numpy as np
import timeit
import time


###########################################
# Algorithms

class UPATrial:
    """
    Simple class to encapsulate optimised trials for the UPA algorithm

    Maintains a list of node numbers with multiple instance of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities

    Uses random.choice() to select a node number from this list for each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a UPATrial object corresponding to a
        complete graph with num_nodes nodes

        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]

    def run_trial(self, num_nodes):
        """
        Conduct num_nodes trials using by applying random.choice()
        to the list of node numbers

        Updates the list of node numbers so that each node number
        appears in correct ratio

        Returns:
        Set of nodes
        """

        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for _ in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))

        # update the list of node numbers so that each node number
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        for dummy_idx in range(len(new_node_neighbors)):
            self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))

        # update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors


def er_graph(n, p):
    graph = {v: set() for v in range(n)}
    for pair in combinations(graph.keys(), 2):
        a = random.uniform(0, 1)
        if a < p:
            iterable = iter(pair)
            node1 = iterable.next()
            node2 = iterable.next()
            graph[node1].add(node2)
            graph[node2].add(node1)
    return graph


def upa_graph(m, n):
    graph = make_complete_graph(m)
    trial = UPATrial(m)
    for i in xrange(m, n):
        new_nodes = trial.run_trial(m)
        graph[i] = new_nodes
        for node in new_nodes:
            graph[node].add(i)
    return graph


def time_function(function, graph):
    start = time.clock()
    function(graph)
    return time.clock() - start


############################################
# Provided code

def degree(graph, node):
    return len(graph[node])


def copy_graph(graph):
    """
    Make a copy of a graph
    """
    new_graph = {}
    for node in graph:
        new_graph[node] = set(graph[node])
    return new_graph

def delete_node(ugraph, node):
    """
    Delete a node from an undirected graph
    """
    neighbors = ugraph[node]
    ugraph.pop(node)
    for neighbor in neighbors:
        ugraph[neighbor].remove(node)

def targeted_order(ugraph):
    """
    Compute a targeted attack order consisting
    of nodes of maximal degree

    Returns:
    A list of nodes
    """
    # copy the graph
    new_graph = copy_graph(ugraph)

    order = []
    while len(new_graph) > 0:
        max_degree = -1
        for node in new_graph:
            if len(new_graph[node]) > max_degree:
                max_degree = len(new_graph[node])
                max_degree_node = node

        neighbors = new_graph[max_degree_node]
        new_graph.pop(max_degree_node)
        for neighbor in neighbors:
            new_graph[neighbor].remove(max_degree_node)

        order.append(max_degree_node)
    return order


def fast_targeted_order(graph):
    n = len(graph)
    degree_sets = {}
    for i in xrange(n):
        degree_sets[i] = set()
    for node in graph:
        d = degree(graph, node)
        degree_sets[d].add(node)
    l = []
    for k in xrange(n - 1, -1, -1):
        while degree_sets[k]:
            u = degree_sets[k].pop()
            for v in graph[u]:
                d = degree(graph, v)
                degree_sets[d].remove(v)
                degree_sets[d - 1].add(v)
            l.append(u)
            for k, w in graph.items():
                if k == u:
                    del graph[k]
                elif u in w:
                    w.remove(u)
    return l





##########################################################
# My stuff

def count_edges(graph):
    return sum(len(value) for value in graph.values()) // 2


def random_order(graph):
    nodes = graph.keys()
    random.shuffle(nodes)
    return nodes


##########################################################
# Code for loading computer network graph

NETWORK_URL = "alg_rf7.txt"


def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph

    Returns a dictionary that models a graph
    """
    graph_file = open(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[:-1]

    print "Loaded graph with", len(graph_lines), "nodes"

    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph

# print "The network has", count_edges(network), "edges."

# random_attack_order = random_order(network)



# def plot1():
#
#     x_vals = range(n + 1)
#     er_vals = np.loadtxt("ER.txt")
#     upa_vals = np.loadtxt("UPA.txt")
#     network_vals = np.loadtxt("NETWORK.txt")
#
#
#     plt.plot(x_vals, er_vals, '-b', label='ER (p=0.003973)')
#     plt.plot(x_vals, upa_vals, '-r', label='UPA (m=3)')
#     plt.plot(x_vals, network_vals, '-g', label="Network")
#
#     plt.title("Resilience of Computer Networks")
#     plt.xlabel("Number of computers hacked")
#     plt.ylabel("Resilience")
#     plt.legend(loc="upper right")
#     plt.savefig("graph1.png")


# def plot2():
#
#     x_vals = range(10, 1000, 10)
#     target_vals = []
#     fast_target_vals = []
#     for n in x_vals:
#         graph = upa_graph(5, n)
#         graph_copy = deepcopy(graph)
#         target_vals.append(time_function(targeted_order, graph))
#         fast_target_vals.append(time_function(fast_targeted_order, graph_copy))
#
#     print target_vals
#     print fast_target_vals
#
#     plt.plot(x_vals, target_vals, '-b', label="non-fast")
#     plt.plot(x_vals, fast_target_vals, '-r', label="fast")
#
#
#
#     plt.title("Runtimes of targeting order functions on UPA graphs\n using time.clock() (m=5)")
#
#     plt.xlabel("Number of nodes")
#     plt.ylabel("Runtime (s)")
#
#     plt.legend(loc="upper left")
#     plt.savefig("graph2.png")
#
#
#
# # print fast_targeted_order({0: {1, 2}, 1: {0, 2}, 2: {0, 1}})


def plot3():

    network = load_graph(NETWORK_URL)
    n, p, m = 1239, 0.003973, 3

    er = er_graph(n, p)
    upa = upa_graph(m, n)

    x_vals = range(n + 1)
    er_vals = compute_resilience(er, targeted_order(er))
    upa_vals = compute_resilience(upa, targeted_order(upa))
    network_vals = compute_resilience(network, targeted_order(network))

    print len(x_vals)
    print len(er_vals)
    print len(upa_vals)
    print len(network_vals)



    plt.plot(x_vals, er_vals, '-b', label='ER (p=0.003973)')
    plt.plot(x_vals, upa_vals, '-r', label='UPA (m=3)')
    plt.plot(x_vals, network_vals, '-g', label="Network")
    plt.plot(x_vals, [1.25*(1239 - x) for x in x_vals], 'p', label="fish")
    plt.plot(x_vals, [0.75*(1239 - x) for x in x_vals], 'p', label="butt")

    plt.title("Resilience of Computer Networks using fast_targeted_order")
    plt.xlabel("Number of computers hacked")
    plt.ylabel("Resilience")
    plt.legend(loc="upper right")
    plt.savefig("graph3.png")

plot3()