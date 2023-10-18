# 4.4 Frequency
import json
import nltk
import re
import contractions
import matplotlib.pyplot as plt
from collections import defaultdict, Counter

sword = input("Input searched word: ")
f = open('tweets.json', "r", encoding='utf-8')
data = json.loads(f.read())
f.close()
c = 0
dic = defaultdict(int)
for text_field in data:
    clrtxt = text_field['text']
    clrtxt = clrtxt.replace('RT', '')
    clrtxt = re.sub(r'http\S+', '', clrtxt)
    clrtxt = re.sub('@[A-Za-z0-9_]+', '', clrtxt)
    clrtxt = re.sub('#[A-Za-z0-9]+', '', clrtxt)
    clrtxt = contractions.fix(clrtxt)
    str1 = nltk.RegexpTokenizer(r"\w+")
    str2 = str1.tokenize(clrtxt)
    str3 = [x.lower() for x in str2]
    if sword in str3:
        co = Counter(str3)
        dic[text_field['created_at'][:7]] += co[sword]
        c += co[sword]

# print(dic)
print(c)
plt.bar(dic.keys(), dic.values())
plt.xlabel("Months")
plt.ylabel(f"Frequency of word: {sword}")
plt.show()
