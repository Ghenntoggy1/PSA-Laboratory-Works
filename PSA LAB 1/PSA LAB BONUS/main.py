# Bonus:
import random
from PIL import Image

image = Image.open("danger_zone.png")
redarea = 0
bluearea = 0
for i in range(1, 10001):
    x = random.randint(0, 3199)
    y = random.randint(0, 1529)
    coordinate = (x, y)
    color = image.getpixel(coordinate)
    if color == (255, 0, 0, 255):
        redarea += 1
    if color == (0, 0, 255, 255):
        bluearea += 1
redareaout = redarea / 10000 * 42
blueareaout = bluearea / 10000 * 42
print("Dangerous Area: ", redareaout, "square miles")
print("Safe Area: ", blueareaout, "square miles")
print("Check: ", redareaout + blueareaout)
