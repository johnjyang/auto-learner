from sentence_transformers import SentenceTransformer
from get_searches import *
import umap
import hdbscan
import matplotlib.pyplot as plt
import pandas as pd

model = SentenceTransformer('all-mpnet-base-v2')

embeddings = model.encode(get_searches()[:500],
                          batch_size=64,
                          show_progress_bar=True,
                          convert_to_tensor=True)

umap_embeddings = umap.UMAP(n_neighbors=15,
                            n_components=5,
                            metric='cosine',
                            low_memory=False).fit_transform(embeddings)

cluster = hdbscan.HDBSCAN(min_cluster_size=15,
                          min_samples=1,
                          metric='euclidean',
                          cluster_selection_method='eom',
                          prediction_data=True).fit(umap_embeddings)

# Source: https://towardsdatascience.com/topic-modeling-with-bert-779f7db187e6