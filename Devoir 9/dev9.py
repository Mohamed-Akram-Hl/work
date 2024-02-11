from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
from math import*


def push(key, ch):
    alfa = ""
    for i in range(ord("A"), ord("Z")+1):
        alfa = alfa + chr(i)
    if key > 0:
        for i in range(key):
            alfa = alfa + alfa[0]
            alfa = alfa[1:26]
    elif key < 0:
        for i in range(int(abs(key))):
            alfa = alfa[25] + alfa
            alfa = alfa[0:26]
    res = ""
    for i in range(len(ch)):
        res = res + alfa[ord(ch[i]) - ord("A")]
    return res


def verifMa(a,b,ch):
    bool = True
    for i in range(len(ch)):
        bool = ord(a) <= ord(ch[i]) <= ord(b)
    return bool

def verifnum(n):
    if len(n) != 1: 
        if (n[0] == "-" or n[0].isdecimal()) and n[1:].isdecimal():
            return True
    elif len(n) == 1:
        if n.isdecimal():
            return True
    
    return False


def play():
    ch = windows.a.text()
    n = windows.b.text()
    if not(verifMa("A", "Z", ch) or verifnum(n)):
        windows.c.setText("please enter a valide key and a valide msg")
    elif  not(verifMa("A", "Z", ch)):
        windows.c.setText("please enter a valide msg")
    elif  not(verifnum(n)):
        windows.c.setText("please enter a valide number")
    else:
        windows.c.setText(push(int(n), ch))


app = QApplication([])
windows = loadUi(r"C:\Users\akram\OneDrive\Documents\BAC\BAC MATH 2024\Informatique\work\Devoir 9\untitled.ui")
windows.show()
windows.d.clicked.connect(play)
app.exec_()