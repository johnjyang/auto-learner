from sentence_transformers import SentenceTransformer, util
from get_searches import *

def calc_seman_sim(query, corps, range=None):
    '''
    BERT based semantic similarity calculation

    Query: search phrase
    Corps: list of phrases to compare to
    Range: specify range of corps (if needed)

    Output: list of tuples, (Phrase, Similarity Score)
    '''
    model = SentenceTransformer('all-mpnet-base-v2')

    if range:
        corpus_embeddings = model.encode(corps[:range])
    else:
        corpus_embeddings = model.encode(corps)

    sentence_embedding = model.encode(query)
    cos_scores = util.pytorch_cos_sim(sentence_embedding, corpus_embeddings)[0]
    results = list(zip(corps, cos_scores))
    results.sort(key=lambda i: i[1], reverse=True)

    return results

'''
search = "most famous architect"
searches = GetSearches()
search_range = 1000
top_results = calc_seman_sim(search, searches, search_range)
top_k = 3
for i in range(len(top_results[0:top_k])):
    print(top_results[i])
'''
