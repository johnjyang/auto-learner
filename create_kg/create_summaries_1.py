from transformers import pipeline
import os, sys
import time
from get_clusters import *

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from create_data import write_txt

print("Loading model. This may take a while.")
start_time = time.time()
os.environ["CUDA_VISIBLE_DEVICES"] = "2"
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
print("Model loaded in {:.2f} secs.".format(time.time() - start_time))

clusters = get_clusters_1()

print("Start summarizing ...")
start_time = time.time()
summaries = []
for c in range(len(clusters)):
    summary_text = summarizer(clusters[c],
                              max_length=5,
                              min_length=2,
                              do_sample=False)[0]['summary_text']
    summary_text = summary_text.replace('"', '')
    summary_text = summary_text.split(',')[0]
    summary_text = summary_text.split(' . ')[0]
    summary_text = summary_text.split(':  ')[0]
    summary_text = summary_text.split('is')[0]
    summary_text = summary_text.lstrip().strip()
    if summary_text:
        summaries.append(summary_text.lower())
    print("Summarized cluster " + str(c + 1) + "/" + str(len(clusters)))
print("Summarizing completed in {:.2f} secs.".format(time.time() - start_time))

write_txt.list_to_txt("summaries_1", summaries)
