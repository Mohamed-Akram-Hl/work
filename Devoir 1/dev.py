from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
from math import*



def premier(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    
    max_divisor = sqrt(n)
    for d in range(3, max_divisor + 1, 2):
        if n % d == 0:
            return False
    return True

def Chance (ch):
    msg = ""
    if not(ch.isdecimal() and len(ch) == 8 and ch[0] in ["2","4","5","9"]):
        msg = "Vérifier le numéro de téléphone !"
    else:
        msg = "Désolé, vous n’avez pas gagné."
        s = 0
        for i in range(len(ch)):
            s = s + int(ch[i])* i
        if premier(s):
            msg = "Félicitation, vous avez gagné."
    return msg



def play():
    ch = windows.c.text()
    windows.a.setText(Chance(ch))




app = QApplication([])
windows = loadUi("untitled.ui")
windows.show()
windows.b.clicked.connect(play)
app.exec_()