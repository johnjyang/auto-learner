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

searches = get_searches()
print("Encode the corpus. This might take a while.")
corpus_embeddings = model.encode(searches,
                                 batch_size=64,
                                 show_progress_bar=True,
                                 convert_to_tensor=True)

print("Start clustering ...")
start_time = time.time()

#Two parameters to tune:
#min_cluster_size: Only consider cluster that have at least # elements
#threshold: Consider sentence pairs with a cosine-similarity larger than threshold as similar
clusters = util.community_detection(corpus_embeddings,
                                    min_community_size=2,
                                    threshold=0.6)

print("Clustering completed in {:.2f} secs.".format(time.time() - start_time))

results = []
for c in range(len(clusters)):
    for i in clusters[c]:
        results.append(searches[i])
    results.append('End of cluster ' + str(c + 1))

write_txt.list_to_txt("search_clusters", results)
