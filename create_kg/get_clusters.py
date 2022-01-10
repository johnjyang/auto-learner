def get_clusters():

    with open('./data/search_clusters.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    clusters_list = []
    cluster = ''
    cluster_words = []

    for line in lines:
        line = line.replace('\n', ', ')
        if line[:15] == "End of cluster ":
            clusters_list.append(cluster)
            cluster = ''
        else:
            if not line in cluster_words:
                if len(cluster) < 1024:
                    cluster += line
                    cluster_words.append(line)
            else:
                continue

    return clusters_list
