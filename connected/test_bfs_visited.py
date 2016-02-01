from unittest import TestCase
from connected import *


class TestEverything(TestCase):

    def setUp(self):
        self.graph1 = {0: {1, 2}, 1: {0, 2}, 2: {0, 1}}
        self.graph2 = {0: {1, 2, 3}, 1: {0, 4, 5}, 2: {0, 6, 7}, 3: {0, 8, 9},
                       4: {1}, 5: {1}, 6: {2}, 7: {2}, 8: {3}, 9: {3}}
        self.graph3 = {0: {1}, 1: {0}, 2: {3}, 3: {2, 4}, 4: {3}}
        self.graph4 = {0: {}, 1: {}}

    def test_bfs_visited(self):
        self.assertEqual(bfs_visited(self.graph1, 0),
                         {0, 1, 2})
        self.assertEqual(bfs_visited(self.graph2, 0),
                         {0, 1, 2, 3, 4, 5, 6, 7, 8, 9})
        self.assertEqual(bfs_visited(self.graph3, 0),
                         {0, 1})
        self.assertEqual(bfs_visited(self.graph3, 2),
                         {2, 3, 4})
        self.assertEqual(bfs_visited(self.graph4, 0),
                         {0})

    def test_cc_visited(self):
        self.assertEqual(cc_visited(self.graph1),
                         [{0, 1, 2}])
        self.assertEqual(sorted(cc_visited(self.graph3)),
                         sorted([{0, 1}, {2, 3, 4}]))
        self.assertEqual(sorted(cc_visited(self.graph4)),
                         sorted([{0}, {1}]))

    def test_largest_cc_size(self):
        self.assertEqual(largest_cc_size(self.graph1),
                         3)
        self.assertEqual(largest_cc_size(self.graph2),
                         10)
        self.assertEqual(largest_cc_size(self.graph3),
                         3)
        self.assertEqual(largest_cc_size(self.graph4),
                         1)

    def test_compute_resilience(self):
        self.assertEqual(compute_resilience(self.graph1, []),
                         [3])
        self.assertEqual(compute_resilience(self.graph1, [2]),
                         [3, 2])
        self.assertEqual(compute_resilience(self.graph2, [0]),
                         [10, 9])
        self.assertEqual(compute_resilience(self.graph2, [1]),
                         [10, 7])
        self.assertEqual(compute_resilience(self.graph2, [1, 2]),
                         [10, 7, 4])
        self.assertEqual(compute_resilience(self.graph2, [1, 2, 3]),
                         [10, 7, 4, 1])
