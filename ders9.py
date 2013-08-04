liste = ["gizem", "pinar", "evde", "oturuyorlar"]
type(liste)
print liste
print liste[0:3]
liste2 = []
liste2 = liste[:] # liste yi liste2 ye kopyaliyor.
isim = "gizem"
print list(isim)


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
