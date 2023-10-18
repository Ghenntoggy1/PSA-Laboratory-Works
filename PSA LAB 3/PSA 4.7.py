# 4.7 Suggestion occurrences
import json
import nltk
import re
import contractions
from nltk.probability import FreqDist


unword = input("Input word: ")
f = open('tweets.json', "r", encoding='utf-8')
data = json.loads(f.read())
f.close()
text = []
for text_field in data:
    clrtxt = text_field['text']
    clrtxt = clrtxt.replace('RT', '')
    clrtxt = clrtxt.replace('\n', ' ')
    clrtxt = re.sub(r'http\S+', '', clrtxt)
    clrtxt = re.sub('@[A-Za-z0-9_]+', '', clrtxt)
    clrtxt = re.sub('#[A-Za-z0-9]+', '', clrtxt)
    clrtxt = contractions.fix(clrtxt)
    str1 = nltk.RegexpTokenizer(r"\w+")
    str2 = str1.tokenize(clrtxt)
    text.append(str2)

words = []
for lists in text:
    for word in lists:
        words.append(word)
next = []
for i in range(len(words) - 1):
    if words[i].lower() == unword:
        next.append(words[i + 1])
# print(next)

fdist = FreqDist()
for string in next:
    fdist[string.lower()] += 1
freq = dict(fdist)
freq_sorted = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True)}
# print(freq_sorted)
res = []
try:
    freq_sorted.pop(unword)
    for k in freq_sorted.keys():
        res.append(k)
        if len(res) == 3:
            break
    for word in res:
        print(word, f'({freq_sorted[word]})')
except KeyError:
    for k in freq_sorted.keys():
        res.append(k)
        if len(res) == 3:
            break
    for word in res:
        print(word, f'({freq_sorted[word]})')
