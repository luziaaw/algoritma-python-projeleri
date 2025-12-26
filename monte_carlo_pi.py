# Algoritma ve Programlama Dersi
# Proje: Monte Carlo Yöntemi ile Pi Sayısı Hesaplama
# Dil: Python

import random

n = int(input("Rastgele nokta sayısını giriniz: "))
m = 0

for i in range(n):
    x = 2 * random.random() - 1
    y = 2 * random.random() - 1

    if x**2 + y**2 <= 1:
        m += 1

pi = 4 * m / n
print("Yaklaşık pi değeri:", pi)
