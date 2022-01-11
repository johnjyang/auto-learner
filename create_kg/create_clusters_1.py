from os import write
from re import search
from sentence_transformers import SentenceTransformer, util
from get_searches import *
import time
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from create_data import write_txt

# model = SentenceTransformer('all-MiniLM-L6-v2')
model = SentenceTransformer('all-mpnet-base-v2')

summaries = get_summaries()
print("Encode the corpus. This might take a while.")
corpus_embeddings = model.encode(summaries,
                                 batch_size=64,
                                 show_progress_bar=True,
                                 convert_to_tensor=True)

print("Start clustering ...")
start_time = time.time()

#Two parameters to tune:
#min_cluster_size: Only consider cluster that have at least # elements
#threshold: Consider sentence pairs with a cosine-similarity larger than threshold as similar
clusters = util.community_detection(corpus_embeddings,
                                    min_community_size=3,
                                    threshold=0.5)

print("Clustering completed in {:.2f} secs.".format(time.time() - start_time))

results = []
for c in range(len(clusters)):
    for i in clusters[c]:
        results.append(summaries[i])
    results.append('End of cluster ' + str(c + 1))

write_txt.list_to_txt("search_clusters_repeat_1", results)

results = []
cluster_words = []
for c in range(len(clusters)):
    for i in clusters[c]:
        if not summaries[i] in cluster_words:
            results.append(summaries[i])
            cluster_words.append(summaries[i])
    results.append('End of cluster ' + str(c + 1))
    cluster_words = []

write_txt.list_to_txt("search_clusters_single_1", results)
