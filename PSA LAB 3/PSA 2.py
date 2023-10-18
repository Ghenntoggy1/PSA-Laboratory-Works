# 2. Continuous Conditional probability
import random
import math

iterations = int(input("Input number of iterations: "))
rs = 0
less = 0
greater = 0
another = 0
for i in range(1, iterations + 1):
    x_coord = 0
    y_coord = 0
    flag = True
    while flag:
        x_c = random.uniform(-10, 10)
        y_c = random.uniform(0, 10)
        if math.pow(x_c, 2) + math.pow(y_c, 2) <= 100:
            x_coord = x_c
            y_coord = y_c
            flag = False
    if x_coord >= 0:
        rs += 1
    if math.pow(x_coord, 2) + math.pow(y_coord, 2) <= 25:
        less += 1
    if math.pow(x_coord, 2) + math.pow(y_coord, 2) >= 25:
        greater += 1
    if (math.pow(x_coord - 0, 2) + math.pow(y_coord - 5, 2)) >= 25:
        another += 1
print("Porbability of hitting Right Side of Target:", rs/iterations)
print("Porbability of Darts distance from the center is less than 5 inches :", less/iterations)
print("Porbability of Darts distance from the center is greater than 5 inches :", greater/iterations)
print("Porbability of landing within 5 inches of the point (0, 5):", another/iterations)
