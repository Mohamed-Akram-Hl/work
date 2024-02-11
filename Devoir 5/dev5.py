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
    for d in range(3, int(max_divisor) + 1, 2):
        if n % d == 0:
            return False
    return True


def primes(n):
    p = "" 
    i = 2

    while i <= n and n != 1:
        if premier(i) and n%i == 0:
            n = n //i
            p = p + (str(i) + "*")
            i = 2
        else:
            i = i+1
    
    return p[0:len(p)-1]


def compter(c, ch):
    count = 0
    for i in range(len(ch)):
        if ch[i:i+len(c)] == c:
            count += 1
    return count


def delete(ch, c):
    result = ""
    i = 0
    while i < len(ch):
        if ch[i:i+len(c)] == c:
            i = i + len(c)
        else:
            result = result + ch[i]
            i = i + 1
    return result

def power(ch):
    ch = ch + "*"
    p = ""
    while ch != "":
        p = p + "(" + ch[0: ch.find("*")] + "^" + str(compter(ch[0:ch.find("*")+1],ch))+ ")" + "*"
        ch = delete(ch, ch[0:ch.find("*")+1])
    return p[0: len(p)-1]










def play():
    ch = windows.a.text()
    if not(ch.isdigit()):
        windows.b.setText("Please enter a valide number")
    elif not(int(ch)>=2):
        windows.b.setText("Please enter a number greater or equal to 2")
    else:
        temp = primes(int(ch))
        windows.b.setText(power(temp))




app = QApplication([])
windows = loadUi(r"C:\Users\akram\OneDrive\Documents\BAC\BAC MATH 2024\Informatique\work\Devoir 5\untitled.ui")
windows.show()
windows.c.clicked.connect(play)
app.exec_()