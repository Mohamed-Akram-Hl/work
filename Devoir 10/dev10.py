from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
from math import*


def push(key, ch):
    alfa = ""
    for i in range(ord("A"), ord("Z")+1):
        alfa = alfa + chr(i)
    for i in range(key):
        alfa = alfa + alfa[0]
        alfa = alfa[1:26]
    res = ""
    for i in range(len(ch)):
        res = res + alfa[ord(ch[i]) - ord("A")]
    return res


def verif_alfa(ch):
    bool = True
    for i in range(len(ch)):
        bool = ("A" <= ord(ch[i]) <= "Z") or ("A" <= ord(ch[i]) <= "Z")
    return bool



def play():
    ch = windows.a.text()
    if not(verif_alfa(ch)):
        windows.c.setText("please enter a valide key and a valide msg")
    else:
        windows.c.setText(push(len(ch), ch))


app = QApplication([])
windows = loadUi(r"C:\Users\akram\OneDrive\Documents\BAC\BAC MATH 2024\Informatique\work\Devoir 9\untitled.ui")
windows.show()
windows.d.clicked.connect(play)
app.exec_()