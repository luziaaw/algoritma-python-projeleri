# Algoritma ve Programlama Dersi
# Proje: Basit Pandas Örneği
# Dil: Python

import pandas as pd

# Basit veri
veri = {
    "Öğrenci": ["meltem", "aleyna", "ayse"],
    "Not": [85, 70, 90]
}

# DataFrame oluştur
df = pd.DataFrame(veri)

# Ekrana yazdır
print(df)
