from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
from math import*



def Verif(ch):
    boo = True
    i=0
    while i <len(ch) and boo:
        boo = "0"<=ch[i]<="9"
        i = i+1
    return boo


def EAN13(ch):
    cc = int(ch[len(ch)-1])
    q = ch[0:len(ch)-1]
    res =0
    for i in range(12):
        if i % 2 == 0:
            res = res + int(ch[i])
        else:
            res = res + int(ch[i])*3
    r = res % 10
    p = 10 - r
    return p == cc






def play():

    ch = windows.a.text()
    if ch == "" or not(Verif(ch)):
        windows.c.setText("le numero doit etre uniquement formé par des chiffres")
    elif len(ch) !=13:
        windows.c.setText("le numero doit etre formé de 13 chiffre")
    elif EAN13(ch) == True :
        windows.c.setText(ch + " est un numero EAN13 Valide")
    else:
        windows.c.setText(ch + " n'est pas un numero EAN13 Valide")

def Effa():
    windows.c.clear()
    windows.a.clear()

app = QApplication([])
windows = loadUi(r"C:\Users\akram\OneDrive\Documents\BAC\BAC MATH 2024\Informatique\work\Serie 2\devoir 5\untitled.ui")
windows.show()
windows.b.clicked.connect(play)
windows.d.clicked.connect(Effa)
app.exec_()