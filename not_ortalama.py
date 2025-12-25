# Algoritma ve Programlama Dersi
# Proje 05: Not Ortalaması Hesaplama
# Dil: Python

vize = float(input("Vize notunu giriniz: "))
final = float(input("Final notunu giriniz: "))

ortalama = (vize * 0.4) + (final * 0.6)

print("Not ortalamanız:", ortalama)

if ortalama >= 60:
    print("Dersten geçtiniz.")
else:
    print("Dersten kaldınız.")
