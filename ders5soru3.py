from __future__ import division
pazartesi = "(1) pazartesi"
sali = "(2) sali"
carsamba = "(3) carsamba"
persembe = "(4) persembe"
cuma = "(5) cuma"
cumartesi = "(6) cumartesi"
pazar = "(7) pazar"

isim = raw_input("isiminiz")
print pazartesi, sali, carsamba, persembe, cuma, cumartesi, pazar 

soru = raw_input("hangi gunun listesi ?")

if soru == "1":
	print ("Gun: Pazartesi")
	print ("musteri ismi: %s") %(isim)
	print "Gunun menusu"
	print "corba : mercimek"
	print "ana yemek: tavuk sote"
	print "tatli : kadayif "

if soru == "2":
	print ("Gun: Sali")
	print ("musteri ismi: %s") %(isim)
	print "Gunun menusu"
	print "corba : sehriye"
	print "ana yemek: tavuk "
	print "tatli : baklava "

if soru == "3":
	print ("Gun: Carsamba")
	print ("musteri ismi: %s") %(isim)
	print "Gunun menusu"
	print "corba : ezogelin"
	print "ana yemek: tavuk "
	print "tatli : gullac "
	