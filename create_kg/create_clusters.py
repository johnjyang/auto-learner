from sentence_transformers import util
import time
import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from create_data import write_txt

def create_clusters(corpus, model):
    print("Encoding the corpus. This might take a while.")
    corpus_embeddings = model.encode(corpus,
                                     batch_size=64,
                                     show_progress_bar=True,
                                     convert_to_tensor=True)
    print("Start clustering ...")
    start_time = time.time()
    clusters = util.community_detection(corpus_embeddings,
                                        min_community_size=2,
                                        threshold=0.6)
    print("Clustering completed in {:.2f} secs.".format(time.time() - start_time))
    return clusters


def log_clusters(file_name, clusters, corpus, repeat=False):
    results = []
    if repeat:
        for c in range(len(clusters)):
            cluster = []
            for i in clusters[c]:
                cluster.append(corpus[i])
            results.append(cluster)
    else:
        cluster_words = []
        for c in range(len(clusters)):
            cluster = []
            for i in clusters[c]:
                if not corpus[i] in cluster_words:
                    cluster.append(corpus[i])
                    cluster_words.append(corpus[i])
            results.append(cluster)
            cluster_words = []
    write_txt.list_of_list_to_txt(file_name, results)