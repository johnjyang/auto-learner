from write_txt import *
from wordcloud import WordCloud
import matplotlib.pyplot as plt

from create_data.write_txt import list_to_txt

with open('./data/searches.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

words_list = []

for line in lines:
    terms = line.split(' ')
    for term in terms:
        term = term.strip()
        term = term.replace('\n', '')
        words_list.append(term)

list_to_txt("words_raw", words_list)

keywords = ['to', 'how', 'the', 'of', 'in', 'is', 'a', 'an', 'what', 'and', 'on', '', 'does', 'you', 'with', 'are', 'a', 'for']
words = []
freqs = []

for i in range(len(words_list)):
    if not words_list[i] in words and not words_list[i] in keywords:
        freq = 1
        words.append(words_list[i])
        for j in range(i + 1, len(words_list)):
            if words_list[i] == words_list[j]:
                freq += 1
        freqs.append(freq)
    else:
        continue

words_freqs = list(zip(words, freqs))
words_freqs.sort(key=lambda i: i[1], reverse=True)

tuple_to_txt("words_freq", words_freqs)

wordcloud = WordCloud(width=800,
                      height=800,
                      background_color='white',
                      max_words=300).generate_from_frequencies(
                          dict((x, y) for x, y in words_freqs))

plt.figure(figsize=(10, 10), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.savefig('./data/word_cloud.png')
plt.show()