# 4.2 Nouns
import json
import nltk
import re
from nltk.probability import FreqDist
import contractions
import enchant

d = enchant.Dict("en_US")
f = open('tweets.json', "r", encoding='utf-8')
data = json.loads(f.read())
f.close()
text = []
for text_field in data:
    clrtxt = text_field['text']
    clrtxt = clrtxt.replace('\n', ' ')
    clrtxt = clrtxt.replace('RT', '')
    clrtxt = re.sub(r'http\S+', '', clrtxt)
    clrtxt = re.sub('@[A-Za-z0-9_]+', '', clrtxt)
    clrtxt = re.sub('#[A-Za-z0-9]+', '', clrtxt)
    clrtxt = contractions.fix(clrtxt)
    clrtxt = clrtxt.replace("'s", '')
    text.append(clrtxt)

nouns = []
for string in text:
    is_noun = lambda pos: pos[:2] == "NN"
    tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
    tokenized = tokenizer.tokenize(string)
    nouns.append([word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos) and d.check(word.lower()) or word == 'kind'])
nouns2 = []
for list in nouns:
    for string in list:
        if len(string) > 1:
            nouns2.append(string.lower())
# print(nouns2)

fdist = FreqDist()
for word in nouns2:
    fdist[word.lower()] += 1
    for suffix in ['s']:
        if word.endswith(suffix):
            fdist[word.lower()[:-len(suffix)]] += 1
            fdist.__delitem__(word)

freq = dict(fdist)
freq_sorted = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True)}
for idx, (k, v) in enumerate(freq_sorted.items()):
    if idx == 10:
        break
    print(k, v)





# import json
# import nltk
# import re
# from nltk.probability import FreqDist
# import contractions
# import enchant
#
# d = enchant.Dict("en_US")
# f = open('tweets.json', "r", encoding='utf-8')
# data = json.loads(f.read())
# f.close()
# text = []
# for text_field in data:
#     clrtxt = text_field['text']
#     clrtxt = clrtxt.replace('\n', ' ')
#     clrtxt = clrtxt.replace('RT', '')
#     clrtxt = re.sub(r'http\S+', '', clrtxt)
#     clrtxt = re.sub('@[A-Za-z0-9_]+', '', clrtxt)
#     clrtxt = re.sub('#[A-Za-z0-9]+', '', clrtxt)
#     clrtxt = contractions.fix(clrtxt)
#     clrtxt = clrtxt.replace("'s", '')
#     text.append(clrtxt)
#
# nouns = []
# for string in text:
#     is_noun = lambda pos: pos[:2] == "NN"
#     tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
#     tokenized = tokenizer.tokenize(string)
#     nouns.append([word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos) and d.check(word) or word == 'kind'])
#
# # print(nouns)
# fdist = FreqDist()
# for string in nouns:
#     for word in string:
#         fdist[word.lower()] += 1
#         for suffix in ['s']:
#             if word.endswith(suffix):
#                 fdist[word.lower()[:-len(suffix)]] += 1
#                 fdist.__delitem__(word)
#
# freq = dict(fdist)
# freq_sorted = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True)}
# for idx, (k, v) in enumerate(freq_sorted.items()):
#     if idx == 10:
#         break
#     print(k, v)