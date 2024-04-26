from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
from math import*



def Verif(ch):
    boo = True
    i=0
    while i <4 and boo:
        boo = "0"<=ch[i]<="9"
        i = i+1
    t = ch[i] == "."
    i = 5
    while i < len(ch) and boo:
        boo = "0"<=ch[i]<="9"
        i = i+1
    return t and bool


def Gan(ch):
    n = float(ch)
    n = round(n)
    n = str(n)
    res = 0
    for i in range(len(n)):
        res = res + int(n[i])
    
    bool = res % 10 == 0
    return bool
    






def play():

    ch = windows.a.text()
    if len(ch) != 8 or not(Verif(ch)):
        windows.c.setText("plz donner un nombre valide")
    elif Gan(ch) == True :
        windows.c.setText("Félicitation, vous avez gagné")
    else:
        windows.c.setText("Desolé vous n'aver pas gagné")

def Effa():
    windows.c.clear()
    windows.a.clear()

app = QApplication([])
windows = loadUi(r"C:\Users\akram\OneDrive\Documents\BAC\BAC MATH 2024\Informatique\work\Serie 2\devoir 5\untitled.ui")
windows.show()
windows.b.clicked.connect(play)
windows.d.clicked.connect(Effa)
app.exec_()