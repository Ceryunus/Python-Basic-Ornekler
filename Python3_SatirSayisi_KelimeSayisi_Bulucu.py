print("Dosya ismini giriniz")
FileName = input()

with open(f"{FileName}", "r+", encoding="Utf-8") as FileName:
    oku = FileName.read()
    LineNumber = oku.count("\n")
    print(f"Satır satısı : {LineNumber}")
    WordsNumber = len(oku.split())
    print(f"Kelime sayısı : {WordsNumber}")
    Words = oku.split()
    LongWord = Words[0]
    for x in range(WordsNumber):
        if len(Words[x]) > len(LongWord):
            LongWord = Words[x]
    print(f"En uzun kelime : {LongWord}")
