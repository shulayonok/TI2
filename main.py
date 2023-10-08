import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import math

symbols = []
quantity = []
isOk = False
count = 0

# Считывание текста
with open("Nose.txt", "r") as file:
    string = file.read()

# Подсчёт того, сколько раз встречается каждая буква
for sign in string:
    for i in range(len(symbols)):
        if sign.lower() == symbols[i]:
            quantity[i] += 1
            count += 1
            isOk = True
    if not isOk and sign != '\n' and sign != '\xa0':
        symbols.append(sign.lower())
        quantity.append(1)
        count += 1
    isOk = False

# Оценка вероятности каждого символа
for i in range(len(quantity)):
    quantity[i] /= count
plt.bar(symbols, quantity)
plt.show()

# Подсчет энтропии
ent = 0
for p in quantity:
    ent += p * math.log2(1/p)
print("Энтропия символа:", ent)
print("Общая энтропия книги:", ent*count)

# Загрузка и конвертация изображения в ч/б
img = Image.open('nos.jpg').convert("L")
(width, height) = img.size
img = img.load()

# Вычисление интесивностей
intens = np.zeros(256)
for i in range(width):
    for j in range(height):
        intens[img[i, j]] += 1

# Оценка вероятности каждой интенсивности пикселя
for pix in range(len(intens)):
    intens[pix] /= (width*height)
plt.scatter(np.arange(256), intens, s=10, c="#9c3b7d")
plt.show()

# Подсчет энтропии
ent = 0
for p in range(len(intens)):
    if intens[p] != 0:
        ent += intens[p] * math.log2(1/intens[p])
print("Энтропия пикселя:", ent)
print("Общая энтропия изображения:", ent*width*height)

