# 4.6 Suggestion
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
    clrtxt = re.sub(r'http\S+', '', clrtxt)
    clrtxt = re.sub('@[A-Za-z0-9_]+', '', clrtxt)
    clrtxt = re.sub('#[A-Za-z0-9]+', '', clrtxt)
    clrtxt = contractions.fix(clrtxt)
    text.append(clrtxt)

string_list = []
for string in text:
    str1 = nltk.RegexpTokenizer(r"\w+")
    str2 = str1.tokenize(string)
    string_list.append(str2)

fdist = FreqDist()
for string in string_list:
    for word in string:
        fdist[word.lower()] += 1

freq = dict(fdist)
freq_sorted = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True)}
# print(freq_sorted)

res = []
try:
    freq_sorted.pop(unword)
    for k in freq_sorted.keys():
        if k.startswith(unword) and k != unword + "s":
        #if k.startswith(unword) and (k != unword + "s" and k != unword + "es"):
            res.append(k)
        if len(res) == 3:
            break

    for word in res:
        print(word, f"({freq_sorted[word]})")
except KeyError:
    for k in freq_sorted.keys():
        if k.startswith(unword):
            res.append(k)
        if len(res) == 3:
            break

    for word in res:
        print(word, f"({freq_sorted[word]})")
