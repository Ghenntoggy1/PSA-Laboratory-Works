# 4.5 Popularity
import json
import nltk
from nltk import word_tokenize
from collections import defaultdict
from scipy.stats import zscore


with open('tweets.json', encoding='utf8') as f:
    data = json.load(f)
f.close()
text = ''
for textfield in data:
    text += (textfield['text'])
text = [word.lower() for word in word_tokenize(text) if word.isalpha() and word != 'https']
tags = nltk.pos_tag(text)
nouns = [word for word, pos in tags if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS') and word != 'i']
frequency = defaultdict(int)
likes = defaultdict(int)
retweets = defaultdict(int)
for textfield in data:
    sequence = word_tokenize(''.join(word.lower() for word in textfield['text']))
    for j in sequence:
        if j in nouns:
            frequency[j] = nouns.count(j)
            likes[j] += textfield['likes']
            retweets[j] += textfield['retweets']
a, b = zip(*likes.items())
normLikes = dict(zip(a, zscore(b)))
x, y = zip(*retweets.items())
normRetweets = dict(zip(x, zscore(y)))
res = defaultdict(int)
for i in frequency:
    res[i] = frequency[i] * (1.4 + normRetweets[i]) * (1.2 + normLikes[i])
prop_nouns_dict = sorted(res, key=res.get, reverse=True)[:10]
print("Most popular nouns are:")
for nounfinal in prop_nouns_dict:
    print(nounfinal, res[nounfinal])
