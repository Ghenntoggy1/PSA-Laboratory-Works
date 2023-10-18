# 4.1 Popular
import json
import nltk
import re
from nltk.probability import FreqDist
import contractions


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
    text.append(clrtxt)

string_list = []
for string in text:
    str1 = nltk.RegexpTokenizer(r"\w+")
    str2 = str1.tokenize(string)
    string_list.append(str2)

# print(string_list)
fdist = FreqDist()
for string in string_list:
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
# from nltk.probability import FreqDist
# import json
#
# f = open('tweets.json', "r", encoding='utf-8')
# data = json.loads(f.read())
# f.close()
# text = []
# for text_field in data:
#     text.append(text_field['text'])
# strings_list = []
# for string in text:
#     str0 = re.sub(r"http\S+", "", string)
#     # stra = re.sub(r'(.)\1+', r'\1', str0)
#     # strb = re.compile(r'(\w)\1*')
#     # match_sub = r'\1'
#     # stra = strb.sub(match_sub, str0)
#     str1 = nltk.RegexpTokenizer(r"\w+")
#     str2 = str1.tokenize(str0)
#     strings_list.append(str2)
# fdist = FreqDist()
# for string in strings_list:
#     for word in string:
#         fdist[word.lower()] += 1
# # print(strings_list)
# freq = dict(fdist)
# print(repr(fdist))
# freq_sorted = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True)}
# # elem = {key: value for key, value in list(freq_sorted.items())[0:10]}
# for idx, (k, v) in enumerate(freq_sorted.items()):
#     if idx == 10:
#         break
#     print(k, v)
# # print(fdist.most_common(10))
