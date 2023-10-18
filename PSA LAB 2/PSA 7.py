# 7. Densities
import random
import matplotlib.pyplot as plt
import collections

headlist = []
for i in range(1, 1001):
    n = 0
    for k in range(1, 101):
        flip = random.choice(["Heads", "Tails"])
        if flip == "Heads":
            n += 1
    for j in range(35, 66):
        if n == j:
            headlist.append(n)
# print(headlist)
count = collections.Counter(headlist)
# print(count)
xaxis1 = count.keys()
yaxis1 = count.values()
plt.subplot(2, 1, 1)
plt.bar(xaxis1, yaxis1, color="Red", width=0.4)
plt.title("Curve of Heads appearances 1000 iterations")
plt.xlabel("Values of n")
plt.ylabel("Number of appearances")
headlist2 = []
for i in range(1, 100001):
    n = 0
    for k in range(1, 101):
        flip = random.choice(["Heads", "Tails"])
        if flip == "Heads":
            n += 1
    for j in range(35, 66):
        if n == j:
            headlist2.append(n)
count2 = collections.Counter(headlist2)
xaxis2 = count2.keys()
yaxis2 = count2.values()
plt.subplot(2, 1, 2)
plt.bar(xaxis2, yaxis2, color="Red", width=0.4)
plt.title("Curve of Heads appearances 1000000 iterations")
plt.xlabel("Values of n")
plt.ylabel("Number of appearances")
plt.show()
# Represents normal curve. Better seen when increased number of iterations of the experiment
