liste = ["gizem", "pinar", "evde", "oturuyorlar"]
type(liste)
print liste
print liste[0:3]
liste2 = []
liste2 = liste[:] # liste yi liste2 ye kopyaliyor.
isim = "gizem"
print list(isim)
# print dir(list) liste metodlarini ekrana bastirir.

x = "112"
y = "1234"
print list((x, y)) # listeye oge ekledim.

text = """Stephen William Hawking CH CBE FRS
born 8 January 1942 is an English theoretical physicist,
cosmologist, author and Director of Research a
the Centre for Theoretical Cosmology within the University of Cambridge"""
print len(text)
print liste2
print liste[::-1]
print liste[0:4:2] #liste[::2]

liste = []
dir(liste) #bos bir liste tanimi.
dir([]) # yada
dir(list) # yada

# listeye oge eklemek

programlamaDilleri = ["python", "ruby", "C", "Java", "C"]
programlamaDilleri.append("C++") # append (ekleme) ile listeye bir oge ekledim.
digerDiller = ["C#", "PHP", "perl"]

for i in digerDiller:
    programlamaDilleri.append(i) # for dongusuyle birden cok oge ekledim.

print programlamaDilleri

programlamaDilleri.extend(["cobol", "Ada", "forthan", "Delphi", "C"]) # extend (genisletme) ile birden cok ogeyi ekledim daha guzel oldu.
print programlamaDilleri

programlamaDilleri.insert(0, "PYTHON") # inset (yerlestirme) ile ogeyi istedigim yere koydum.
print programlamaDilleri


alisveris_listesi = ["sogan", "sarimsak", "cilek", "uzum"]
print alisveris_listesi
for i in alisveris_listesi:
    print i  #normaide listedekileri turkce karakter yazdiriyor.

# listeden oge silmek

mevsimler = ["ilkbahar", "yaz", "sonbahar", "kis"]
mevsimler.remove("yaz") # silmek istedigin ogeyi siliyor.
print mevsimler

mevsimler.pop(0) # sildigin ogeyi silip ekrana basar.
print mevsimler

del mevsimler[0] # del tum listeyi de silebilir del mevsimler
print mevsimler

# liste ogelerini siralamak

sayilar = range(10)
print sayilar
sayilar.reverse() # listeyi ters cevirir.
print sayilar

sesliler = ["e", "i", "o", "a"]
sesliler.sort()
print sesliler # sort metodu alfabetik siraya dizer

#listedeki ogelerin sirasini bulmak

print programlamaDilleri.index("C") # index metodu ogenin sirasini verir.
print programlamaDilleri.index("C",7) # 7.sirardan baslayarak arama yapar.

liste = []
sira = 0
while sira < len(programlamaDilleri):
    try:  #eger aradigim oge yoksa try except ile verilecek hatayi onluyorum.
        oge = programlamaDilleri.index("C",sira)
    except ValueError:
        pass
    sira += 1
    if not oge in liste: # aradigim ogeyi listeye ekliyorum
        liste.append(oge)

for nmr in liste:
    print "aranan oge %s konumunda bulundu!" %nmr # bulundugu sirayi for ile yazdiriyorum.

print programlamaDilleri.count("C") # count metodu ile listedeki ogenin sayisini buldum.

# sum fonksiyonu

sayilar = []

while True:
    toplam = raw_input("sayi:")
    if toplam == "q":
        print "hoscakalin!"
        break
    else:
        sayilar.append(int(toplam))
    print "girdiginiz sayilarin toplami\n", sum(sayilar)

#enumerate fonksiyonu

liste = dir(list)

for no, metodAdi in enumerate(liste, 1): # enumerate fonksiyonu ile listeyi numaralandirarak listelemeis olduk.
    print "%s   %s" %(no, metodAdi)

isim = "gizemiskenderoglu"
kontrol = raw_input("isminizin icinde bir harf soyleyin:\t")
if kontrol in isim:
    print "evet harf ismin icinde bu harf var"
else:
    print "malesef yanlis!"

#min max fonksiyonlari

lst = [45, 24, 98, 71, 43, 94, 35, 90, 66, 39, 97, 96, 66, 26, 34, 61,
80, 77, 30, 92, 88, 59, 64, 50, 27, 63, 77, 48, 28, 52, 78, 56, 61, 52,]

print "sayilarin en kucugu:", min(lst)
print "sayilarin en buyugu:", max(lst)
