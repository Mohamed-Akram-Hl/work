from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
import numpy as np




def Russe(a, b):
    tab_D = np.array([int()]* a)
    tab_M = np.array([int()]* a)
    tab_D[0] = a
    tab_M[0] = b
    i = 1
    temp = a
    while i < temp and a != 1:
        tab_D[i] = a//2
        tab_M[i] = b * 2
        a = a//2
        b = b*2
        i = i + 1
    j = 0
    i = i - 1
    res = 0
    while j <=i:
        if tab_D[j]%2 != 0:
            res = res + tab_M[j]
        j = j+1
    return res


def play():
    A = windows.a.text()
    B = windows.b.text()
    if not(A.isdecimal() or B.isdecimal()):
        windows.c.setText("please enter a valide numbers")
    else:
        windows.c.setText(str(Russe(int(A), int(B))))





app = QApplication([])
windows = loadUi(r"C:\Users\akram\OneDrive\Documents\BAC\BAC MATH 2024\Informatique\work\Devoir 12\untitled.ui")
windows.show()
windows.d.clicked.connect(play)
app.exec_()