from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication






def pgcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a



def uni(n):
    p = 0
    for i in range(1, n//2+1):
        if n%i == 0 and pgcd(i, n//i) ==1:
            p = p + i 

    return n ==p


def play():
    ch = windows.a.text()
    if not(ch.isdecimal()):
        windows.b.setText("please enter a valide number")
    elif not(int(ch)>1):
        windows.b.setText("please enter a number greater than one")
    elif not(uni(int(ch))):
        windows.b.setText("not uni")
    else:
        windows.b.setText("uni")





app = QApplication([])
windows = loadUi(r"C:\Users\akram\OneDrive\Documents\BAC\BAC MATH 2024\Informatique\work\Devoir 8\untitled.ui")
windows.show()
windows.c.clicked.connect(play)
app.exec_()