# cevap 2

surumler = ["Warthy Warthog ", "Hoary Hedgehog ", "Breezy Badger ", "Dapper Drake ", "Edgy Eft ", "Feisty Fawn ", "Gutsy Gibbon ", "Hardy Heron", "Intrepid Ibex ", "Jaunty Jackalope ", "Karmic Koala ", " Lucid Lynx ", "Maverick Meerkat "]
for no, isim in enumerate(surumler,1):
    print "%s: %s " %(no, isim)

# cevap 3

sayilar = []
teksayilar = []
ciftsayilar = []
while len(sayilar) < 11:
    sayi = int(raw_input("sayi giriniz:"))
    if sayi in sayilar:
        print "girdiginiz sayi zaten girildi."
        continue
    else:
        sayilar.append(sayi)
        if sayi % 2 == 0:
            teksayilar.append(sayi)
        else:
            ciftsayilar.append(sayi)

print "girdiginiz sayilar", sayilar
print "girdiginiz tek sayilar", min(teksayilar)
print "girdiginiz cift sayilar", min(ciftsayilar)

