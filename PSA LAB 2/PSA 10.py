# 10. Important Distributions
import numpy as np
import matplotlib.pyplot as plt

# take a year with 365 days, therefore 730 trips
iterations = int(input("Input number of iterations: "))
pocketval = []
summoney = 0
for i in range(1, iterations + 1):
    dc = 0
    c = 0
    cp = 0
    pocket = 0
    for j in range(1, 731):
        posib = ["DC", "C", "CP"]  # DC = Didn't get caught, C = Got Caught, CP = Got caught by a muscular hairy taxator
        trip = np.random.choice(posib, 1, p=[0.93, 0.05, 0.02])
        if trip == "DC":
            dc += 1
        elif trip == "C":
            c += 1
        elif trip == "CP":
            cp += 1
    # pocket += dc * 6  # intreb de fistic
    if c == 1:
        pocket -= 50
    elif c == 2:
        pocket -= 200
    else:
        pocket -= ((c - 2) * 300 + 150 + 50)
    pocket -= cp * 6
    pocketval.append(pocket)
for i in pocketval:
    summoney += i
iterlist = []
for i in range(1, iterations+1):
    iterlist.append(i)
jora = round(summoney/len(pocketval))
student = 0 - 6*730
print("Jora Petrovici spends:", jora)
print("Law-abiding Student spends:", student)
print("Ratio:", round(jora/student, 3))
plt.plot(iterlist, pocketval)
plt.show()
