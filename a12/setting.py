from point import *


def setting():
    points = []
    points_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    X = [0, 2, 2, 3, 4, 5, 6, 8]
    Y = [0, 0, 1, 0, 1, 0, 0, 0]
    for i, p_info in enumerate(zip(points_names, X, Y)):
        name, x, y = p_info
        p = Point(i, name, x, y)
        points.append(p)

    epsilon = 1
    min_pts = 2

    return points, epsilon, min_pts
