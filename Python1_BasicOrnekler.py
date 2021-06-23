# Basic sorular ornekler
import math  # matematik modülü

# SORU1-------------------

print("Hello World")
# SORU2-------------------İsmini yazdır
a = "yunus"
print(a * 98)

# SORU3-------------------
for x in range(98):
    print("Yunus Emre")

# SORU4-------------------
i = 0
while i < 98:
    print("yunus emre")
    i += 1

# SORU5------------------
a = 4
b = 3 ** 2
print("diktörtgenin alanı : ", a * b)
# SORU4 2. yöntemi-------------------
a = float(input("diktortgenin kısa kenarını giriniz "))
b = float(input("diktortgenin uzun kenarını giriniz "))
print("dikdörtgenin alanı :  ", a * b)

# SORU6-------------------

bolum = "bilgisayar programciligi"
print(bolum)
print(list(bolum))
# bolum[0:9] de kullaanabilriz
for x in range(len(bolum)):
    print(bolum[x])

# SORU7-------------------rakamları yazdır
i = 0
while i < 10:

    print("-----------%d-----------" % (i + 1))
    for rakamlar in range(10):
        print(rakamlar)
    i = i + 1

# SORU8-------------------Girilen bilgiyi listeye koyma
a = input("İsminizi giriniz:")
b = input("Soyadınızı giriniz:")
c = int(input("Okul numaranızı giriniz:"))
bilgi = [a, b, c]
print(bilgi)

# basit örnekler ve matematiksel hesaplar

sayi = "okul numaranızı 61"
print(len(sayi))  # metinin uzunluğunu verir len(deyisken).
print(sayi.upper())  # bütün harfleri büyük yazar.
print(sayi.lower())  # bütün harfleri kücük yazdırır.
print(sayi.capitalize())  # metnin ilk harfini sadece büyük yazar.

# -----------datanın icindekileri bulma-----------------
okul = "Antalya Bilim Universitesi"
print(okul.find("Bilim"))  # "Bilim" kelimesi kacıncı karakterden sonra başladığını gösteriyor bosluklar da dahil.
print(okul.startswith("Ant"))  # datanın "Ant" ile basladıgını sorgular ve bool olarak döndürür
print(okul.endswith("tesi"))  # datanın "testi" ile bittiğini sorgular ve bool olarak döndürür

# ----------karakteri cümlelere ayırma-------------------
okul23 = "Antalya,Bilim,Universite"
print(okul23.split(","))  # icerisine yazılan karakterre gördüğünde herbirşeyi ayırır

# -----------------veriyi deryiştirme--------
veri = "En büyük rte"
print(veri)
print(veri.replace("rte", "yanlıs yazmısım Mustafa Kemal Atatürk !"))

# ------------veri dönüştürme-----------
# str() , int() , float()
asd = "123"
print(asd)
print(float(asd))

# ------------slicing komutu---------
sayım = "123456789"

print(sayım[::])  # bütün veriyi yazdırır
print(sayım[::2])  # 2 ser atlayark yazdırır
print(sayım[::-1])  # tersten yazdırır

# -----------ornek1 input alma -----
print("a sayınısı giriniz")
a = float(input())
print("b sayınısı giriniz")
b = float(input())
print("c sayınısı giriniz")
c = float(input())
print("a=", a)
print("b=", b)
print("c=", c)
print("a+b : ", (a + b))
print("a-b : ", (a - b))
print("a*b : ", (a * b))
print("2 üzeri a+b", 2 ** (a + b))

# ---------ornek 2---2.derceden denklem-----
a = float(input("Denklemin a sını giriniz : "))
b = float(input("Denklemin b sını giriniz : "))
c = float(input("Denklemin c sını giriniz : "))
delta = b ** 2 - (4 * a * c)
kok1 = (b + (delta ** (1 / 2))) / 2 * a
kok2 = (-b - (delta ** (1 / 2))) / 2 * a
print("1. Kök : ", kok1)
print("2. Kök : ", kok2)

# -------ornek 3 kare farkı -----------------
print("x i giriniz : ")
x = float(input())
print("y i giriniz : ")
y = float(input())
print(x ** 3 - y ** 3)
print(x ** 2 - y ** 2)
print((x - y) ** 3)
print((x + y) ** 2)
# -------ornek 4---cemberin cevresi ve alanı------

print("Çemberin çapını giriniz : ")
cap = float(input())
print("Cemberin çevresi", 2 * cap * math.pi)
print("Cemberin alanı", 2 * cap ** 2)


# ---------kendi örneğim function kullanarak 2.dereceden denklem bulma
def kokbulma(a, b, c):
    deltah = (b ** 2) - (4 * a * c)
    kok = (b + (deltah ** (1 / 2))) / 2 * a
    return kok


print("Denklemin a sını giriniz : ")
a = float(input())
print("Denklemin b sını giriniz : ")
b = float(input())
print("Denklemin c sını giriniz : ")
c = float(input())
kokbulma(a, b, c)
print("1. Kök : ", kokbulma(a, b, c))
print("2. Kök : ", -kokbulma(a, b, c))

# ---------kendi ornegim bir isimin 3 ile 15 karakter arasında olması
# isim.count("a") isim stringinin icinde kac adaet a harfi olduğunu gösterir

while True:
    print("Bir isim giriniz")
    isim = input()
    if isim == "quit":
        break
    uzunluk = len(isim)
    if uzunluk < 3:
        print("İsminiz cok kısa")
    elif uzunluk > 15:
        print("İsminiz cok uzun")
    else:
        print("Hosgeldin " + isim)
        break
