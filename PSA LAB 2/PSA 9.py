# 9. Random Variable
import random
import matplotlib.pyplot as plt

games = int(input("Input number of games: "))
tot = []
for i in range(1, games + 1):
    yval = []
    x = random.uniform(0, 1)
    while True:
        y = random.uniform(0, 1)
        if y <= x:
            yval.append(y)
        else:
            yval.append(y)
            # print("i =", len(yval))
            # print(y)
            # print(yval)
            # print(x)
            break
    tot.append(len(yval))
sum = 0
for i in tot:
    sum += i
# print(sum)
# print(len(tot))
# print(sum)
# print(tot)
gamesxaxis = []
for i in range(1, games + 1):
    gamesxaxis.append(i)
print("Expected Value:", sum/len(tot))
plt.plot(gamesxaxis, tot)
plt.show()
# Willing to pay any amount of money, sum is changing when increasing number of games.





# # 9. Random Variable
# import random
# import matplotlib.pyplot as plt
#
# games = int(input("Input number of games: "))
# expval = []
# for j in range(1, 101):
#     tot = []
#     for i in range(1, games + 1):
#         yval = []
#         x = random.uniform(0, 1)
#         while True:
#             y = random.uniform(0, 1)
#             if y <= x:
#                 yval.append(y)
#             else:
#                 yval.append(y)
#                 break
#         tot.append(len(yval))
#     sum = 0
#     for i in tot:
#         sum += i
#     e = sum/len(tot)
#     # print("Expected Value:", e)
#     expval.append(e)
# gamesxaxis = []
# for i in range(1, 101):
#     gamesxaxis.append(i)
# sum2 = 0
# for i in expval:
#     sum2 += i
# print("ExpValMed:", sum2 / 100)
# plt.plot(gamesxaxis, expval)
# plt.show()