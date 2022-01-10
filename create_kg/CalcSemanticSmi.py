from sentence_transformers import SentenceTransformer, util
from GetSearches import *

def CalcSemanticSimi(query, corps, range=None):
    '''
    BERT based semantic similarity calculation

    Query: search phrase
    Corps: list of phrases to compare to
    Range: specify range of corps (if needed)

    Output: list of tuples, (Phrase, Similarity Score)
    '''
    model = SentenceTransformer('all-mpnet-base-v2')

    if range:
        corpus_embeddings = model.encode(corps[:range], convert_to_tensor=True)
    else:
        corpus_embeddings = model.encode(corps, convert_to_tensor=True)

    sentence_embedding = model.encode(query, convert_to_tensor=True)
    cos_scores = util.pytorch_cos_sim(sentence_embedding, corpus_embeddings)[0]
    results = list(zip(corps, cos_scores))
    results.sort(key=lambda i: i[1], reverse=True)

    return results


'''
search = "most famous architect"
searches = GetSearches()
search_range = 1000
top_results = CalcSemanticSimi(search, searches, search_range)
top_k = 3
for i in range(len(top_results[0:top_k])):
    print(top_results[i])
'''
