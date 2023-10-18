# 1. Important Distributions
import random

iterations = int(input("Input number of iterations: "))
ap_8 = []
o = 0
flag = True
for n in range(200, 10100, 50):
    mean = 0
    for i in range(1, iterations + 1):
        tagged = []
        tagged2 = 0
        for j in range(1, 51):
            d = random.randint(1, n)
            tagged.append(d)
        for j in range(1, 201):
            d = random.randint(1, n)
            if d in tagged:
                tagged2 += 1
        mean += tagged2
    f = "{:.3f}".format(mean/iterations)
    if round(float(f)) == 8:
        if flag:
            print('-------' * 25)
            flag = False
        print(f"In a population of {n} total deers, {round(float(f))} tagged deers found ")
        ap_8.append(n)
        o += n
    elif float(f) < 7:
        break
print('-------' * 25)
print("Population of deers in Codrii Reserve by Simulations:", o//len(ap_8))
print('-------' * 25)
print("Population of deers in Codrii Reserve by Mathematical Formula:", (50/8)*200)