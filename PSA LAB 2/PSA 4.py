# 4. Densities
import random

iterations = int(input("Input number of iterations: "))
wc = 0
for i in range(1, iterations + 1):
    bp1 = random.randint(1, 360)
    bp2 = random.randint(1, 360)
    bp3 = random.randint(1, 360)
    ark1 = max(bp1, bp2, bp3) - min(bp1, bp2, bp3)
    ark2 = 360 - max(bp1, bp2, bp3)
    ark3 = min(bp1, bp2, bp3)
    if (ark1/2) < 90 and (ark2/2) < 90 and (ark3/2) < 90:
        wc += 1
print("Probability:", wc/iterations)
# 0.25
