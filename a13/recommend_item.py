import numpy as np


def recommend_item(similar_users, target_user):
    predictions = []
    for i, i_target in enumerate(target_user.bought_items):
        if i_target == 1:
            pred = -1
        else:
            pred = sum([sim_u.bought_items[i] for sim_u in similar_users])

        predictions.append(pred)

    recommended_item = np.argmax(predictions)

    return recommended_item
