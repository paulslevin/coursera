"""
Algorithmic Thinking Module 2
"""
from collections import deque
from copy import deepcopy

def enqueue(queue, node):
    """
    Enqueue the given node to the given queue
    :param queue:
    :param node:
    :return:
    """
    queue.appendleft(node)


def dequeue(queue):
    """
    Dequeue the given queue
    :param queue:
    :return:
    """
    return queue.pop()


def bfs_visited(ugraph, start_node):
    """
    Run BFS algorithm
    :param ugraph:
    :param start_node:
    :return:
    """
    queue = deque([])
    visited = {start_node}
    enqueue(queue, start_node)
    while queue:
        next_node = dequeue(queue)
        for neighbour in ugraph[next_node]:
            if neighbour not in visited:
                visited |= {neighbour}
                enqueue(queue, neighbour)
    return visited


def cc_visited(ugraph):
    """
    Find connected components
    :param ugraph:
    :return:
    """
    remaining = set(ugraph.keys())
    components = []
    while remaining:
        node = iter(remaining).next()
        component = bfs_visited(ugraph, node)
        components.append(component)
        remaining -= component
    return components


def largest_cc_size(ugraph):
    """
    Return largest component size
    :param ugraph:
    :return:
    """
    if cc_visited(ugraph):
        return max(len(component) for component in cc_visited(ugraph))
    return 0


def compute_resilience(ugraph, attack_order):
    smaller_graph = deepcopy(ugraph)
    attack_copy = deque(deepcopy(attack_order))
    resilience = [largest_cc_size(ugraph)]
    while attack_copy:
        next_node = attack_copy.popleft()
        smaller_graph = {k: v - {next_node} for
                         k, v in smaller_graph.iteritems() if
                         k != next_node}
        resilience.append(largest_cc_size(smaller_graph))
    return resilience
