# 8. Densities
import random
# Oricare doua perechi de persoane
games = int(input("Input number of games: "))
c = 0
for x in range(games):
    lunch = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    dinner = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    random.shuffle(lunch)
    random.shuffle(dinner)
    lunch.append(lunch[0])
    dinner.append(dinner[0])
    # print(lunch, dinner)
    nexttoeachother = False
    if not nexttoeachother:
        for i in range(10):
            for j in range(10):
                # print(dinner[j])
                if (lunch[i] == dinner[j] and lunch[i+1] == dinner[j+1]):
                    nexttoeachother = True
                    # print(lunch[i], lunch[i+1])
                    # print(lunch[i], dinner[j+1])
                elif (lunch[i] == dinner[j] and lunch[i+1] == dinner[j-1]):
                    # print(lunch[i], lunch[i + 1])
                    # print("a b a b:",lunch[i], dinner[j - 1])
                    nexttoeachother = True
                elif lunch[i] == dinner[j] and lunch[i+1] == dinner[9] and dinner[10] == lunch[i]:
                    nexttoeachother = True
                    # print("check", lunch[i], dinner[9])
    if nexttoeachother:
        c += 1
        # print("c =", c)
print("Probability:", (games - c)/games)

# # 8. Densities
# import random
# import math
# games = int(input("Input number of games: "))
# lcl = 0
# lcd = 0
# for i in range(1, games + 1):
#     placesl = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     place1l = random.choice(placesl)
#     placesl.remove(place1l)
#     place2l = random.choice(placesl)
#     if (place1l == 10 and place2l == 1) or (place2l == 10 and place1l == 1) or (place1l + 1 == place2l) or (
#             place2l + 1 == place1l):
#         lcl += 1
#     placesd = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     place1d = random.choice(placesd)
#     placesd.remove(place1d)
#     place2d = random.choice(placesd)
#     if (place1d == 10 and place2d == 1) or (place2d == 10 and place1d == 1) or (place1d + 1 == place2d) or (
#             place2d + 1 == place1d):
#         lcd += 1
# print("Probability:", (games - lcl)/games * (games - lcd)/games)
# # 0.6

# # 8. Densities
# import random
# # Oricare doua perechi de persoane
# games = int(input("Input number of games: "))
# c = 0
# for x in range(games):
#     lunch = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     dinner = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     random.shuffle(lunch)
#     random.shuffle(dinner)
#     lunch.append(lunch[0])
#     dinner.append(dinner[0])
#     print(lunch, dinner)
#     nexttoeachother = False
#     if not nexttoeachother:
#         for i in range(10):
#             for j in range(10):
#                 if lunch[i] == dinner[j] and lunch[i+1] == dinner[j+1]:
#                     nexttoeachother = True
#                     # print(lunch[i], lunch[i+1])
#                     print(lunch[i], dinner[j+1])
#                 elif lunch[i] == dinner[j] and lunch[i+1] == dinner[j-1]:
#                     # print(lunch[i], lunch[i + 1])
#                     print(lunch[i], dinner[j - 1])
#                     nexttoeachother = True
#         if nexttoeachother:
#             c += 1
#             print("c =", c)
# print("Probability:", (games - c)/games)