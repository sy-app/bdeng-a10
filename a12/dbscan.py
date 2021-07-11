from calc_euclidean_distance import *
from set_color import *
import numpy as np
import matplotlib.pyplot as plt


def dbscan(points, epsilon, min_pts):
    new_label = 0
    step = 0
    for p in points:
        step += 1

        # 近傍点には自分自身も含めて初期化
        # n_neighborhood = 1
        tmp_neighborhoods = [p]

        # pの近傍を探索
        for p_another in points:
            if p.id == p_another.id:
                continue
            if calc_euclidean_distance(p, p_another) <= epsilon:
                # n_neighborhood += 1
                tmp_neighborhoods.append(p_another)

        # min_pts個以上近傍点がある場合
        if len(tmp_neighborhoods) >= min_pts:
            # 付与するlabelを決定
            label = np.inf
            for tmp_nbh in tmp_neighborhoods:
                if tmp_nbh.belong_to is not None:
                    label = min(label, tmp_nbh.belong_to)
            if label == np.inf:
                label = new_label
                new_label += 1

            # if p.belong_to is None:
            #     label = new_label
            #     new_label += 1
            #     # core pointにラベルを付与
            #     p.belong_to = label
            # else:
            #     label = p.belong_to

            # 近傍点にラベルを付与
            for tmp_nbh in tmp_neighborhoods:
                # if tmp_nbh.belong_to is not None:
                tmp_nbh.belong_to = label

        # visualize
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        for p_scat in points:
            if p.id == p_scat.id:
                ax.scatter([p_scat.x], [p_scat.y], s=150, c='r', label='Attended point')
            else:
                ax.scatter([p_scat.x], [p_scat.y], s=100, c=set_color(p_scat))

        ax.legend()
        ax.set_title('step:{}'.format(step))
        ax.set_xlabel('x')
        ax.set_ylabel('y')

        fig.show()
        # fig.savefig('img/a11-{}.png'.format(step), dpi=300)

    # visualize result
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    n_cluster = max([p.belong_to for p in points if p.belong_to is not None]) + 1  # クラスター数が0でない仮定
    clusters = []
    for i in range(n_cluster):
        cluster = [p for p in points if p.belong_to == i]
        clusters.append(cluster)
    noise = [p for p in points if p.belong_to is None]

    # 描画
    for cluster in clusters:
        x = [p.x for p in cluster]
        y = [p.y for p in cluster]
        ax.scatter(x, y, s=100, c=set_color(cluster[0]))
    x = [p.x for p in noise]
    y = [p.y for p in noise]
    ax.scatter(x, y, s=100, c=set_color(noise[0]))

    ax.set_title('Result')
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    fig.show()

    # for i in range(len(x)):
    #     ax.scatter([x[i]], [y[i]], s=100, c=set_color(i,points,belong))
    #
    # ax.set_title('Result')
    # ax.set_xlabel('x')
    # ax.set_ylabel('y')
    #
    # fig.show()
    # fig.savefig('img/a11-result.png', dpi=300)

    return points, clusters
