from sentence_transformers import SentenceTransformer
from GetSearches import *

model = SentenceTransformer('distilbert-base-nli-mean-tokens')
embeddings = model.encode(GetSearches(), show_progress_bar=True)