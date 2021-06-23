def tcsorgulama():
    pass


teksira = 0
cifsira = 0
sonuc = 0
toplam = 0
print("Lütfen gecerli bir Tc Giriniz : ")
tc = input()

for x in range(0, 10, 2):  # 1,3,5,7,9. indeksleri topladım
    teksira += int(tc[x])
    print("Tek indexlerin toplamı : ", teksira)

teksira *= 7  # 7 katını alıyorum burada

print("tek indexlerin toplamının 7 katı : ", teksira)

for x in range(1, 9, 2):  # 2,4,6,8. hanelerin toplamı
    cifsira += int(tc[x])
    print("cif indexlerin toplamı :  ", cifsira)

sonuc = teksira - cifsira  # 7 katı alınmıs tek sıra ile cif sırayı direkt cıkarıyoruz
print("aralarındaki fark", sonuc)
sonuc = sonuc % 10  # burda sonucun mod10 u alınca bize 10. haneyi veriyor
if sonuc == int(tc[9]):
    print("Tc nizi yanlış girdiniz ! tekrar deneyiniz ! ! !")

print("10 a bölümünden kalan sonuc yani 10. HANE  ", sonuc)

for x in range(0, 10):  # burada tc kimlik no sunun son rakamını buluyoruz tüm rakamların toplamının mod 10 alıyoruz
    toplam += int(tc[x])
    print("1. haneden 10. hanete kadar rakamların toplamı :  ", toplam)
toplam = toplam % 10
print("1. haneden 10. hanete kadar rakamların toplamının 10 a bölümünden kalanı : ", toplam)
print("Son HANE:", toplam)
