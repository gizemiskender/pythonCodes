__author__ = 'gizem'

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import random
from subprocess import call

def metinGuncelle():
    renkler = ['yellow', 'red', 'blue', 'brown', 'violet', 'green']
    etiket.setText(random.choice(renkler))

def buttonGuncelle1():
    buttonEtiket.setText('1.button')

def buttonGuncelle2():
    buttonEtiket.setText('2.button')

uyg = QApplication([])

pencere = QWidget()

etiket = QLabel('Merhaba dunyali')

buttonEtiket = QLabel('burasi buttonlar')


dugme = QPushButton('renk sec')
button1 = QPushButton('1. button')
button2 = QPushButton('2. button')

pencere.connect(dugme, SIGNAL('pressed()'), metinGuncelle)

pencere.connect(button1, SIGNAL('pressed()'), buttonGuncelle1)

pencere.connect(button2, SIGNAL('pressed()'), buttonGuncelle2)

kutu = QVBoxLayout()

kutu.addWidget(etiket)
kutu.addWidget(buttonEtiket)

kutu.addWidget(dugme)
kutu.addWidget(button1)
kutu.addWidget(button2)

pencere.setLayout(kutu)
pencere.show()
pencere.setWindowTitle('ilk PyQt programim')

uyg.exec_()