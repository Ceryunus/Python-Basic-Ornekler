BannedWords = ["amk", "oc", "sik", "aq", "amq"]  # veri seti buraya girilecek
Sentence = input("Bir cümle giriniz : ")

Words = Sentence.split()
CompletedSentence = ""

for word in Words:
    if word in BannedWords:
        word = "**** "
        CompletedSentence += f"{word}"
    else:
        CompletedSentence += f"{word} "

print(CompletedSentence)
