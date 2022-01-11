from transformers import pipeline
import os, sys
import requests
import time
from get_clusters import *

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from create_data import write_txt

clusters = get_clusters_1()[:10]


def topic_tagging(text):
    tag = requests.post(
        url='https://twinword-topic-tagging.p.rapidapi.com/generate/',
        headers={
            'content-type': 'application/x-www-form-urlencoded',
            'x-rapidapi-host': 'twinword-topic-tagging.p.rapidapi.com',
            'x-rapidapi-key':
            'fea19f5fb0msha93d82d70bfe072p150eb5jsn06e794a82d03'
        },
        data={
            'text': text
        }).text
    print(tag)
    tag = eval(tag)['topic']
    print(tag)
    tag = list(tag)
    return tag[0]


print("Start tagging ...")
start_time = time.time()
summaries = []
for c in range(len(clusters)):
    summary_text = topic_tagging(clusters[c])
    if summary_text:
        summaries.append(summary_text)
    print("Summarized cluster " + str(c + 1) + "/" + str(len(clusters)))
print("Summarizing completed in {:.2f} secs.".format(time.time() - start_time))

write_txt.list_of_str_to_txt("summaries_1", summaries)
