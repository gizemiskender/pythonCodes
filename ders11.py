# sozlukler (dict)

# sozluk olusturmak 

sozluk = {"anahtar": "deger",
 "ankara": "06",
 "trabzon": "61"}
print type(sozluk) # sozluk tipi "dict"
print len(sozluk) # sozluk icindeki sozlukler
print sozluk 

# sozluk ogelerine erismek 

ogrenciNo = {"gizem": "259153",
"pinar": "123232",
"halit": "259141",
"ayse": "123434"}
print "gizem'in numarasi\t" + ogrenciNo["gizem"] # anahtara gore cagiriyoruz.

# sozcuklere oge eklemek

liste = dir(dict) # sozluk degimleri listeye eklendi.
sozluk = {} # bos sozluk olusturdum
for anahtar, deger in enumerate(liste): # for dongusuyle sozluk metodlarini numaralandirdim.
	sozluk[anahtar] = deger  # ve sozluge ekledim
print sozluk[1] + sozluk[14]	# artik numarayla cagirabilirim.

for i in ogrenciNo:
	print i

# sozluge oge eklemek ve silmek 

telefonRehberi = {"ayse": "05362569815",
"fatma": "05345632145"}	
telefonRehberi["ayse"] = "05456235698" # degeri degistirdim
print telefonRehberi["ayse"]
telefonRehberi.clear()
print telefonRehberi # rehberi sildim 
# del telefonRehberi["ayse"] 

# sozluk metodlari

for i in dir(dict): 
	if "_" not in i[0]:
		print i

print ogrenciNo.keys()	# keys sozlukteki anahtarlar
print ogrenciNo.values() # sozluk degerleri
telefonRehberi.clear() # tum sozlugu siler 
ogrenciNo.pop("ayse") # sadece istenilenn ogeyi siler 

for key, values in ogrenciNo.items(): # unpacking 
	print key, values	

# get metodu kullanalim 

soru = raw_input("sehir adi giriniz :")
cevap = {"ankara": "06",
"trabzon": "61",
"istanbul": "34",
"antalya": "07"}
print cevap.get(soru, "aradiginiz sehir listede yoktur")  # vuu baby bayildim buna :D 
# az kodla cok is 
# if elif else ye gerek kalmadan get kullandim

