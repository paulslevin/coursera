from collections import deque


def enqueue(queue, node):
    queue.appendleft(node)


def dequeue(queue):
    return queue.pop()


def bfs_visited(ugraph, start_node):
    queue = deque([])
    visited = {start_node}
    enqueue(queue, start_node)
    while queue:
        next = dequeue(queue)
        for neighbour in ugraph[next]:
            print neighbour
            if neighbour not in visited:
                visited |= {neighbour}
                enqueue(queue, neighbour)
    return visited



def cc_visited(ugraph):
    pass


def largest_cc_size(ugraph):
    pass


def compute_resilience(ugraph, attack_order):
    pass

