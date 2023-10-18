# 1. Interesting observation
import random
import matplotlib.pyplot as plt
import collections

games = int(input("Input number of games: "))
gamespltxaxis = []
sumvalues = []
values10yaxis = []
values9yaxis = []
sum10 = 0
sum9 = 0
for i in range(1, games + 1):
    gamespltxaxis.append(i)
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    roll3 = random.randint(1, 6)
    if (roll1 + roll2 + roll3) == 10:
        sum10 += 1
    if (roll1 + roll2 + roll3) == 9:
        sum9 += 1
    values10yaxis.append(sum10)
    values9yaxis.append(sum9)
    # print(roll1, roll2, roll3, roll1 + roll2 + roll3)
    for k in range(3, 18):
        if (roll1 + roll2 + roll3) == k:
            sumvalues.append(k)
# print(sumvalues)
sumdict = collections.Counter(sumvalues)
# print(sumdict)
print("Sum 9:", sum9)
print("Sum 10:", sum10)
plt.subplot(2, 1, 1)
plt.plot(gamespltxaxis, values9yaxis)
plt.plot(gamespltxaxis, values10yaxis)
plt.subplot(2, 1, 2)
numb = list(sumdict.keys())
sum = list(sumdict.values())
plt.bar(numb, sum, color="Red", width=0.3)
plt.title("Evolution of Sums")
plt.xlabel("Games")
plt.ylabel("Values")
plt.show()
# Student is correct, first graph shows that the growth of counter of sum 9 is lower than sum 10,
# second graph represents the appearances of all possible sums, and represent a normal curve.
