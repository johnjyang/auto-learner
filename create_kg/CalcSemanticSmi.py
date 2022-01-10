from sentence_transformers import SentenceTransformer, util


def CalcSemanticSimi(query, corps, range=None):
    '''
    BERT based semantic similarity calculation

    Query: search phrase
    Corps: list of phrases to compare to
    Range: specify range of corps (if needed)

    Output: list of tuples, (Phrase, Similarity Score)
    '''
    model = SentenceTransformer('stsb-roberta-large')
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
with open('./data/searches.txt', 'r', encoding='utf-8') as f:
lines = f.readlines()

searches_list = []

for line in lines:
line = line.replace('\n', '')
searches_list.append(line)

search = "most famous architecture"

search_range = 50
top_results = CalcSemanticSimi(search, searches_list, search_range)

top_k = 3
for i in range(len(top_results[0:top_k])):
print(top_results[i])
'''
