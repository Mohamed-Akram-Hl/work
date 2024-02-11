from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication



def CLE(ch):
    t = ""
    for i in range(2):
        t = t + str(ord(ch[i]) -55)
    t = t+"00"
    t = int(t)
    t = 98 - t%97
    if len(str(t)) == 1:
        return "0" + str(t)
    return str(t)

def verifMa(a,b,ch):
    bool = True
    for i in range(len(ch)):
        bool = ord(a) <= ord(ch[i]) <= ord(b)
    return bool

def verif(ch):
    if len(ch) == 2 and verifMa("A", "Z", ch):
        return True
    return False


def play():
    ch = windows.a.text()
    RIB = windows.a_2.text()
    if not(verif(ch)) and not(RIB.isdecimal() and 10<=len(RIB) <=30):
        windows.b.setText("verifier votre nom de pays et votre code RIB")
    elif not(verif(ch)):
        windows.b.setText("verifier votre nom de pays")
    elif not(RIB.isdecimal() and 10<=len(RIB) <=30):
        windows.b.setText("verifier votre code RIB")
    else:
        windows.b.setText(ch + CLE(ch)+RIB)
        

    



app = QApplication([])
windows = loadUi(r"C:\Users\akram\OneDrive\Documents\BAC\BAC MATH 2024\Informatique\work\Devoir 2\untitled.ui")
windows.show()
windows.c.clicked.connect(play)
app.exec_()