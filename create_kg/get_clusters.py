def get_clusters_0():

    with open('./data/search_clusters_single_0.txt', 'r',
              encoding='utf-8') as f:
        lines = f.readlines()

    clusters_list = []
    cluster = ''

    for line in lines:
        line = line.replace('\n', ', ')
        if line[:15] == "End of cluster ":
            clusters_list.append(cluster)
            cluster = ''
        else:
            if len(cluster) < 1024:
                cluster += line

    return clusters_list


def get_clusters_1():

    with open('./data/search_clusters_single_1.txt', 'r',
              encoding='utf-8') as f:
        lines = f.readlines()

    clusters_list = []
    cluster = ''

    for line in lines:
        line = line.replace('\n', ', ')
        if line[:15] == "End of cluster ":
            clusters_list.append(cluster)
            cluster = ''
        else:
            if len(cluster) < 1024:
                cluster += line

    return clusters_list
