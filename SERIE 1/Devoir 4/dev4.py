from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication


def verif(a, b, ch):
    bool = False
    for i in range(len(ch)):
        bool = a <= ch[i] <= b
    return bool

def convr(ch):
    return ord(ch) -ord("A")+1


def auth(ch):
    n =  str(convr(ch[0])) + ch[1:]
    s = 0
    for i in range(len(n)):
        s = s + int(n[i])
    return s % 9 == 8




def play():
    ch = windows.a.text()
    if not(len(ch) == 12 and verif("A", "Z", ch[0]) and ch[1:].isdigit()):
        windows.b.setText("enter a valide code")
    elif auth(ch):
        windows.b.setText("you can pass!")
    else:
        windows.b.setText("stay there what are you doing?!")





app = QApplication([])
windows = loadUi(r"C:\Users\akram\OneDrive\Documents\BAC\BAC MATH 2024\Informatique\work\Devoir 4\untitled.ui")
windows.show()
windows.c.clicked.connect(play)
app.exec_()