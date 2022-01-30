import time
import os, sys
import re

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from create_data import write_txt


def summarize_clusters(clusters, model):
    print("Start summarizing ...")
    start_time = time.time()
    summaries = []
    for c in range(len(clusters)):
        if len(clusters[c].split(', ')) <= 3:
            summary_text = min(clusters[c].split(', '), key=len).lower().lstrip()
        else:
            if not re.search("[\u4e00-\u9FFF]", clusters[c][0]):
                summary_text = model(clusters[c][:1024], max_length=15, min_length=1, do_sample=False)[0]['summary_text'].lower().lstrip()
                found_search = False
                for search in clusters[c].split(', '):
                    if search in summary_text:
                        summary_text = search
                        found_search = True
                        break
                if not found_search:
                    summary_text = clusters[c].split(',')[0]
            else:
                summary_text = 'n/a (chinese)'
        if summary_text:
            summaries.append(summary_text.strip())
        else:
            summaries.append(clusters[c].split(',')[0])
            print(str(f'Error: cluster {c}, {clusters[c]}, {summary_text}'))
            write_txt.list_of_str_to_txt(
                'errors', [str(f'Error: cluster {c}, {clusters[c]}, {summary_text}')])
        print(
            f'Summarized cluster {str(c + 1)}/{str(len(clusters))}: {summary_text.lower()}'
        )
    print("Summarizing completed in {:.2f} secs.".format(time.time() - start_time))
    return summaries


def log_summaries(file_name, summaries):
    write_txt.list_of_str_to_txt(file_name, summaries)
