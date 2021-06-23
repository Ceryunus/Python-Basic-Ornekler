# Fonksiyona uygulanmış  şekilde tc doğrulama ayrıntılısı TcSorgulama1 de

def tcsorgulama(tc):
    teksira = 0
    cifsira = 0
    sonuc = 0
    toplam = 0

    for x in range(0, 10, 2):
        teksira += int(tc[x])

    teksira *= 7

    for x in range(1, 9, 2):
        cifsira += int(tc[x])

    sonuc = (teksira - cifsira) % 10

    if sonuc != int(tc[9]):
        return "Girilen Tc Hatali"
    else:
        for x in range(0, 10):
            toplam += int(tc[x])

        toplam = toplam % 10

        if toplam != int(tc[10]):
            return "Girilen Tc Hatali"
        return "Girilen Tc dogru"


print("Lütfen bir Tc giriniz : ")
tc = input()
print(tcsorgulama(tc))
