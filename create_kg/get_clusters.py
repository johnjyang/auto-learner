def get_clusters():

    with open('./data/search_clusters_single.txt', 'r', encoding='utf-8') as f:
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
