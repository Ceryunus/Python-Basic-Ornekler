# *args *kwargs !Bir fonksiyona istediğiöiz kadar argüman gönderme
# (1) Sorun multiply functionu argümanlarını süreki eklemek


def multiply(x, y, z):
    return (x * y * z)


print(multiply(2, 3, 4))


# --------------------------------------
# (2)Burada bu sorunu ortadan kaldırıyoruz
# function un  icine *numbers koyarak burada önemli olan * dır
# burada *numbers bir tuple dır (demet demetlerin icindeki verileri deyistiremezsin)


def multiply(*numbers):
    print(numbers)
    print(type(numbers))


print(multiply(2, 3, 4))


# --------------------------------------
# (3) 1 deki sorunun çözümü
# 2. özellik olarak sadece sayıların burada caprılması gerektiğini söylüyorum cünkü 
# tuple larda bir metin de olabilir bu da bize hata verdirtir


def multiply(*numbers):
    result = 1
    for number in numbers:
        if type(number) == int or type(number) == float:  # 2 sinden biri true olursa alltaki işlemi yapacak
            result *= number

    return result


print(multiply(2, 3, 4, "yunus", 2.10))


# --------------------------------------
# (4) Verimiz bir liste veya tuple sa napıcaz
# bu sefer de fonksiyona gönderdiğimiz değişkenini önüne * koyuyoruz
# burdaki * ın anlamı ise gönderdiğimiz veriyie unpack(ayır) et anlamında 


def multiply(*numbers):
    result = 1
    for number in numbers:
        if type(number) == int or type(number) == float:
            result *= number

    return result


myList = [2, 3, 4, "yunus", 2.10]
print(multiply(*myList))
print(*myList)


# --------------------------------------
# (5) kaolorisi 50 den düşk meyvelreri verditiyoruz
# burada ise sözlük tipinde veriyi fonksiyona nasıl göndereceğimiz hakkında


def ProperCalories(ananas, kiwi):
    if ananas < 50:
        print("Ananas :", ananas)
    if kiwi < 50:
        print("Kiwi : ", kiwi)


ProperCalories(49, 51)


# --------------------------------------
# (5.1) sözlük tipinde yani key value şeklinde göndeereceksek **myFruits
# şeklinde göndermemiz gerekiyor. ki unpack ederek göndersin
# fonksiyonun icindeki deyişken de **furits şeklinde olması gerekiyor.


def ProperCalories(**furits):
    print(furits)
    print(type(furits))


myFurits = {"ananas": 49, "kiwi": 51, "nar": 63, "portakal": 41}
ProperCalories(**myFurits)


# --------------------------------------
# (5.2) şimdi 5. örnegi buna göre düzenliyorum(Key value şeklinde gönderilenler)


def ProperCalories(**furits):
    for furitName, furitCalorie in furits.items():
        if furitCalorie < 50:
            print(f"{furitName} : {furitCalorie}")


myFurits = {"ananas": 49, "kiwi": 51, "nar": 63, "portakal": 41, "elma": 23, "karpuz": 80}
ProperCalories(**myFurits)
