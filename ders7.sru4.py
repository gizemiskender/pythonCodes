sayi = 11
while sayi == 11:
    tahmin = int(raw_input("tahmininizi giriniz:"))
    if tahmin == sayi:
        print ("tebrikler kazandiniz!")
        break
    if tahmin > sayi:
        print("asagi inin.")
    else:
        print ("yukari cikin.")
