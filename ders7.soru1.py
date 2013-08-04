from __future__ import division
secenek1 = "(1) toplama"
secenek2 = "(2) cikartma"
secenek3 = "(3) carpma"
secenek4 = "(4) bolme"

print secenek1
print secenek2
print secenek3
print secenek4

soru = raw_input("hangi islem?")
if soru == "1":
	toplam = 0
	kac = int(raw_input("kac sayi topliycaksin"))
	while kac==0: 
		sayi = int (raw_input("sayilari giriniz")) 
		toplam += sayi 
		kac -= kac
	print toplam 	

total = 0 
first = 0 
last = input("sayi gir") 
while last > first: 
total += input("sayi")
 i += 1
