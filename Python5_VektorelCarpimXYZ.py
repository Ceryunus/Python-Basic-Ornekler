myList = []
for a in range(3):
    x = int(input(f"1. listenin {a + 1}. elemani griniz : "))
    myList.append(x)
print(f"Oluşan liste : {myList}")



myList2 = []
for a in range(3):
    x = int(input(f"2. listenin {a + 1}. elemani griniz : "))
    myList2.append(x)
print(f"Oluşan liste : {myList2}")



resultList=[]
for s in range(3):
    result=myList[s]*myList2[s]
    resultList.append(result)


print(f"{myList}")
print(f"{myList2}")
print(f"Sonuç : {resultList}")