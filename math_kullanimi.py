# Algoritma ve Programlama Dersi
# Proje 16: Math Kütüphanesi Kullanımı
# Dil: Python

import math

sayi = float(input("Bir sayı giriniz: "))

print("Sayının karekökü:", math.sqrt(sayi))
print("Sayının karesi:", math.pow(sayi, 2))

yari_cap = float(input("Dairenin yarıçapını giriniz: "))
alan = math.pi * math.pow(yari_cap, 2)

print("Dairenin alanı:", alan)
