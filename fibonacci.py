# Algoritma ve Programlama Dersi
# Proje 12: Fibonacci Serisi
# Dil: Python

n = int(input("Kaç terim istiyorsunuz?: "))

a = 0
b = 1

print("Fibonacci serisi:")

for i in range(n):
    print(a)
    a, b = b, a + b

