from tkinter import *
import decimal
import math


def clear():
    global lbl
    lbl.destroy()


def plus():
    global lbl
    e1 = float(entry1.get())
    e2 = float(entry2.get())
    add = e1 + e2
    print(add)
    lbl = Label(window, text=add, font=("Ariel", 40))
    lbl.place(x=110, y=25)


def minus():
    global lbl
    e1 = float(entry1.get())
    e2 = float(entry2.get())
    sub = e1 - e2
    print(sub)
    lbl = Label(window, text=sub, font=("Ariel", 40))
    lbl.place(x=110, y=25)


def times():
    global lbl
    e1 = float(entry1.get())
    e2 = float(entry2.get())
    mult = e1 * e2
    print(mult)
    lbl = Label(window, text=mult, font=("Ariel", 40))
    lbl.place(x=110, y=25)


def divide():
    global lbl
    e1 = float(entry1.get())
    e2 = float(entry2.get())
    div = decimal.Decimal(e1/e2)
    rdiv = div.quantize(decimal.Decimal("0.01"))
    print(div)
    lbl = Label(window, text=rdiv, font=("Ariel", 40))
    lbl.place(x=110, y=25)


def perimeter():
    global lbl
    e1 = float(entry1.get())
    e2 = float(entry2.get())
    per = e1 + e2
    per2 = per * 2
    print(per2)
    lbl = Label(window, text=per2, font=("Ariel", 40))
    lbl.place(x=110, y=25)


def radius():
    global lbl
    entry = float(entry1.get())
    x = entry * entry
    pi = x * 3.14
    print(pi)
    lbl = Label(window, text=pi, font=("Ariel", 40))
    lbl.place(x=110, y=25)


def sqr():
    global lbl
    x = float(entry1.get())
    y = decimal.Decimal(math.sqrt(x))
    print(y)
    y2 = y.quantize(decimal.Decimal("0.01"))
    lbl = Label(window, text=y2, font=("Ariel", 40))
    lbl.place(x=110, y=25)


def power():
    global lbl
    x = float(entry1.get())
    y = float(entry2.get())
    pwr = pow(x, y)
    print(pwr)
    lbl = Label(window, text=pwr, font=("Ariel", 40))
    lbl.place(x=110, y=25)


def cper():
    global lbl
    x = float(entry1.get())
    y = float(x * 2)
    pi = decimal.Decimal(y * 3.14)
    pi2 = pi.quantize(decimal.Decimal("0.01"))
    print(pi)
    lbl = Label(window, text=pi2, font=("Ariel", 40))
    lbl.place(x=110, y=25)


def LCM():
    global lbl
    x = int(entry1.get())
    y = int(entry2.get())
    lm = decimal.Decimal(math.lcm(x, y))
    lc = lm.quantize(decimal.Decimal("0.01"))
    lbl = Label(window, text=lc, font=("Ariel", 40))
    lbl.place(x=110, y=25)


def GCF():
    global lbl
    x = int(entry1.get())
    y = int(entry2.get())
    gc = decimal.Decimal(math.gcd(x, y))
    cf = gc.quantize(decimal.Decimal("0.01"))
    lbl = Label(window, text=cf, font=("Ariel", 40))
    lbl.place(x=110, y=25)
    

def fact():
    global lbl
    x = int(entry1.get())
    fct = math.factorial(x)
    print(fct)
    lbl = Label(window, text=fct, font=("Ariel", 40))
    lbl.place(x=110, y=25)


def tarea():
    global lbl
    x = float(entry1.get())
    y = float(entry2.get())
    mth = decimal.Decimal((x * y) / 2)
    print(mth)
    mth2 = mth.quantize(decimal.Decimal("0.01"))
    lbl = Label(window, text=mth2, font=("Ariel", 40))
    lbl.place(x=110, y=25)


def rnd():
    global lbl
    x = float(entry1.get())
    y = decimal.Decimal(round(x))
    y2 = y.quantize(decimal.Decimal("0.01"))
    print(y2)
    lbl = Label(window, text=y2, font=("Ariel", 40))
    lbl.place(x=110, y=25)


def absolute():
    global lbl
    x = float(entry1.get())
    y = decimal.Decimal(abs(x))
    z = y.quantize(decimal.Decimal("0.01"))
    print(z)
    lbl = Label(window, text=z, font=("Ariel", 40))
    lbl.place(x=110, y=25)


def pd():
    global lbl
    x = str(entry1.get())
    y = x[::-1]
    if x == y:
        lbl = Label(window, text="Yes", font=("Ariel", 40))
        lbl.place(x=110, y=25)
    else:
        lbl = Label(window, text="No", font=("Ariel", 40))
        lbl.place(x=110, y=25)

    
window = Tk()
window.title("Calculator")
window = Canvas(window, width=300, height=400)
window.pack()
lbl = Label(window, text="0.00", font=("Ariel", 40))
lbl.place(x=110, y=25)
entry1 = Entry(window)
entry1.insert(0, "1st Number")
entry1.place(x=87, y=100)
entry2 = Entry(window)
entry2.insert(0, "2nd Number")
entry2.place(x=87, y=140)
abutton = Button(window, text="+", command=plus, bg="black", fg="white")
abutton.place(x=137, y=170)
sbutton = Button(window, text="–", command=minus, bg="black", fg="white")
sbutton.place(x=138, y=210)
mbutton = Button(window, text="×", command=times, bg="black", fg="white")
mbutton.place(x=137, y=250)
dbutton = Button(window, text="÷", command=divide, bg="black", fg="white")
dbutton.place(x=137, y=290)
pbutton = Button(window, text="Perimeter", command=perimeter, bg="black", fg="white")
pbutton.place(x=114, y=330)
bttn = Button(window, text="Circle Area", command=radius, bg="black", fg="white")
bttn.place(x=112, y=370)
sbttn = Button(window, text="Square Root", command=sqr, bg="black", fg="white")
sbttn.place(x=25, y=290)
ebttn = Button(window, text="Exponents", command=power, bg="black", fg="white")
ebttn.place(x=190, y=290)
pbttn = Button(window, text="Circle Perimeter", command=cper, bg="black", fg="white")
pbttn.place(x=190, y=370)
lcmbttn = Button(window, text="LCM", command=LCM, bg="black", fg="white")
lcmbttn.place(x=50, y=210)
gcfbttn = Button(window, text="GCF", command=GCF, bg="black", fg="white")
gcfbttn.place(x=200, y=210)
fbttn = Button(window, text="Factorial", command=fact, bg="black", fg="white")
fbttn.place(x=40, y=250)
tbttn = Button(window, text="Triangle Area", command=tarea, bg="black", fg="white")
tbttn.place(x=25, y=370)
rbttn = Button(window, text="Round", command=rnd, bg="black", fg="white")
rbttn.place(x=195, y=250)
absbttn = Button(window, text="Absolute Value", command=absolute, bg="black", fg="white")
absbttn.place(x=190, y=330)
cbttn = Button(window, text="Clear", command=clear, bg="black", fg="white")
cbttn.place(x=50, y=170)
plbttn = Button(window, text="Palindrome?", command=pd, bg="black", fg="white")
plbttn.place(x=25, y=330)
window.mainloop()

lbl = Label(window, text="", font=("Ariel", 40))
lbl.place(x=110, y=25)
