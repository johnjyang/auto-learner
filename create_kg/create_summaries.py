import time
import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from create_data import write_txt

def summarize_clusters(clusters, model):
    print("Start summarizing ...")
    start_time = time.time()
    summaries = []
    for c in range(len(clusters)):
        summary_text = model(clusters[c],
                                max_length=15,
                                min_length=1,
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
    return summaries


def log_summaries(file_name, summaries):
    write_txt.list_of_str_to_txt(file_name, summaries)