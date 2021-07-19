from setting import *
from assign_similarity import *
from extract_similar_users import *
from recommend_item import *


def main():
    source_users, target_user = setting()
    assign_similarity(source_users, target_user)
    similar_users = extract_similar_users(source_users)
    recommended_item = recommend_item(similar_users, target_user)
    print('Item {} should be recommended.'.format(recommended_item))


if __name__ == '__main__':
    main()
