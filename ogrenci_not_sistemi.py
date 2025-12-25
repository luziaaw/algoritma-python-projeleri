# Algoritma ve Programlama Dersi
# Proje: Öğrenci Not Giriş Sistemi (e-okul mantığı)
# Dil: Python

ogrenciler = {}

ogrenci_sayisi = int(input("Kaç öğrenci notu girilecek?: "))

for i in range(ogrenci_sayisi):
    print("\n", i + 1, ". öğrenci")

    ad = input("Öğrenci adı: ")
    notu = int(input("Öğrenci notu: "))

    ogrenciler[ad] = notu

print("\n--- NOT LİSTESİ ---")
for ad, notu in ogrenciler.items():
    print(ad, ":", notu)

print("\nNot girişi tamamlandı. Program sonlandırıldı.")


