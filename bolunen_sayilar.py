# Algoritma ve Programlama Dersi
# Proje 08: Girilen sayıya bölünen sayıları bulma
# Dil: Python

sayi = int(input("Bir sayı giriniz: "))

print("Bu sayıya tam bölünen sayılar:")

for i in range(1, sayi + 1):
    if sayi % i == 0:
        print(i)

