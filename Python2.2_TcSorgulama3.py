# Ayrıntısı TcSorgulama1
def TcDogrulama(tc):  # str->bool
    cifindextop = 0
    tekindextop = 0
    index = 1
    for numbers in tc:
        if index >= 10:
            break
        elif (index % 2) == 0:
            cifindextop += int(numbers)
        else:
            tekindextop += int(numbers)
        index += 1
    tekindextop2 = tekindextop * 7
    onuncuhane = (tekindextop2 - cifindextop) % 10

    if onuncuhane != int(tc[9]):
        return False
    else:
        sonhane = (tekindextop + cifindextop + onuncuhane) % 10

        if sonhane != int(tc[10]):
            return False
    return True


print("Lütfen bir Tc giriniz : ")
tc = input()
if len(tc) == 11:
    if TcDogrulama(tc) == True:
        print("Doğru Bir Tc Girdiniz")
    else:
        print("Yanlış Bir Tc Girdiniz !!!")
else:
    print("Hatalı giriş !")
