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


def premier(n):
    d = 1
    if n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**(1/2))+1, 2):
            if n % i == 0:
                d = d + i
    return d == 1



def Gan(ch):
    d = 0
    if premier(int(ch)):
        d = d + 1
    for i in range(len(ch)):
        if premier(int(ch[i])):
            d = d+1
    for i in range(len(ch)-2):
        if premier(int(ch[i: i+2])):
            d = d+1
    if premier(int(ch[0:3])):
        d= d+1
    if premier(int(ch[1:4])):
        d= d+1

    return d ==5
    






def play():

    ch = windows.a.text()
    if len(ch) != 4 or not(Verif(ch)):
        windows.c.setText("erreur!!!")
    elif Gan(ch) == True :
        windows.c.setText("Bravo, notre hôtel vous offre un séjour gratuit le samedi prochain")
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