# Algoritma ve Programlama Dersi
# Proje 09: Basit Hesap Makinesi
# Dil: Python

print("1- Toplama")
print("2- Çıkarma")
print("3- Çarpma")
print("4- Bölme")

secim = int(input("Seçiminizi yapınız (1-4): "))

sayi1 = float(input("Birinci sayıyı giriniz: "))
sayi2 = float(input("İkinci sayıyı giriniz: "))

if secim == 1:
    print("Sonuç:", sayi1 + sayi2)
elif secim == 2:
    print("Sonuç:", sayi1 - sayi2)
elif secim == 3:
    print("Sonuç:", sayi1 * sayi2)
elif secim == 4:
    if sayi2 != 0:
        print("Sonuç:", sayi1 / sayi2)
    else:
        print("Bir sayı 0'a bölünemez.")
else:
    print("Geçersiz seçim.")
