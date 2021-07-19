import numpy as np


def assign_similarity(source_users, target_user):
    for source in source_users:
        source.similarity = calc_similarity(source, target_user)


def calc_similarity(source, target_user):
    similarity = np.dot(source.bought_items, target_user.bought_items)

    return similarity
