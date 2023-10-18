# 2. Densities
import random


wc = 0
iterations = int(input("Input number of iterations: "))
for i in range(1, iterations + 1):
    bp1 = random.uniform(0, 1)
    bp2 = random.uniform(0, 1)
    maxim = max(bp1, bp2)
    minim = min(bp1, bp2)
    s3 = 1 - maxim
    s2 = maxim - minim
    s1 = minim
    if s1 + s2 > s3 and s1 + s3 > s2 and s3 + s2 > s1:
        wc += 1
print("Probability:", wc/iterations)
# 0.25



# # 2. Densities
# import random
#
#
# wc = 0
# for i in range(1, 10001):
#     bp1 = random.randint(1, 100)
#     bp2 = random.randint(1, 100)
#     if bp1 > 50 and bp2 > 50 and bp1 + bp2 > 50:
#         wc += 1
# print("Probability:", wc/10000) # 0.25
