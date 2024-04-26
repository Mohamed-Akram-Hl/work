from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
from math import*
import numpy as np


def premier(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    
    max_divisor = sqrt(n)
    for d in range(3, int(max_divisor) + 1, 2):
        if n % d == 0:
            return False
    return True


def primes(n):
    tab = np.array([str()]*n)
    p = "" 
    i = 2
    j =0
    temp = n
    while i <= n and j < temp and n != 1:
        if premier(i) and n%i == 0:
            n = n //i
            tab[j] = str(i)
            i = 2
            j = j + 1
        else:
            i = i+1
    
    return tab

def res(n):
    tab = primes(n)
    i = 0
    p = ""
    while i < n and tab[i] != "":
        p = p + tab[i] + "*"
        i = i+1
    return p[0: len(p)-1]

    




def play():
    ch = windows.a.text()
    if not(ch.isdigit()):
        windows.b.setText("Please enter a valide number")
    elif not(int(ch)>=2):
        windows.b.setText("Please enter a number greater or equal to 2")
    else:
        windows.b.setText(res(int(ch)))




app = QApplication([])
windows = loadUi(r"C:\Users\akram\OneDrive\Documents\BAC\BAC MATH 2024\Informatique\work\Devoir 5\untitled.ui")
windows.show()
windows.c.clicked.connect(play)
app.exec_()