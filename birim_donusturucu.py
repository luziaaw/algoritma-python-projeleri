# Algoritma ve Programlama Dersi
# Proje: Metre Birim Dönüştürücü
# Dil: Python

metre = float(input("Metre cinsinden değeri giriniz: "))

print("\nDönüştürmek istediğiniz birimi seçiniz:")
print("1 - Milimetre (mm)")
print("2 - Desimetre (dm)")
print("3 - Santimetre (cm)")
print("4 - Kilometre (km)")

secim = input("Seçiminiz (1-2-3-4): ")

if secim == "1":
    print("Sonuç:", metre * 1000, "mm")
elif secim == "2":
    print("Sonuç:", metre * 10, "dm")
elif secim == "3":
    print("Sonuç:", metre * 100, "cm")
elif secim == "4":
    print("Sonuç:", metre / 1000, "km")
else:
    print("Hatalı seçim yaptınız.")

