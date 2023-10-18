# 4.1 Popular
import json
import nltk
import re
from nltk.probability import FreqDist
from nltk.corpus import stopwords
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
    clrtxt = clrtxt.replace("FW:", '')
    clrtxt = clrtxt.replace("Stack Overflow", "StackOverflow")
    clrtxt = clrtxt.replace("iPad Pro", "IpadPro")
    clrtxt = clrtxt.replace("CPU", 'cpu')
    clrtxt = clrtxt.replace("Do", 'do')
    clrtxt = clrtxt.replace("New", 'new')
    clrtxt = clrtxt.replace(' A ', 'a')
    clrtxt = contractions.fix(clrtxt)
    clrtxt = clrtxt.replace("'s", '')
    text.append(clrtxt)

# print(text)
propnouns = []
for string in text:
    is_noun = lambda pos: pos == "NNP" or pos == "NNPS"
    tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
    tokenized = tokenizer.tokenize(string)
    propnouns.append([word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos) and word not in set(stopwords.words('english'))])
# print(propnouns)
fdist = FreqDist()
for string in propnouns:
    for word in string:
        fdist[word.lower()] += 1

freq = dict(fdist)
freq_sorted = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True)}
for idx, (k, v) in enumerate(freq_sorted.items()):
    if idx == 10:
        break
    print(k, v)




# import nltk
# import re
# import enchant
# from nltk.probability import FreqDist
# import json
#
# d = enchant.Dict("en_US")
# f = open('tweets.json', "r", encoding='utf-8')
# data = json.loads(f.read())
# f.close()
# text = []
# for text_field in data:
#     text.append(text_field['text'])
# propnouns = []
# for i in text:
#     is_noun = lambda pos: pos == "NNP"
#     str0 = re.sub(r"http\S+", "", i)
#     stra = re.sub(r'[^\w\s]', '', str0)
#     tokenized = nltk.word_tokenize(stra)
#     propnouns.append([word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos) and d.check(word) and word != "RT"])
# print(propnouns)
# freq = FreqDist()
# for string in propnouns:
#     for word in string:
#         freq[word.lower()] += 1
# print(repr(freq))
# freq_sorted = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True)}
# for idx, (k, v) in enumerate(freq_sorted.items()):
#     if idx == 10:
#         break
#     print(k, v)