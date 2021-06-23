def factorialCalculator(*numbers):  # bu foksiyon faktoriyel hesaplayıp yeni bir listeye sonucları yazdırır.
    result = 1
    resultList = []  # listeyi sonraki foksiyona göndereceğim icin yaptım.
    for number in numbers:
        result *= number
        resultList.append(result)
    print(resultList)
    myPersonelCalculator(*resultList)  # oluşuş listeyi myPersonelCalculator gönderdim


def myPersonelCalculator(*resultListParam):  # burada sırasına göre sayilar bölünür
    div = 1
    for results in resultListParam:
        lastResult = results / div
        div += 1
        print(lastResult)


numberList = [1, 2, 3, 4, 5]
factorialCalculator(*numberList)
