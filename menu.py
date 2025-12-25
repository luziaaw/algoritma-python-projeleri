# Algoritma ve Programlama Dersi
# Proje 13: Basit Menü Uygulaması
# Dil: Python

while True:
    print("1- Merhaba Yaz")
    print("2- Toplama Yap")
    print("3- Çıkış")

    secim = int(input("Seçiminizi giriniz: "))

    if secim == 1:
        print("Merhaba Ayşe!")
    elif secim == 2:
        a = int(input("Bir sayı giriniz: "))
        b = int(input("Bir sayı giriniz: "))
        print("Toplam:", a + b)
    elif secim == 3:
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz seçim.")

