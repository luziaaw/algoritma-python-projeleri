# Algoritma ve Programlama Dersi
# Proje 04: 1'den N'e kadar olan sayıların toplamı
# Dil: Python

n = int(input("Bir sayı giriniz: "))
toplam = 0

for i in range(1, n + 1):
    toplam += i

print("Toplam:", toplam)
