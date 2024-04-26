from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
from math import*



def Verif(ch):
    boo = True
    i=0
    while i <len(ch) and boo:
        boo = "A"<=ch[i]<="Z" or ch[i]==" "
        i = i+1
    return boo and (ch.find("  ")==-1 and ch[0]!= " " and ch[len(ch)-1] != " ")


def tuto(ch):
    ch = ch + " "
    p = ch[0].upper()
    boo = True
    while ch.find(" ")!=-1 and boo:
        res= ch[:ch.find(" ")]
        boo = res.find(p) != -1
        ch = ch[ch.find(" ")+1::]
  
    return boo






def play():

    ch = windows.a.text()
    if ch == "" or not(Verif(ch)):
        windows.c.setText("Verifier votre chaine")
    elif tuto(ch) == True :
        windows.c.setText(" Cocogramme")
    else:
        windows.c.setText("n'est pas Cocogramme")

def Effa():
    windows.c.clear()
    windows.a.clear()

app = QApplication([])
windows = loadUi(r"C:\Users\akram\OneDrive\Documents\BAC\BAC MATH 2024\Informatique\work\Serie 2\devoir 2\untitled.ui")
windows.show()
windows.b.clicked.connect(play)
windows.d.clicked.connect(Effa)
app.exec_()