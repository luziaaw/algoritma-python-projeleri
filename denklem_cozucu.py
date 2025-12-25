b = int(input("b değerini girin: "))

cozumler = [a for a in range(0, 101) if a**3 - a**2 == b]
  
if cozumler:
    print("a^3 - a^2=b")
    print("Çözümler (a):", cozumler)
else:
    print("a^3 - a^2=b")
    print("0 ile 100 arasında hiç çözüm yok.")