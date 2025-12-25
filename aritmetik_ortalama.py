# Algoritma ve Programlama Dersi
# Proje: Aritmetik Ortalama Hesaplama
# Dil: Python

toplam = 0
adet = int(input("Kaç tane sayı gireceksiniz?: "))

for i in range(adet):
    sayi = float(input(f"{i + 1}. sayıyı giriniz: "))
    toplam += sayi

ortalama = toplam / adet
print("Aritmetik ortalama:", ortalama)
