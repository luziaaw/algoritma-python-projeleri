# Algoritma ve Programlama Dersi
# Proje: pickle ile veri kaydetme ve okuma
# Dil: Python

import pickle

# Kaydedilecek veri
notlar = [70, 85, 90, 60]

# Dosyaya yazma
with open("notlar.pkl", "wb") as dosya:
    pickle.dump(notlar, dosya)

print("Veriler dosyaya kaydedildi.")

# Dosyadan okuma
with open("notlar.pkl", "rb") as dosya:
    okunan_notlar = pickle.load(dosya)

print("Dosyadan okunan veriler:", okunan_notlar)
