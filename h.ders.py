#-*- coding: windows-1254 -*-
import math

novels = ['a', 'e', 'i', 'o', 'u']
novdict = dict(zip(novels, [0, 0, 0, 0, 0]))

text = """
Nassau saw service in the North Sea in the beginning of World War I,
in the II Division of the I Battle Squadron of the German High Seas Fleet.
In August 1915, she entered the Baltic Sea and participated in the Battle
of the Gulf of Riga, where she engaged the Russian battleship Slava. Following
her return to the North Sea, Nassau and her sister ships took part in the
Battle of Jutland on 31 May1 June 1916. During the battle,
Nassau collided with the British destroyer HMS Spitfire. Nassau suffered
a total of 11 killed and 16 injured during the engagement.
"""

for nov in novdict:
    for char in text:
        if char in nov:
            novdict[nov] += 1

print "Cumle icinde %d tane a var" %(novdict['a'])
print "Cumle icinde %d tane e var" %(novdict['e'])
print "Cumle icinde %d tane i var" %(novdict['i'])
print "Cumle icinde %d tane o var" %(novdict['o'])
print "Cumle icinde %d tane u var" %(novdict['u'])


print "Toplam " + str(reduce(lambda x, y: x+y,novdict.values())) + " \
unlu harf var"

def add(x):
    return x * x * x

print novdict.values()
print map(add,novdict.values())

def even(x):
    if x%2 == 0:
        return False
    else:
        return True

def odd(x):
    if x%2 == 0:
        return True
    else:
        return False

evens = filter(even, range(0,100))
odds = filter(odd, range(0,100))
print zip(evens, odds)


ciftler = range(0,100,2) # herbirine 5 eklicez tum elemanlara

def ekle5(x):
    return x + 5

print ciftler
print map(lambda x: x*x*x, ciftler)

print len(text.split(" "))
print len(range(0,100))

def gizem(x):
    """ bak buraya yazdiklarin yani ilk satira
        pythonda doc string derler
        her fonksiyonuna yazacan ki nasil kullaniliyor bilinsin
    """

    return x+5

print dir(math)

# math modulu icinde kullanabilecegin fonksiyonlar
# nasil kullanildigi icin az onceki mantik

print math.trunc.__doc__

print math.trunc(45.73)

# gordun :D ahahah com ıyı yaa :D o fonksiyonlarin hepsi senin iste :D bi de

with open("/home/gizem/a.txt", "r") as dosya:
    satirlar = dosya.readlines()

    for satir in satirlar:
        print "satir : " + satir[::-1]

with open("/home/gizem/b1.txt", "w") as dosya:
    text = 1000 * " seni seviyom gizem\n"
    dosya.write(text)

class insan:

    def __init__(self, isim, soyisim, yas, boy, kilo):
        self.isim = isim
        self.soyisim = soyisim
        self.yas = yas
        self.boy = boy
        self.kilo = kilo

    def goster(self):
        print "Nesnenizin adi " + self.isim
        print "Soyismi de " + self.soyisim
        print "5 Sene sonraki yasi da muhtemelen olmezse " + str(self.yas+5) + " olacak"
        print "Boyuda masallah " + str(self.boy) + " essek gibi"
        print "Kilo desen hic yok " + str(self.kilo) + " diye kilo mu olur? ciliz seni"

    def showMustGoOn(self, kopkop):
        print "a bu fonksiyonu " + self.isim + " nesnesinden cagirdin"
        print "ve parametre olarak " + kopkop + " verdin"
        print "bravo iyi bok yedin"
        print str(self.yas) + " yasindan basindan utan"
        print "nah bunu yolladin bana " + kopkop

gizem = insan("gizem", "iskenderoglu", 20, 160, 50,)
halit = insan("halit", "alptekin", 19, 190, 70)

gizem.goster()
halit.showMustGoOn("oturmayami geldik?")

class tank:

    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        self.damage = 100

    def move(self, x, y):
        self.x += x
        self.y += y
        print "Your tank's moved x cordinate: " + str(x) + "y coordinate " + str(y)

    def attack(self):
        import random
        nDamage = random.randint(10, 30)
        if self.damage:
            self.damage -= nDamage
            print self.name + ": Your tank's damaged!!! : " + str(nDamage)
        else:
            print self.name + " losed..."

gizeminTanki = tank(0, 0, "gizem")
halitinTanki = tank(0, 0, "halit")

gizeminTanki.move(10,20)
gizeminTanki.move(5,6)

halitinTanki.move(15,26)

i = 0
while 50 > i:
    if gizeminTanki.damage > 0:
        gizeminTanki.attack()
    else:
        print "gizem losed"
        break

    if halitinTanki.damage > 0:
        halitinTanki.attack()
    else:
        print "halit losed"
        break
    i += 1

