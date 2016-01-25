"""
Provided code for Application portion of Module 1

Imports physics citation graph
"""

# general imports
from ER import ER
from DPA import dpa
from graphs import in_degree_distribution
from fractions import Fraction
import matplotlib.pyplot as pyplot
import random


class DegreeDistribution(object):

    def __init__(self, graph):
        self.distribution = in_degree_distribution(graph)
        self.values = sum(self.distribution.values())

    def normalise(self):
        self.distribution = dict((k, Fraction(v, self.values)) for k, v in
                    self.distribution.items())
        assert sum(v for v in self.distribution.values()) == 1

    def keys(self):
        return sorted(self.distribution.keys())

    def normalised_values(self):
        return [self.distribution[key] for key in self.keys()]


###################################
# Code for loading citation graph

CITATION_URL = "alg_phys-cite.txt"


def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph

    Returns a dictionary that models a graph
    """
    graph_file = open(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[: -1]

    print "Loaded graph with", len(graph_lines), "nodes"

    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1: -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph


def out_degree_average(graph):
    total_degrees = sum(len(graph[node]) for node in graph)
    return total_degrees / float(len(graph.keys()))


#citation_graph = load_graph(CITATION_URL)
# # print len(set(citation_graph.keys()))
# s = set.union(*citation_graph.values())
# print in_degree_distribution(citation_graph).items()
#
#

#d = DegreeDistribution(citation_graph)

#d.normalise()
# print d.distribution
# print d.keys()
# print d.normalised_values()

# fig1 = pyplot.figure()
# pyplot.loglog(d.keys(), d.normalised_values(), 'r.', basex=10, basey=10)
# pyplot.title("log/log plot points of normalised in-degree distribution\n (base 10)")
# pyplot.xlabel("in-degree")
# pyplot.ylabel("occurences (normalised)")
# pyplot.savefig("normalised.png")
#
# fig2 = pyplot.figure()
# n = random.randrange(250, 500)
# p = random.uniform(0, 1)
# d = DegreeDistribution(ER(n, p))
# d.normalise()
# pyplot.loglog(d.keys(), d.normalised_values(), 'r.', basex=10, basey=10)
# pyplot.title("log/log plot points of normalised in-degree distribution for ER graph \n n = {}, p = {}".format(n, p))
# pyplot.xlabel("in-degree")
# pyplot.ylabel("occurences (normalised)")
# pyplot.savefig("ER.png")

fig3 = pyplot.figure()
n = 27770
m = 13
graph = dpa(m, n)
print "done"

d = DegreeDistribution(graph)
d.normalise()
pyplot.loglog(d.keys(), d.normalised_values(), 'r.', basex=10, basey=10)
pyplot.title("log/log plot points of normalised in-degree distribution for DPA graph \n n = {}, m = {}".format(n, m))
pyplot.xlabel("in-degree")
pyplot.ylabel("occurences (normalised)")
pyplot.savefig("DPA.png")