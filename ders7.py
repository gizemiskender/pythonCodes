a = 0
while a<100:
	a +=1
	print a

x = 1 
kullanici = "gizem"
parola = "1234"

while a == 1:
	ka=raw_input("kullanici adinizi giriniz:")
	ks=raw_input("sifreniz:")

	if ka == kullanici and ks == parola:
		print "hosgeldiniz."
		x = 2
	elif not kullanici or not parola:
		print("bu alanlari bos birakamazsiniz.")
	else:
		print ("kullanici adiniz veya parolaniz hatali.")	

