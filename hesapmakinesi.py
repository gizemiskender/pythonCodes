from __future__ import division
secenek1 = "(1) toplama"
secenek2 = "(2) cikartma"
secenek3 = "(3) carpma"
secenek4 = "(4) bolme"

print secenek1
print secenek2
print secenek3
print secenek4

soru = raw_input("hangi islemi istersiniz: \n")

if soru == "1":
	print(" iki sayi giriniz: \n")
	sayi1 = input()
	sayi2 = input()
	print ("sunuc = %s") %(sayi1+sayi2)

if soru == "2":
	print ("iki sayi giriniz: \n")
	sayi1 = input()
	sayi2 = input()
	print ("sonuc = %s") %(sayi1*sayi2)

if soru == "3":
	print ("iki sayi giriniz: \n")
	sayi1 = input()
	sayi2 = input()
	print ("sonuc = %s") %(sayi1*sayi2)

if soru == "4":
	print ("iki sayi giriniz: \n")
	sayi1 = input()
	sayi2 = input()
	print ("sonuc = %s") %(sayi1/sayi2)	