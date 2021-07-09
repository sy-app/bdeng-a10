from setting import *
from dbscan import *
from assign_score import *


def main():
    points, epsilon, min_pts = setting()
    points = dbscan(points, epsilon, min_pts)
    points = assign_score(points)


if __name__ == '__main__':
    main()
