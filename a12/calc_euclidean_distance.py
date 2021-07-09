import numpy as np


def calc_euclidean_distance(p0, p1):
    d = np.sqrt((p0.x-p1.x)**2 + (p0.y-p1.y)**2)
    return d
