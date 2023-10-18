# 2. Densities
import random

lc = 0
iterations = int(input("Input number of iterations: "))
for i in range(1, iterations + 1):
    bp1 = random.uniform(0, 1)
    st1 = 1 - bp1
    st2 = 1 - st1
    longst = max(st1, st2)
    shortst = min(st1, st2)
    bp2 = random.uniform(0, longst)
    st3 = longst - bp2
    st4 = longst - st3
    maxlen = max(shortst, st4, st3)
    if maxlen >= 0.5:
        lc += 1
print((iterations - lc) / iterations)
# 0.38
