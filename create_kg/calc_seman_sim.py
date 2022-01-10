from sentence_transformers import SentenceTransformer, util
from get_searches import *
import time

def calc_seman_sim(query, corps):
    '''
    BERT based semantic similarity calculation

    Query: search phrase
    Corps: list of phrases to compare to
    Range: specify range of corps (if needed)

    Output: list of tuples, (Phrase, Similarity Score)
    '''
    model = SentenceTransformer('all-mpnet-base-v2')

    corpus_embeddings = model.encode(corps)

    print("Encode the corpus. This might take a while.")
    sentence_embedding = model.encode(query,
                                      batch_size=64,
                                      show_progress_bar=True,
                                      convert_to_tensor=True)

    print("Start calculations ...")
    start_time = time.time()
    cos_scores = util.pytorch_cos_sim(sentence_embedding, corpus_embeddings)[0]
    print("Calculations completed in {:.2f} secs.".format(time.time() - start_time))

    results = list(zip(corps, cos_scores))
    results.sort(key=lambda i: i[1], reverse=True)

    return results

'''
search = "most famous architect"
searches = get_searches()
top_results = calc_seman_sim(search, searches[:500])
top_k = 3
for i in range(len(top_results[0:top_k])):
    print(top_results[i])
'''
