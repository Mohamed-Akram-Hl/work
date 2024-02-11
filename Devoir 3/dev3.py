from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication


def verifdate(ch):
    year = int(ch[0:4])
    month = int(ch[4:6])
    if year < 2022 :
        if 1<=month <= 12:
            return True
    elif year == 2022:
        if month <= 4:
            return True
    else:
        return False
    return False

def ann(b , a):
    year = int(a[0:4])
    month = int(a[4: 6])
    return b - year *12 - month


def play():
    ch = windows.a.text()
    if not(ch.isdigit() and len(ch) == 10 and verifdate(ch)):
        windows.b.setText("enter a valide code")
    elif ann(2022*12 +4, ch) < 60:
        windows.b.setText("you can't take the advantage because you have less than 5 years of experience")
    else:
        windows.b.setText("you have " + str(ann(2022*12 +4, ch))+ " hours as bonus.")



app = QApplication([])
windows = loadUi(r"C:\Users\akram\OneDrive\Documents\BAC\BAC MATH 2024\Informatique\work\Devoir 3\untitled.ui")
windows.show()
windows.hb.clicked.connect(play)
app.exec_()