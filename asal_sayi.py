# Algoritma ve Programlama Dersi
# Proje 06: Asal Sayı Kontrolü
# Dil: Python

sayi = int(input("Bir sayı giriniz: "))
asal = True

if sayi <= 1:
    asal = False
else:
    for i in range(2, sayi):
        if sayi % i == 0:
            asal = False
            break

if asal:
    print("Girilen sayı asaldır.")
else:
    print("Girilen sayı asal değildir.")
