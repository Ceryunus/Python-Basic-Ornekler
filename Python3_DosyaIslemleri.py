# "w" write anlamıda her sefer yeni bi dosya acar objeismi.write("metin") seklinde calısır
# "r" read anlamında sadece olan bir dosyayı okur objeismi.read() seklinde calısır
# "w+" hem read hem de write yetkisi verir dosyayı oluşturur  dosya yoksa kullanır dosya var olunca "r+" gecilir.
# "r+" hem read hem de write yetkisi verir dosya yok ise oluşturmaz ve hata verir dosya varsa kullanılır
# "a"  dosyayı sadece 1 kere olusturur ve üzerine yazdırma yetkisi verir
# "a+" dosyayı sadece 1 kere olusturur , üzerine yazdırma yetkisi verir , okuma yetkisi verir yani tüm yetkileri verir .
# a+ metodunu kullandıgımız zaman okuma yaparken objeninism.seek(0) yapmamız gerekir bu kod ise dosyanın başından okuma yapılacağını söyler.
# objeismi.readline sadece 1 satır yazdırır
# objeismi.read() bütün dosyayı okur

with open("deneme.txt", "r+",
          encoding="Utf-8") as FileObject:  # burada "as" kullanarak fileobject adlı bir obje yani nesne olusturdum
    # FileObject.write("Python")
    oku = FileObject.read()
    print(oku)
    FileObject.write("asd")  # dosyaya "r+" verdikten sonra hem okuma hemde yazma
