"""
Student template code for Project 3
Student will implement five functions:

slow_closest_pair(cluster_list)
fast_closest_pair(cluster_list)
closest_pair_strip(cluster_list, horiz_center, half_width)
hierarchical_clustering(cluster_list, num_clusters)
kmeans_clustering(cluster_list, num_clusters, num_iterations)

where cluster_list is a 2D list of clusters in the plane
"""

import math
import alg_cluster


######################################################
# Code for closest pairs of clusters


def pair_distance(cluster_list, idx1, idx2):
    """
    Helper function that computes Euclidean distance between two clusters in a list

    Input: cluster_list is list of clusters, idx1 and idx2 are integer indices for two clusters

    Output: tuple (dist, idx1, idx2) where dist is distance between
    cluster_list[idx1] and cluster_list[idx2]
    """
    return (cluster_list[idx1].distance(cluster_list[idx2]), min(idx1, idx2),
            max(idx1, idx2))


def slow_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (slow)

    Input: cluster_list is the list of clusters

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.
    """
    distance, idx1, idx2 = (float("inf"), -1, -1)
    for idx3, cluster in enumerate(cluster_list):
        for idx4, other_cluster in enumerate(cluster_list):
            if idx3 == idx4:
                continue
            distance, idx1, idx2 = min((distance, idx1, idx2),
                                       (cluster.distance(other_cluster),
                                        idx3, idx4),
                                       key=lambda z: z[0])
    return distance, idx1, idx2


def fast_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (fast)

    Input: cluster_list is list of clusters SORTED such that horizontal positions of their
    centers are in ascending order

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.
    """
    num = len(cluster_list)
    if num <= 3:
        return slow_closest_pair(cluster_list)
    midpoint = num / 2
    left, right = cluster_list[:midpoint], cluster_list[midpoint:]
    left_pair = fast_closest_pair(left)
    right_pair = fast_closest_pair(right)
    right_pair[1] += midpoint
    right_pair[2] += midpoint
    result = min((left_pair, right_pair), key=lambda z: z[0])
    mid = 0.5 * (cluster_list[midpoint].horiz_center +
                 cluster_list[midpoint - 1].horiz_center())
    return min(result, closest_pair_strip(cluster_list, mid, result[0]),
               key=lambda z: z[0])


def closest_pair_strip(cluster_list, horiz_center, half_width):
    """
    Helper function to compute the closest pair of clusters in a vertical strip

    Input: cluster_list is a list of clusters produced by fast_closest_pair
    horiz_center is the horizontal position of the strip's vertical center line
    half_width is the half the width of the strip (i.e; the maximum horizontal distance
    that a cluster can lie from the center line)

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] lie in the strip and have minimum distance dist.
    """
    in_range = [idx for idx, _ in enumerate(cluster_list) if
                abs(idx - horiz_center) < half_width]
    in_range = sorted(in_range, key=lambda z: cluster_list[z].vert_center())
    length = len(in_range)
    print "length is", length
    result = (float("inf"), -1, -1)
    values = []
    if result == 1:
        values = [0]
    else:
        values = xrange(0, length - 1)
    for idz in values:
        for idw in range(idz + 1, min(idz + 3, length - 1) + 1):
            cluster1 = cluster_list[in_range[idz]]
            cluster2 = cluster_list[in_range[idw]]
            result = min(result, (cluster1.distance(cluster2),
                                  in_range[idz], in_range[idw]),
                         key=lambda z: z[0])
    return result

print closest_pair_strip([alg_cluster.Cluster(set([]), 0, 0, 1, 0), alg_cluster.Cluster(set([]), 0, 1, 1, 0), alg_cluster.Cluster(set([]), 0, 2, 1, 0), alg_cluster.Cluster(set([]), 0, 3, 1, 0)], 0.0, 1.0)


######################################################################
# Code for hierarchical clustering


def hierarchical_clustering(cluster_list, num_clusters):
    """
    Compute a hierarchical clustering of a set of clusters
    Note: the function may mutate cluster_list

    Input: List of clusters, integer number of clusters
    Output: List of clusters whose length is num_clusters
    """

    return []


######################################################################
# Code for k-means clustering


def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    """
    Compute the k-means clustering of a set of clusters
    Note: the function may not mutate cluster_list

    Input: List of clusters, integers number of clusters and number of iterations
    Output: List of clusters whose length is num_clusters
    """

    # position initial clusters at the location of clusters with largest populations

    return []
