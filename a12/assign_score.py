from calc_score import *


def assign_score(points, clusters):
    for p in points:
        score = calc_score(p, clusters)
        if score is None:
            pass
        else:
            p.score = score
        # print('{}のscore= {}'.format(p.name, p.score))
