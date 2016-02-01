from itertools import permutations
from random import uniform
# from graphs_application import DegreeDistribution
import matplotlib.pyplot as pyplot

def ER(n, p):
    V = set(range(n))
    E = set()
    for pair in permutations(V, 2):
        a = uniform(0, 1)
        if a < p:
            E.add(pair)
    G = {v: set() for v in V}
    for e in E:
        G[e[0]].add(e[1])
    return G
