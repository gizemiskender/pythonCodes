x = 6 ** 3#** ust alma belirteci
y = 12 % 3#mod alir
print x 
sayi = input ("sayi giriniz:")
if sayi % 2 == 0:
	print ("%s sayisi ciftir.") %(sayi)
else: 
    print ("%s sayisi tektir.") %(sayi)	

bool(x)
while bool(x):
	print "gizem"


soru = raw_input("Adiniz: ")

if bool(soru) == True:
    print "Teşekkurler"
else:
	print "Bu soruyu boş geçemezsiniz!"	

a = 12 
b = 14
print ("a / b "), float(a), b  #float() donusturme islemi yapar.

sayi1 = int(raw_input("ilk sayi:")) #boylece input() fonksiyonundan kurtulmus oldum !
sayi2 = int(raw_input("ikinci sayi"))

print("toplam"), sayi1 + sayi2

c = 122
str(c) #sayiyi karakter dizisine dondurur.
print c + a