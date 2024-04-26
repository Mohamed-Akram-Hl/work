from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication


def power2(a):
    return a*a


def hereux(n):
    n = str(power2(int(n)))
    p =0
    while len(n)!= 1:
        p=0
        for i in range(len(n)):
            p = p + power2(int(n[i]))
        n = str(p)
    return n == "1"






def play():
    ch = windows.a.text()
    if not(ch.isdigit()):
        windows.b.setText("enter a valide a number!")
    elif hereux(ch):
       windows.b.setText("un nombre hereux!") 
    else:
       windows.b.setText("non hereux!") 

app = QApplication([])
windows = loadUi(r"C:\Users\akram\OneDrive\Documents\BAC\BAC MATH 2024\Informatique\work\Devoir 6\untitled.ui")
windows.show()
windows.c.clicked.connect(play)
app.exec_()