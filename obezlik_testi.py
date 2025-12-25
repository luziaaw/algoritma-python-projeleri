# Algoritma ve Programlama Dersi
# Proje: Obezlik (BKİ) Testi
# Dil: Python

kilo = float(input("Kilonuzu (kg) giriniz: "))
boy = float(input("Boyunuzu (metre) giriniz: "))

bki = kilo / (boy * boy)

print("Vücut Kitle İndeksiniz:", round(bki, 2))

if bki < 18.5:
    print("Durum: Zayıf")
elif bki < 25:
    print("Durum: Normal")
elif bki < 30:
    print("Durum: Fazla Kilolu")
elif bki < 35:
    print("Durum: 1. Derece Obez")
elif bki < 40:
    print("Durum: 2. Derece Obez")
else:
    print("Durum: 3. Derece Obez")
