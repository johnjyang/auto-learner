import os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from transformers import pipeline
from create_data.init_clean import *
from create_data.create_searches import *
from create_kg.get_data import *
from create_kg.create_clusters import *
from create_kg.create_summaries import *
from create_kg.create_tree_json import *
'''
# clean html and log searches
load_dotenv()
cleaned_html = init_clean(os.getenv('HTML_FILE_NAME'))
log_searches(cleaned_html)

# create and log clusters_0 from searches
searches = get_data('searches')
cluster_model = SentenceTransformer('all-mpnet-base-v2')
clusters_0_raw = create_clusters(searches, cluster_model, 0.6)
log_clusters('clusters_0', clusters_0_raw, searches)
log_clusters('clusters_0_repeat', clusters_0_raw, searches, True)

# create and log summaries_0 from clusters_0
clusters_0 = get_data('clusters_0')
os.environ['CUDA_VISIBLE_DEVICES'] = os.getenv('CUDA_GPU_COUNT')
summarize_model = pipeline('summarization', model='sshleifer/distilbart-cnn-12-6')
summaries_0_raw = summarize_clusters(clusters_0, summarize_model)
log_summaries('summaries_0', summaries_0_raw)

# create and log clusters_1 from summaries_0
summaries_0 = get_data('summaries_0')
clusters_1_raw = create_clusters(summaries_0, cluster_model, 0.4)
log_clusters('clusters_1', clusters_1_raw, summaries_0)

# create and log summaries_1 from clusters_1
clusters_1 = get_data('clusters_1')
summaries_1_raw = summarize_clusters(clusters_1, summarize_model)
log_summaries('summaries_1', summaries_1_raw)
'''
# create frontend/search_tree.json
create_tree_json()
