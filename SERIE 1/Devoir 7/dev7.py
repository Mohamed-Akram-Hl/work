from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication



def puissant(n):
    p = 1
    end = n//2 + 1
    for i in range(2, end):
        if n%i == 0:
            p = p * i
    t = 0
    while p%int(n) == 0 and p != 0:
         t =t +1
         p = p//n
    return t !=0



def play():
    ch = windows.a.text()
    if not(ch.isdecimal()):
        windows.b.setText("enter a valide number")
    elif not(int(ch)>1):
        windows.b.setText("enter a number greater than 1")
    elif not(puissant(int(ch))):
        windows.b.setText("Le nombre ne vérifie pas la propriété")
    else:
        windows.b.setText("Le nombre vérifie la propriété")



app = QApplication([])
windows = loadUi(r"C:\Users\akram\OneDrive\Documents\BAC\BAC MATH 2024\Informatique\work\Devoir 7\untitled.ui")
windows.show()
windows.c.clicked.connect(play)
app.exec_()