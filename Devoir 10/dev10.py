from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
from math import*


def push(key, ch):
    alfaMA = ""
    for i in range(ord("A"), ord("Z")+1):
        alfaMA = alfaMA + chr(i)
    for i in range(key):
        alfaMA = alfaMA + alfaMA[0]
        alfaMA = alfaMA[1:27]
    alfaMI = ""
    for i in range(ord("a"), ord("z")+1):
        alfaMI = alfaMI + chr(i)
    for i in range(key):
        alfaMI = alfaMI + alfaMI[0]
        alfaMI = alfaMI[1:27]
    res = ""
    for i in range(len(ch)):
        if "A"<=ch[i]<="Z":
            res = res + alfaMA[ord(ch[i]) - ord("A")]
        elif "a"<=ch[i]<="z":
            res = res + alfaMI[ord(ch[i]) - ord("a")]
        elif ch[i] == " ":
            res = res + " "
    return res


def verif_alfa(ch):
    bool = True
    for i in range(len(ch)):
        bool = ("A" <= ch[i] <= "Z") or ("a" <= ch[i] <= "z") or ch[i] == " "
    return bool

def superflu(ch):
    if ch.find("  ")!=-1 or ch[0] == " " or ch[len(ch)-1] == " ":
        return True
    return False

def chount(c, ch):
    count = 0
    for i in range(len(ch)):
        if ch[i:i+len(c)] == c:
            count += 1
    return count



def play():
    ch = windows.a.text()
    if not(verif_alfa(ch)):
        windows.c.setText("please enter a valide msg")
    elif superflu(ch):
        windows.c.setText("please remove extra spaces")
    else:
        windows.c.setText(push(chount(" ", ch) + 1, ch))


app = QApplication([])
windows = loadUi(r"C:\Users\akram\OneDrive\Documents\BAC\BAC MATH 2024\Informatique\work\Devoir 9\untitled.ui")
windows.show()
windows.d.clicked.connect(play)
app.exec_()