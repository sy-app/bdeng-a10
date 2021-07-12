from calc_euclidean_distance import *
import numpy as np


def calc_score(p, clusters):
    if p.belong_to is None:
        return None
    else:
        dist = np.inf
        for i, cluster in enumerate(clusters):
            if i == p.belong_to:
                continue
            for p_another in cluster:
                if p.id == p_another.id:
                    continue
                dist = min(dist, calc_euclidean_distance(p, p_another))
        n_point_of_same_cluster = len(clusters[p.belong_to])
        score = dist / n_point_of_same_cluster

        return score
