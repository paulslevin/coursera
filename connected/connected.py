"""
Algorithmic Thinking Module 2
"""
from collections import deque


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
    """
    Get resilience of graph
    :param ugraph:
    :param attack_order:
    :return:
    """
    if not attack_order:
        return [largest_cc_size(ugraph)]
    if not isinstance(attack_order, deque):
        attack_order = deque(attack_order)
    next_node = attack_order.popleft()
    smaller_graph = {k: v - {next_node} for k, v in ugraph.iteritems() if
                     k != next_node}
    return [largest_cc_size(ugraph)] + compute_resilience(smaller_graph,
                                                          attack_order)
