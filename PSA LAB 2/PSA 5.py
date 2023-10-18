# 5. Densities
import random
import math

realroots = 0
positiveroots = 0
iterations = int(input("Input number of iterations: "))
for i in range(1, iterations+1):
    b = random.uniform(-1, 1)
    c = random.uniform(-1, 1)
    delta = math.pow(b, 2) - 4*c
    if delta < 0:
        continue
    else:
        root1 = (-b + math.sqrt(delta)) / 2
        root2 = (-b - math.sqrt(delta)) / 2
        realroots += 1
        if root1 > 0 and root2 > 0:
            positiveroots += 1
print("Real Roots:", realroots/iterations)  # 0.54
print("Positive Roots:", positiveroots/iterations)  # 0.02
