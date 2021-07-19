from user import *
import numpy as np


def setting():
    matrix = np.array(
        [
            [1, 0, 1, 1, 1, 0],
            [1, 0, 1, 0, 0, 1],
            [1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 1, 1],
            [0, 0, 1, 0, 0, 1],
            [1, 1, 0, 1, 0, 0]
        ]
    )
    n_source_user = len(matrix)-1
    source_users = []
    for i, items in enumerate(matrix[:n_source_user]):
        u = User(i, items)
        source_users.append(u)

    target_user = User(len(matrix)-1, matrix[-1])

    return source_users, target_user
