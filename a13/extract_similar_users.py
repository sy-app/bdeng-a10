def extract_similar_users(source_users):
    similar_users = sorted(source_users, key=lambda su: su.similarity, reverse=True)[:2]

    return similar_users
