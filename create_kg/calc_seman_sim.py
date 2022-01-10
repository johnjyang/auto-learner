from sentence_transformers import SentenceTransformer, util
from get_searches import *
import time

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

    print("Encode the corpus. This might take a while")
    sentence_embedding = model.encode(query,
                                      batch_size=64,
                                      show_progress_bar=True,
                                      convert_to_tensor=True)

    print("Start calculating similarity scores")
    start_time = time.time()
    cos_scores = util.pytorch_cos_sim(sentence_embedding, corpus_embeddings)[0]
    print("Calculation done after {:.2f} sec".format(time.time() - start_time))

    results = list(zip(corps, cos_scores))
    results.sort(key=lambda i: i[1], reverse=True)

    return results

'''
search = "most famous architect"
searches = get_searches()
search_range = None
top_results = calc_seman_sim(search, searches, search_range)
top_k = 3
for i in range(len(top_results[0:top_k])):
    print(top_results[i])
'''
