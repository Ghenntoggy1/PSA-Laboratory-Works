# 6. Densities
import random
import matplotlib.pyplot as plt

games = int(input("Input number of games: "))
pocketlist = []
x = 0
for j in range(1, 1001):
    wc = 0
    pocket = 0.25
    for i in range(1, games + 1):
        xcoord = random.uniform(0, 1)
        ycoord = random.uniform(0, 1)
        pocket -= 0.25
        if 0.75 >= xcoord >= 0.25 and 0.75 >= ycoord >= 0.25:
            wc += 1
            pocket += 1
        else:
            continue
    pocketlist.append(pocket)
    x += wc/games

print("Probability:", x/1000)
sum = 0
for i in pocketlist:
    sum += i
# gamesxaxis = []
# for i in range(1, 1001):
#     gamesxaxis.append(i)
# print(sum)
kjk = 0
for i in pocketlist:
    kjk += i
print(pocketlist)
print(kjk/len(pocketlist))
# plt.plot(gamesxaxis, pocketlist)
# plt.title("Variation of pocket bank")
# plt.xlabel("Iteration")
# plt.ylabel("Pocket Bank")
# plt.show()

# Fluctuates around 0, therefore 0.25 bet will grant mean value of winnings around 0.
# Same probability for more squares, so no need to compute for a full checkerboard - enough one square

# # 6. Densities
# import random
# import matplotlib.pyplot as plt
#
# games = int(input("Input number of games: "))
# pocketlist = []
# x = 0
# for j in range(1, 1001):
#     wc = 0
#     pocket = 0.25
#     for i in range(1, games + 1):
#         xcoord = random.uniform(0, 2)
#         ycoord = random.uniform(0, 2)
#         pocket -= 0.25
#         if (0.75 >= xcoord >= 0.25 and 0.75 >= ycoord >= 0.25) or (1.75 >= xcoord >= 1.25 and 0.75 >= ycoord >= 0.25) or (
#                 0.75 >= xcoord >= 0.25 and 1.75 >= ycoord >= 1.25) or (1.75 >= xcoord >= 1.25 and 1.75 >= ycoord >= 1.25):
#             wc += 1
#             pocket += 1
#         else:
#             continue
#     pocketlist.append(pocket)
#     x += wc/games
#
# print("Probability:", x/1000)
# sum = 0
# for i in pocketlist:
#     sum += i
# gamesxaxis = []
# for i in range(1, 1001):
#     gamesxaxis.append(i)
# plt.plot(gamesxaxis, pocketlist)
# plt.title("Variation of pocket bank")
# plt.xlabel("Iteration")
# plt.ylabel("Pocket Bank")
# plt.show()
# # Fluctuates around 0, therefore 0.25 bet will grant mean value of winnings around 0.