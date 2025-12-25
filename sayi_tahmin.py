# Algoritma ve Programlama Dersi
# Proje 07: Sayı Tahmin Oyunu (Gelişmiş)
# Dil: Python

import random

tutulan_sayi = random.randint(1, 10)
tahmin_hakki = 3

print("1 ile 10 arasında bir sayı tuttum.")
print("3 tahmin hakkınız var.")

while tahmin_hakki > 0:
    tahmin = int(input("Tahmininizi giriniz: "))

    if tahmin == tutulan_sayi:
        print("Tebrikler! Doğru tahmin.")
        break
    elif tahmin > tutulan_sayi:
        print("Daha küçük bir sayı giriniz.")
    else:
        print("Daha büyük bir sayı giriniz.")

    tahmin_hakki -= 1

    if tahmin_hakki > 0:
        print("Kalan tahmin hakkı:", tahmin_hakki)
    else:
        print("Tahmin hakkınız bitti.")
        print("Tutulan sayı:", tutulan_sayi)

