import tkinter.messagebox
from tkinter import *
import time
from tkinter import Tk, ttk
import tkinter.font as font
from random import*


parent = Tk()
parent.geometry("1342x800+0+0")
parent.title("My Menu")
parent["bg"] = "powder blue"
fnt = font.Font(family="Helevitica", size=15, weight=font.BOLD)
f = font.Font(weight="bold", size=20)
ft = font.Font(weight="bold", size=45)

f1 = Frame(parent, bd=10, width=1350, height=100, bg="light blue", relief=RIDGE, highlightbackground="black")
f1.pack(side=TOP, fill=X)

f2 = Frame(parent, bg="light blue", width=1350, height=200, relief=RIDGE)
f2.pack(side=BOTTOM, anchor="n", fill=X)

f3 = Frame(f2, bd=12, width=400, height=400, bg="light blue", highlightthickness=3, highlightbackground="black",
           relief=RIDGE)
f3.pack(side=LEFT, anchor="n", fill=Y, expand=True)

f4 = Frame(f2, bd=12, height=500, width=450, bg="light blue", highlightbackground="black", highlightthickness=3,
           relief=RIDGE)
f4.pack(side=RIGHT, fill=X, anchor="n", expand=True)

f5 = Frame(f2, bd=12, height=290, width=450, bg="light blue", highlightbackground="black", highlightthickness=3,
           relief=RIDGE)
f5.pack(side=BOTTOM, fill=Y, anchor="n", expand=True)

f6 = Frame(f2, bd=12, height=400, width=450, bg="light blue", highlightbackground="black", highlightthickness=3,
           relief=RIDGE)
f6.pack(side=BOTTOM, fill=X, expand=True, anchor="n")

w = Label(f1, text="007'S ASSORTED KITCHEN", font="50", bg="light blue", fg="black")
w["font"] = ft
w.pack(side=LEFT)
tt = time.asctime(time.localtime(time.time()))
tl = Label(f1, text=tt, fg='steel blue', bg='light blue', bd=2, font=fnt, anchor='n')
tl.pack(side=RIGHT)
HH1 = IntVar()
HH1.set(0)
b1 = IntVar()


def add():
    l1.configure(state=NORMAL)
    value = int(l1.get())
    value += 1
    l1.delete(0, "end")
    l1.insert(0, value)
    l1.configure(state=DISABLED)


def sub():
    l1.configure(state=NORMAL)
    value = int(l1.get())
    if b1.get() > 0:
        value -= 1
    l1.delete(0, "end")
    l1.insert(0, value)
    l1.configure(state=DISABLED)


def act():
    if HH1.get() == 1:
        bt1.configure(state=NORMAL)
        bt2.configure(state=NORMAL)
    elif HH1.get() == 0:
        bt1.configure(state=DISABLED)
        bt2.configure(state=DISABLED)


HH2 = IntVar()
HH2.set(0)
b2 = IntVar()


def add1():
    l2.configure(state=NORMAL)
    value = int(l2.get())
    value += 1
    l2.delete(0, "end")
    l2.insert(0, value)
    l2.configure(state=DISABLED)


def sub1():
    l2.configure(state=NORMAL)
    value = int(l2.get())
    if b2.get() > 0:
        value -= 1
    l2.delete(0, "end")
    l2.insert(0, value)
    l2.configure(state=DISABLED)


def act1():
    if HH2.get() == 1:
        bt3.configure(state=NORMAL)
        bt4.configure(state=NORMAL)
    elif HH2.get() == 0:
        bt3.configure(state=DISABLED)
        bt4.configure(state=DISABLED)


HH3 = IntVar()
HH3.set(0)
b3 = IntVar()


def add2():
    l3.configure(state=NORMAL)
    value = int(l3.get())
    value += 1
    l3.delete(0, "end")
    l3.insert(0, value)
    l3.configure(state=DISABLED)


def sub2():
    l3.configure(state=NORMAL)
    value = int(l3.get())
    if b3.get() > 0:
        value -= 1
    l3.delete(0, "end")
    l3.insert(0, value)
    l3.configure(state=DISABLED)


def act2():
    if HH3.get() == 1:
        bt5.configure(state=NORMAL)
        bt6.configure(state=NORMAL)
    elif HH3.get() == 0:
        bt5.configure(state=DISABLED)
        bt6.configure(state=DISABLED)


HH4 = IntVar()
HH4.set(0)
b4 = IntVar()


def add3():
    l4.configure(state=NORMAL)
    value = int(l4.get())
    value += 1
    l4.delete(0, "end")
    l4.insert(0, value)
    l4.configure(state=DISABLED)


def sub3():
    l4.configure(state=NORMAL)
    value = int(l4.get())
    if b4.get() > 0:
        value -= 1
    l4.delete(0, "end")
    l4.insert(0, value)
    l4.configure(state=DISABLED)


def act3():
    if HH4.get() == 1:
        bt7.configure(state=NORMAL)
        bt8.configure(state=NORMAL)
    elif HH4.get() == 0:
        bt7.configure(state=DISABLED)
        bt8.configure(state=DISABLED)


HH5 = IntVar()
HH5.set(0)
b5 = IntVar()


def add4():
    l5.configure(state=NORMAL)
    value = int(l5.get())
    value += 1
    l5.delete(0, "end")
    l5.insert(0, value)
    l5.configure(state=DISABLED)


def sub4():
    l5.configure(state=NORMAL)
    value = int(l5.get())
    if b5.get() > 0.0:
        value -= 1
    l5.delete(0, "end")
    l5.insert(0, value)
    l5.configure(state=DISABLED)


def act4():
    if HH5.get() == 1:
        bt9.configure(state=NORMAL)
        bt10.configure(state=NORMAL)
    elif HH5.get() == 0:
        bt9.configure(state=DISABLED)
        bt10.configure(state=DISABLED)


HH6 = IntVar()
HH6.set("0")
b6 = IntVar()


def add5():
    l6.configure(state=NORMAL)
    value = int(l6.get())
    value += 1
    l6.delete(0, "end")
    l6.insert(0, value)
    l6.configure(state=DISABLED)


def sub5():
    l6.configure(state=NORMAL)
    value = int(l6.get())
    if b6.get() > 0:
        value -= 1
    l6.delete(0, "end")
    l6.insert(0, value)
    l6.configure(state=DISABLED)


def act5():
    if HH6.get() == 1:
        bt11.configure(state=NORMAL)
        bt12.configure(state=NORMAL)
    elif HH6.get() == 0:
        bt11.configure(state=DISABLED)
        bt12.configure(state=DISABLED)


HH7 = IntVar()
HH7.set("0")
b7 = IntVar()


def add6():
    l7.configure(state=NORMAL)
    value = int(l7.get())
    value += 1
    l7.delete(0, "end")
    l7.insert(0, value)
    l7.configure(state=DISABLED)


def sub6():
    l7.configure(state=NORMAL)
    value = int(l7.get())
    if b7.get() > 0:
        value -= 1
    l7.delete(0, "end")
    l7.insert(0, value)
    l7.configure(state=DISABLED)


def act6():
    if HH7.get() == 1:
        bt13.configure(state=NORMAL)
        bt14.configure(state=NORMAL)
    elif HH6.get() == 0:
        bt13.configure(state=DISABLED)
        bt14.configure(state=DISABLED)


HH8 = IntVar()
HH8.set("0")
b8 = IntVar()


def add7():
    l8.configure(state=NORMAL)
    value = int(l8.get())
    value += 1
    l8.delete(0, "end")
    l8.insert(0, value)
    l8.configure(state=DISABLED)


def sub7():
    l8.configure(state=NORMAL)
    value = int(l8.get())
    if b8.get() > 0:
        value -= 1
    l8.delete(0, "end")
    l8.insert(0, value)
    l8.configure(state=DISABLED)


def act7():
    if HH8.get() == 1:
        bt15.configure(state=NORMAL)
        bt16.configure(state=NORMAL)
    elif HH8.get() == 0:
        bt15.configure(state=DISABLED)
        bt16.configure(state=DISABLED)


HH9 = IntVar()
HH9.set(0)
b9 = IntVar()


def add8():
    l9.configure(state=NORMAL)
    value = int(l9.get())
    value += 1
    l9.delete(0, "end")
    l9.insert(0, value)
    l9.configure(state=DISABLED)


def sub8():
    l9.configure(state=NORMAL)
    value = int(l9.get())
    if b9.get() > 0:
        value -= 1
    l9.delete(0, "end")
    l9.insert(0, value)
    l9.configure(state=DISABLED)


def act8():
    if HH9.get() == 1:
        bt17.configure(state=NORMAL)
        bt18.configure(state=NORMAL)
    elif HH9.get() == 0:
        bt17.configure(state=DISABLED)
        bt18.configure(state=DISABLED)


HH10 = IntVar()
HH10.set(0)
b10 = IntVar()


def add9():
    l10.configure(state=NORMAL)
    value = int(l10.get())
    value += 1
    l10.delete(0, "end")
    l10.insert(0, value)
    l10.configure(state=DISABLED)


def sub9():
    l10.configure(state=NORMAL)
    value = int(l10.get())
    if b10.get() > 0:
        value -= 1
    l10.delete(0, "end")
    l10.insert(0, value)
    l10.configure(state=DISABLED)


def act9():
    if HH10.get() == 1:
        bt19.configure(state=NORMAL)
        bt20.configure(state=NORMAL)
    elif HH10.get() == 0:
        bt19.configure(state=DISABLED)
        bt20.configure(state=DISABLED)


HH11 = IntVar()
HH11.set("0")
b11 = IntVar()


def add10():
    l11.configure(state=NORMAL)
    value = int(l11.get())
    value += 1
    l11.delete(0, "end")
    l11.insert(0, value)
    l11.configure(state=DISABLED)


def sub10():
    l11.configure(state=NORMAL)
    value = int(l11.get())
    if b11.get() > 0:
        value -= 1
    l11.delete(0, "end")
    l11.insert(0, value)
    l11.configure(state=DISABLED)


def act10():
    if HH11.get() == 1:
        bt21.configure(state=NORMAL)
        bt22.configure(state=NORMAL)
    elif HH11.get() == 0:
        bt21.configure(state=DISABLED)
        bt22.configure(state=DISABLED)


HH12 = IntVar()
HH12.set("0")
b12 = IntVar()


def add11():
    l12.configure(state=NORMAL)
    value = int(l12.get())
    value += 1
    l12.delete(0, "end")
    l12.insert(0, value)
    l12.configure(state=DISABLED)


def sub11():
    l12.configure(state=NORMAL)
    value = int(l12.get())
    if b12.get() > 0:
        value -= 1
    l12.delete(0, "end")
    l12.insert(0, value)
    l12.configure(state=DISABLED)


def act11():
    if HH12.get() == 1:
        bt23.configure(state=NORMAL)
        bt24.configure(state=NORMAL)
    elif HH12.get() == 0:
        bt23.configure(state=DISABLED)
        bt24.configure(state=DISABLED)


HH13 = IntVar()
HH13.set(0)
b13 = IntVar()


def add12():
    l13.configure(state=NORMAL)
    value = int(l13.get())
    value += 1
    l13.delete(0, "end")
    l13.insert(0, value)
    l13.configure(state=DISABLED)


def sub12():
    l13.configure(state=NORMAL)
    value = int(l13.get())
    if b13.get() > 0:
        value -= 1
    l13.delete(0, "end")
    l13.insert(0, value)
    l13.configure(state=DISABLED)


def act12():
    if HH13.get() == 1:
        bt25.configure(state=NORMAL)
        bt26.configure(state=NORMAL)
    elif HH13.get() == 0:
        bt25.configure(state=DISABLED)
        bt26.configure(state=DISABLED)


HH14 = IntVar()
HH14.set(0)
b14 = IntVar()


def add13():
    l14.configure(state=NORMAL)
    value = int(l14.get())
    value += 1
    l14.delete(0, "end")
    l14.insert(0, value)
    l14.configure(state=DISABLED)


def sub13():
    l14.configure(state=NORMAL)
    value = int(l14.get())
    if b14.get() > 0:
        value -= 1
    l14.delete(0, "end")
    l14.insert(0, value)
    l14.configure(state=DISABLED)


def act13():
    if HH14.get() == 1:
        bt27.configure(state=NORMAL)
        bt28.configure(state=NORMAL)
    elif HH14.get() == 0:
        bt27.configure(state=DISABLED)
        bt28.configure(state=DISABLED)


HH15 = IntVar()
HH15.set(0)
b15 = IntVar()


def add14():
    l15.configure(state=NORMAL)
    value = int(l15.get())
    value += 1
    l15.delete(0, "end")
    l15.insert(0, value)
    l15.configure(state=DISABLED)


def sub14():
    l15.configure(state=NORMAL)
    value = int(l15.get())
    if b15.get() > 0:
        value -= 1
    l15.delete(0, "end")
    l15.insert(0, value)
    l15.configure(state=DISABLED)


def act14():
    if HH15.get() == 1:
        bt29.configure(state=NORMAL)
        bt30.configure(state=NORMAL)
    elif HH15.get() == 0:
        bt29.configure(state=DISABLED)
        bt30.configure(state=DISABLED)


HH16 = IntVar()
HH16.set(0)
b16 = IntVar()

def add15():
    l16.configure(state=NORMAL)
    value = int(l16.get())
    value += 1
    l16.delete(0, "end")
    l16.insert(0, value)
    l16.configure(state=DISABLED)

def sub15():
    l16.configure(state=NORMAL)
    value = int(l16.get())
    if b16.get() > 0:
        value -= 1
    l16.delete(0, "end")
    l16.insert(0, value)
    l16.configure(state=DISABLED)

def act15():
    if HH16.get() == 1:
        bt31.configure(state=NORMAL)
        bt32.configure(state=NORMAL)
    elif HH16.get() == 0:
        bt31.configure(state=DISABLED)
        bt32.configure(state=DISABLED)


HH17 = IntVar()
HH17.set(0)
b17 = IntVar()
def add16():
    l17.configure(state=NORMAL)
    value = int(l17.get())
    value += 1
    l17.delete(0, "end")
    l17.insert(0, value)
    l17.configure(state=DISABLED)

def sub16():
    l17.configure(state=NORMAL)
    value = int(l17.get())
    if b17.get() > 0:
        value -= 1
    l17.delete(0, "end")
    l17.insert(0, value)
    l17.configure(state=DISABLED)

def act16():
    if HH17.get() == 1:
        bt33.configure(state=NORMAL)
        bt34.configure(state=NORMAL)
    elif HH17.get() == 0:
        bt33.configure(state=DISABLED)
        bt34.configure(state=DISABLED)

HH18 = IntVar()
HH18.set("0")
b18 = IntVar()


def add17():
    l18.configure(state=NORMAL)
    value = int(l18.get())
    value += 1
    l18.delete(0, "end")
    l18.insert(0, value)
    l18.configure(state=DISABLED)

def sub17():
    l18.configure(state=NORMAL)
    value = int(l18.get())
    if b18.get() > 0:
        value -= 1
    l18.delete(0, "end")
    l18.insert(0, value)
    l18.configure(state=DISABLED)

def act17():
    if HH18.get() == 1:
        bt35.configure(state=NORMAL)
        bt36.configure(state=NORMAL)
    elif HH18.get() == 0:
        bt35.configure(state=DISABLED)
        bt36.configure(state=DISABLED)

HH19 = IntVar()
HH19.set(0)
b19 = IntVar()

def add18():
    l19.configure(state=NORMAL)
    value = int(l19.get())
    value += 1
    l19.delete(0, "end")
    l19.insert(0, value)
    l19.configure(state=DISABLED)

def sub18():
    l19.configure(state=NORMAL)
    value = int(l19.get())
    if b19.get() > 0:
        value -= 1
    l19.delete(0, "end")
    l19.insert(0, value)
    l19.configure(state=DISABLED)

def act18():
    if HH19.get() == 1:
        bt37.configure(state=NORMAL)
        bt38.configure(state=NORMAL)
    elif HH19.get() == 0:
        bt37.configure(state=DISABLED)
        bt38.configure(state=DISABLED)

HH20 = IntVar()
HH20.set("0")
b20 = IntVar()

def add19():
    l20.configure(state=NORMAL)
    value = int(l20.get())
    value += 1
    l20.delete(0, "end")
    l20.insert(0, value)
    l20.configure(state=DISABLED)

def sub19():
    l20.configure(state=NORMAL)
    value = int(l20.get())
    if b20.get() > 0:
        value -= 1
    l20.delete(0, "end")
    l20.insert(0, value)
    l20.configure(state=DISABLED)

def act19():
    if HH20.get() == 1:
        bt39.configure(state=NORMAL)
        bt40.configure(state=NORMAL)
    elif HH20.get() == 0:
        bt39.configure(state=DISABLED)
        bt40.configure(state=DISABLED)

HH21 = IntVar()
HH21.set(0)
b21 = IntVar()

def add20():
    l21.configure(state=NORMAL)
    value = int(l21.get())
    value += 1
    l21.delete(0, "end")
    l21.insert(0, value)
    l21.configure(state=DISABLED)

def sub20():
    l21.configure(state=NORMAL)
    value = int(l21.get())
    if b21.get() > 0:
        value -= 1
    l21.delete(0, "end")
    l21.insert(0, value)
    l21.configure(state=DISABLED)

def act20():
    if HH21.get() == 1:
        bt41.configure(state=NORMAL)
        bt42.configure(state=NORMAL)
    elif HH21.get() == 0:
        bt41.configure(state=DISABLED)
        bt42.configure(state=DISABLED)

HH22 = IntVar()
HH22.set(0)
b22 = IntVar()

def add21():
    l22.configure(state=NORMAL)
    value = int(l22.get())
    value += 1
    l22.delete(0, "end")
    l22.insert(0, value)
    l22.configure(state=DISABLED)

def sub21():
    l22.configure(state=NORMAL)
    value = int(l22.get())
    if b22.get() > 0:
        value -= 1
    l22.delete(0, "end")
    l22.insert(0, value)
    l22.configure(state=DISABLED)

def act21():
    if HH22.get() == 1:
        bt43.configure(state=NORMAL)
        bt44.configure(state=NORMAL)
    elif HH22.get() == 0:
        bt43.configure(state=DISABLED)
        bt44.configure(state=DISABLED)




p1 = IntVar()


def reset():
    p1.set(0)
    v1.set(0)
    HH1.set(0)
    HH2.set(0)
    HH3.set(0)
    HH4.set(0)
    HH5.set(0)
    HH6.set(0)
    HH7.set(0)
    HH8.set(0)
    HH9.set(0)
    HH10.set(0)
    HH11.set(0)
    HH12.set(0)
    HH13.set(0)
    HH14.set(0)
    HH15.set(0)
    HH16.set(0)
    HH17.set(0)
    HH18.set(0)
    HH19.set(0)
    HH20.set(0)
    HH21.set(0)
    HH22.set(0)
    payment_box.set("Pick an option")
    
    b1.set(0)
    b2.set(0)
    b3.set(0)
    b4.set(0)
    b5.set(0)
    b6.set(0)
    b7.set(0)
    b8.set(0)
    b9.set(0)
    b10.set(0)
    b11.set(0)
    b12.set(0)
    b13.set(0)
    b14.set(0)
    b15.set(0)
    b16.set(0)
    b17.set(0)
    b18.set(0)
    b19.set(0)
    b20.set(0)
    b21.set(0)
    b22.set(0)

    bt1.configure(state=DISABLED)
    bt2.configure(state=DISABLED)
    bt3.configure(state=DISABLED)
    bt4.configure(state=DISABLED)
    bt5.configure(state=DISABLED)
    bt6.configure(state=DISABLED)
    bt7.configure(state=DISABLED)
    bt8.configure(state=DISABLED)
    bt9.configure(state=DISABLED)
    bt10.configure(state=DISABLED)
    bt11.configure(state=DISABLED)
    bt12.configure(state=DISABLED)
    bt13.configure(state=DISABLED)
    bt14.configure(state=DISABLED)
    bt15.configure(state=DISABLED)
    bt16.configure(state=DISABLED)
    bt17.configure(state=DISABLED)
    bt18.configure(state=DISABLED)
    bt19.configure(state=DISABLED)
    bt20.configure(state=DISABLED)
    bt21.configure(state=DISABLED)
    bt22.configure(state=DISABLED)
    bt23.configure(state=DISABLED)
    bt24.configure(state=DISABLED)
    bt25.configure(state=DISABLED)
    bt26.configure(state=DISABLED)
    bt27.configure(state=DISABLED)
    bt28.configure(state=DISABLED)
    bt29.configure(state=DISABLED)
    bt30.configure(state=DISABLED)
    bt31.configure(state=DISABLED)
    bt32.configure(state=DISABLED)
    bt33.configure(state=DISABLED)
    bt34.configure(state=DISABLED)
    bt35.configure(state=DISABLED)
    bt36.configure(state=DISABLED)
    bt37.configure(state=DISABLED)
    bt38.configure(state=DISABLED)
    bt39.configure(state=DISABLED)
    bt40.configure(state=DISABLED)
    bt41.configure(state=DISABLED)
    bt42.configure(state=DISABLED)
    bt43.configure(state=DISABLED)
    bt44.configure(state=DISABLED)



v1 = IntVar()
def cost():
    f1 = int(b1.get())
    f2 = int(b2.get())
    f3 = int(b3.get())
    f4 = int(b4.get())
    f5 = int(b5.get())
    f6 = int(b6.get())
    f7 = int(b7.get())
    f8 = int(b8.get())
    f9 = int(b9.get())
    f10 = int(b10.get())
    f11 = int(b11.get())
    f12 = int(b12.get())
    f13 = int(b13.get())
    f14 = int(b14.get())
    f15 = int(b15.get())
    f16 = int(b16.get())
    f17 = int(b17.get())
    f18 = int(b18.get())
    f19 = int(b19.get())
    f20 = int(b20.get())
    f21 = int(b21.get())
    f22 = int(b22.get())
    global v1
    v1.set(f1*700 + f2*600 +f3*1500 + f4*100+ f5*700 + f6*300 + f7*200 + f8 * 100 + f9 * 100 + f10 * 50 + f11 * 100 +
           f12 * 100 + f13 * 100 + f14 * 200 +f15 * 500 + f16 * 500 +
           f17 * 300 + f18 * 170 + f19 * 1000 + f20 * 1000 + f21 * 1000 + f22 * 1500 )

def receipt():
    from reportlab.pdfgen import canvas
    rand=random.random(1000,92314934358)
    randsr=str(x)

    c = canvas.Canvas("invoice.pdf",pagesize=(200,250),bottomup=0)


    c.translate(10,40)

    c.scale(1,-1)

   # c.drawImage("icon.jpg",0,0,width=50,height=30)


    c.scale(1,-1)

    c.translate(-10,-40)

    c.setFont("Helvetica-Bold",10)

    c.drawCentredString(125,20,"007's Assorted Kitchen")

    c.line(70,22,180,22)

    c.setFont("Helvetica-Bold",5)
    c.drawCentredString(125,30,"4,Agbelura close,Falana,Beside SAO Petrol Station,Lagos/Ibadan Express way")
    c.drawCentredString(125,35,"Challenge, Ibadan.")
    c.setFont("Helvetica-Bold",6)
    c.drawCentredString(125,42,"GSTIN : 07AABCS1429B1Z")


    c.line(5,45,195,45)


    c.setFont("Courier-Bold",8)
    c.drawCentredString(100,55,"RECEIPT")


    c.roundRect(15,63,170,40,10,stroke=1,fill=0)
    c.setFont("Times-Bold",5)

    customer=str(input("Enter customers number: "))
    phone=str(input("customers phone number: "))
  
    c.drawRightString(70,70,"INVOICE No. :"+randsr)
    c.drawRightString(70,80,"DATE: "+ tt)
    c.drawRightString(70,90,("CUSTOMER_NAME: "+customer))
    c.drawRightString(70,100,"PHONE_No "+phone)


    c.roundRect(15,108,170,130,10,stroke=1,fill=0)
    c.line(15,120,185,120)


    c.drawCentredString(25,118,"SR No: "+randsr)
    c.drawCentredString(75,118,"GOODS DESCRIPTION")
    c.drawCentredString(125,118,"PRICE:")
    c.drawCentredString(148,118,"QTY")
    c.drawCentredString(173,118,"TOTAL"+v1)

    c.line(15,210,185,210)
    c.line(35,108,35,220)
    c.line(115,108,115,220)
    c.line(135,108,135,220)
    c.line(160,108,160,220)


    c.showPage()

    c.save()


def Exit():
    exit = tkinter.messagebox.askyesno("ODOGWU'S KITCHEN", 'Do you want to exit?')
    if exit > 0:
        parent.destroy()
        return


t1 = Label(f3, text="Fast Meal and Vegetarian", bg="LIGHT BLUE", fg="black")
t1["font"] = f
t1.grid(row=0, column=0, sticky=W)

C1 = Checkbutton(f3, text="Fries :#700", width=10, height=2, bg="light blue", activebackground="light blue", font=fnt,
                 anchor="w", variable=HH1, onvalue=1, offvalue=0, command=act)
C1.grid(row=1, column=0, sticky=W)
l1 = Entry(f3, font=('arial', 18, 'bold'), width=5, bd=2, justify='right', textvariable=b1, state=DISABLED,
           relief=SUNKEN)
l1.grid(row=1, column=1, sticky=E)
bt1 = Button(f3, text="+", command=lambda: add(), width=3, height=1, bg="light blue", activebackground="light blue",
             state=DISABLED, relief=RIDGE)
bt1.grid(row=1, column=0, sticky=N)
bt2 = Button(f3, text="-", command=lambda: sub(), width=3, height=1, bg="light blue", activebackground="light blue",
             state=DISABLED, relief=RIDGE)
bt2.grid(row=1, column=0, sticky=S)

C2 = Checkbutton(f3, text="Salad:#600", width=10, height=2, bg="light blue", activebackground="light blue", font=fnt,
                 anchor="w", variable=HH2, onvalue=1, offvalue=0, command=act1)
C2.grid(row=2, column=0, sticky=W)
l2 = Entry(f3, font=('arial', 18, 'bold'), width=5, bd=2, justify='right', textvariable=b2, state=DISABLED,
           relief=SUNKEN)
l2.grid(row=2, column=1, sticky=E)
bt3 = Button(f3, text="+", command=lambda: add1(), width=3, height=1, bg="light blue", activebackground="light blue",
             state=DISABLED, relief=RIDGE)
bt3.grid(row=2, column=0, sticky=N)
bt4 = Button(f3, text="-", command=lambda: sub1(), width=3, height=1, bg="light blue", activebackground="light blue",
             state=DISABLED, relief=RIDGE)
bt4.grid(row=2, column=0, sticky=S)

C3 = Checkbutton(f3, text="Pizza:#1500", bg="light blue", activebackground="light blue", font=fnt, width=10, height=2,
                 anchor="w", variable=HH3, onvalue=1, offvalue=0, command=act2)
C3.grid(row=3, column=0, sticky=W)
l3 = Entry(f3, font=('arial', 18, 'bold'), width=5, bd=2, justify='right', state=DISABLED, textvariable=b3,
           relief=SUNKEN)
l3.grid(row=3, column=1, sticky=E)
bt5 = Button(f3, text="+", command=lambda: add2(), width=3, height=1, bg="light blue", activebackground="light blue",
             state=DISABLED, relief=RIDGE)
bt5.grid(row=3, column=0, sticky=N)
bt6 = Button(f3, text="-", command=lambda: sub2(), width=3, height=1, bg="light blue", activebackground="light blue",
             state=DISABLED, relief=RIDGE)
bt6.grid(row=3, column=0, sticky=S)

C4 = Checkbutton(f3, text="Dodo  :#100", bg="light blue", activebackground="light blue", width=15, height=2, font=fnt,
                 anchor="w", variable=HH4, onvalue=1, offvalue=0, command=act3)
C4.grid(row=4, column=0, sticky=W)
l4 = Entry(f3, font=('arial', 18, 'bold'), width=5, bd=2, justify='right', textvariable=b4, state=DISABLED,
           relief=SUNKEN)
l4.grid(row=4, column=1, sticky=E)
bt7 = Button(f3, text="+", command=lambda: add3(), width=3, height=1, bg="light blue", activebackground="light blue",
             state=DISABLED, relief=RIDGE)
bt7.grid(row=4, column=0, sticky=N)
bt8 = Button(f3, text="-", command=lambda: sub3(), width=3, height=1, bg="light blue", activebackground="light blue",
             state=DISABLED, relief=RIDGE)
bt8.grid(row=4, column=0, sticky=S)

c5 = Checkbutton(f3, text="Suya :#700", bg="light blue", activebackground="light blue", font=fnt, width=10, height=2,
                 anchor="w", variable=HH5, onvalue=1, offvalue=0, command=act4)
c5.grid(row=5, column=0, sticky=W)
l5 = Entry(f3, font=('arial', 18, 'bold'), width=5, bd=2, justify='right', textvariable=b5, state=DISABLED,
           relief=SUNKEN)
l5.grid(row=5, column=1, sticky=E)
bt9 = Button(f3, text="+", command=lambda: add4(), width=3, height=1, bg="light blue", activebackground="light blue",
             state=DISABLED, relief=RIDGE)
bt9.grid(row=5, column=0, sticky=N)
bt10 = Button(f3, text="-", command=lambda: sub4(), width=3, height=1, bg="light blue", activebackground="light blue",
              state=DISABLED, relief=RIDGE)
bt10.grid(row=5, column=0, sticky=S)

s = Label(f3, text="Okélè", bg="light blue")
s["font"] = f
s.grid(row=6, column=0, sticky=W)

s1 = Checkbutton(f3, text="Íyàn  :#300", bg="light blue", activebackground="light blue", font=fnt, width=10, height=2,
                 anchor="w", variable=HH6, onvalue=1, offvalue=0, command=act5)
s1.grid(row=7, column=0, sticky=W)
l6 = Entry(f3, font=('arial', 18, 'bold'), width=5, bd=2, justify='right', textvariable=b6, state=DISABLED,
           relief=SUNKEN)
l6.grid(row=7, column=1, sticky=E)
bt11 = Button(f3, text="+", command=lambda: add5(), width=3, height=1, bg="light blue", activebackground="light blue",
              state=DISABLED, relief=RIDGE)
bt11.grid(row=7, column=0, sticky=N)
bt12 = Button(f3, text="-", command=lambda: sub5(), width=3, height=1, bg="light blue", activebackground="light blue",
              state=DISABLED, relief=RIDGE)
bt12.grid(row=7, column=0, sticky=S)

s2 = Checkbutton(f3, text="Ámàlá :#200", bg="light blue", activebackground="light blue", font=fnt, width=10, height=2,
                 anchor="w", variable=HH7, onvalue=1, offvalue=0, command=act6)
s2.grid(row=8, column=0, sticky=W)
l7 = Entry(f3, font=('arial', 18, 'bold'), width=5, bd=2, justify='right', textvariable=b7, state=DISABLED,
           relief=SUNKEN)
l7.grid(row=8, column=1, sticky=E)
bt13 = Button(f3, text="+", command=lambda: add6(), width=3, height=1, bg="light blue", activebackground="light blue",
              state=DISABLED, relief=RIDGE)
bt13.grid(row=8, column=0, sticky=N)
bt14 = Button(f3, text="-", command=lambda: sub6(), width=3, height=1, bg="light blue", activebackground="light blue",
              state=DISABLED, relief=RIDGE)
bt14.grid(row=8, column=0, sticky=S)

s3 = Checkbutton(f3, text="Ébà :#100", bg="light blue", activebackground="light blue", font=fnt, width=10, height=2,
                 anchor="w", variable=HH8, onvalue=1, offvalue=0, command=act7)
s3.grid(row=9, column=0, sticky=W)
l8 = Entry(f3, font=('arial', 18, 'bold'), width=5, bd=2, justify='right', textvariable=b8, state=DISABLED,
           relief=SUNKEN)
l8.grid(row=9, column=1, sticky=E)
bt15 = Button(f3, text="+", command=lambda: add7(), width=3, height=1, bg="light blue", activebackground="light blue",
              state=DISABLED, relief=RIDGE)
bt15.grid(row=9, column=0, sticky=N)
bt16 = Button(f3, text="-", command=lambda: sub7(), width=3, height=1, bg="light blue", activebackground="light blue",
              state=DISABLED, relief=RIDGE)
bt16.grid(row=9, column=0, sticky=S)

d1 = Label(f6, text="Soup", bg="light blue", anchor="w")
d1["font"] = f
d1.grid(row=0, column=0, sticky=W)

d2 = Checkbutton(f6, text="Égùsí   :#100", bg="light blue", activebackground="light blue", font=fnt, width=10, height=2,
                 anchor="w", variable=HH9, onvalue=1, offvalue=0, command=act8)
d2.grid(row=1, column=0, sticky=W)
l9 = Entry(f6, font=('arial', 18, 'bold'), width=5, bd=2, justify='right', textvariable=b9, state=DISABLED,
           relief=SUNKEN)
l9.grid(row=1, column=1, sticky=E)
bt17 = Button(f6, text="+", command=lambda: add8(), width=3, height=1, bg="light blue", activebackground="light blue",
              state=DISABLED, relief=RIDGE)
bt17.grid(row=1, column=0, sticky=N)
bt18 = Button(f6, text="-", command=lambda: sub8(), width=3, height=1, bg="light blue", activebackground="light blue",
              state=DISABLED, relief=RIDGE)
bt18.grid(row=1, column=0, sticky=S)

d3 = Checkbutton(f6, text="Óbè Átà :#50", bg="light blue", activebackground="light blue", font=fnt, width=10, height=2,
                 anchor="w", variable=HH10, onvalue=1, offvalue=0, command=act9)
d3.grid(row=2, column=0, sticky=W)
l10 = Entry(f6, font=('arial', 18, 'bold'), width=5, bd=2, justify='right', textvariable=b10, state=DISABLED,
            relief=SUNKEN)
l10.grid(row=2, column=1, sticky=E)
bt19 = Button(f6, text="+", command=lambda: add9(), width=3, height=1, bg="light blue", activebackground="light blue",
              state=DISABLED, relief=RIDGE)
bt19.grid(row=2, column=0, sticky=N)
bt20 = Button(f6, text="-", command=lambda: sub9(), width=3, height=1, bg="light blue", activebackground="light blue",
              state=DISABLED, relief=RIDGE)
bt20.grid(row=2, column=0, sticky=S)

d4 = Checkbutton(f6, text="Gbégírì :#100", bg="light blue", activebackground="light blue", font=fnt, width=16, height=2,
                 anchor="w", variable=HH11, onvalue=1, offvalue=0, command=act10)
d4.grid(row=3, column=0, sticky=W)
l11 = Entry(f6, font=('arial', 18, 'bold'), width=5, bd=2, justify='right', textvariable=b11, state=DISABLED,
            relief=SUNKEN)
l11.grid(row=3, column=1, sticky=E)
bt21 = Button(f6, text="+", command=lambda: add10(), width=3, height=1, bg="light blue", activebackground="light blue",
              state=DISABLED, relief=RIDGE)
bt21.grid(row=3, column=0, sticky=N)
bt22 = Button(f6, text="-", command=lambda: sub10(), width=3, height=1, bg="light blue", activebackground="light blue",
              state=DISABLED, relief=RIDGE)
bt22.grid(row=3, column=0, sticky=S)

d5 = Checkbutton(f6, text=" Óbè Ílà :#100", bg="light blue", activebackground="light blue", font=fnt, width=18,
                 height=2, anchor="w", variable=HH12, onvalue=1, offvalue=0, command=act11)
d5.grid(row=4, column=0, sticky=W)
l12 = Entry(f6, font=('arial', 18, 'bold'), width=5, bd=2, justify='right', textvariable=b12, state=DISABLED,
            relief=SUNKEN)
l12.grid(row=4, column=1, sticky=E)
bt23 = Button(f6, text="+", command=lambda: add11(), width=3, height=1, bg="light blue", activebackground="light blue",
              state=DISABLED, relief=RIDGE)
bt23.grid(row=4, column=0, sticky=N)
bt24 = Button(f6, text="-", command=lambda: sub11(), width=3, height=1, bg="light blue", activebackground="light blue",
              state=DISABLED, relief=RIDGE)
bt24.grid(row=4, column=0, sticky=S)

d6 = Checkbutton(f6, text="Ogbona :#100", bg="light blue", activebackground="light blue", font=fnt, width=27, height=2,
                 anchor="w", variable=HH13, onvalue=1, offvalue=0, command=act12)
d6.grid(row=5, column=0, sticky=W)
l13 = Entry(f6, font=('arial', 18, 'bold'), width=5, bd=2, justify='right', textvariable=b13, state=DISABLED,
            relief=SUNKEN)
l13.grid(row=5, column=1, sticky=E)
bt25 = Button(f6, text="+", command=lambda: add12(), width=3, height=1, bg="light blue", activebackground="light blue",
              state=DISABLED, relief=RIDGE)
bt25.grid(row=5, column=0, sticky=N)
bt26 = Button(f6, text="-", command=lambda: sub12(), width=3, height=1, bg="light blue", activebackground="light blue",
              state=DISABLED, relief=RIDGE)
bt26.grid(row=5, column=0, sticky=S)

a = Label(f4, text="Drinks", bg="light blue")
a["font"] = f
a.grid(row=0, column=0, sticky=W)
a1 = Checkbutton(f4, text="Tea  :#200", bg="light blue", activebackground="light blue", font=fnt, height=2, width=20,
                 anchor="w", variable=HH14, onvalue=1, offvalue=0, command=act13)
a1.grid(row=1, column=0, sticky=W)
l14 = Entry(f4, font=('arial', 18, 'bold'), width=5, bd=2, justify='right', textvariable=b14, state=DISABLED,
            relief=SUNKEN)
l14.grid(row=1, column=1, sticky=E)
bt27 = Button(f4, text="+", command=lambda: add13(), width=3, height=1, bg="light blue", activebackground="light blue",
              state=DISABLED, relief=RIDGE)
bt27.grid(row=1, column=0, sticky=N)
bt28 = Button(f4, text="-", command=lambda: sub13(), width=3, height=1, bg="light blue", activebackground="light blue",
              state=DISABLED, relief=RIDGE)
bt28.grid(row=1, column=0, sticky=S)

a2 = Checkbutton(f4, text="Cola  :#500", bg="light blue", activebackground="light blue", font=fnt, width=15, height=2,
                 anchor="w", variable=HH15, onvalue=1, offvalue=0, command=act14)
a2.grid(row=2, column=0, sticky=W)
l15 = Entry(f4, font=('arial', 18, 'bold'), width=5, bd=2, justify='right', textvariable=b15, state=DISABLED,
            relief=SUNKEN)
l15.grid(row=2, column=1, sticky=E)
bt29 = Button(f4, text="+", command=lambda: add14(), width=3, height=1, bg="light blue", activebackground="light blue",
              state=DISABLED, relief=RIDGE)
bt29.grid(row=2, column=0, sticky=N)
bt30 = Button(f4, text="-", command=lambda: sub14(), width=3, height=1, bg="light blue", activebackground="light blue",
              state=DISABLED, relief=RIDGE)
bt30.grid(row=2, column=0, sticky=S)

a3 = Checkbutton(f4, text="Coffee:#500", bg="light blue", activebackground="light blue", font=fnt, width=15, height=2,
                 anchor="w", variable=HH16, onvalue=1, offvalue=0, command=act15)
a3.grid(row=3, column=0, sticky=W)
l16 = Entry(f4, font=('arial', 18, 'bold'), width=5, bd=2, justify='right', textvariable=b16, state=DISABLED,
            relief=SUNKEN)
l16.grid(row=3, column=1, sticky=E)
bt31 = Button(f4, text="+", command=lambda: add15(), width=3, height=1, bg="light blue", activebackground="light blue",
              state=DISABLED, relief=RIDGE)
bt31.grid(row=3, column=0, sticky=N)
bt32 = Button(f4, text="-", command=lambda: sub15(), width=3, height=1, bg="light blue", activebackground="light blue",
              state=DISABLED, relief=RIDGE)
bt32.grid(row=3, column=0, sticky=S)

a4 = Checkbutton(f4, text="Orange:#300", bg="light blue", activebackground="light blue", font=fnt, width=15, height=2,
                 anchor="w", variable=HH17, onvalue=1, offvalue=0, command=act16)
a4.grid(row=4, column=0, sticky=W)
l17 = Entry(f4, font=('arial', 18, 'bold'), width=5, bd=2, justify='right', textvariable=b17, state=DISABLED,
            relief=SUNKEN)
l17.grid(row=4, column=1, sticky=E)
bt33 = Button(f4, text="+", command=lambda: add16(), width=3, height=1, bg="light blue", activebackground="light blue",
              state=DISABLED, relief=RIDGE)
bt33.grid(row=4, column=0, sticky=N)
bt34 = Button(f4, text="-", command=lambda: sub16(), width=3, height=1, bg="light blue", activebackground="light blue",
              state=DISABLED, relief=RIDGE)
bt34.grid(row=4, column=0, sticky=S)

a5 = Checkbutton(f4, text=" Water:#170", bg="light blue", activebackground="light blue", font=fnt, width=15, height=2,
                 anchor="w", variable=HH18, onvalue=1, offvalue=0, command=act17)
a5.grid(row=5, column=0, sticky=W)
l18 = Entry(f4, font=('arial', 18, 'bold'), width=5, bd=2, justify='right', textvariable=b18, state=DISABLED,
            relief=SUNKEN)
l18.grid(row=5, column=1, sticky=E)
bt35 = Button(f4, text="+", command=lambda: add17(), width=3, height=1, bg="light blue", activebackground="light blue",
              state=DISABLED, relief=RIDGE)
bt35.grid(row=5, column=0, sticky=N)
bt36 = Button(f4, text="-", command=lambda: sub17(), width=3, height=1, bg="light blue", activebackground="light blue",
              state=DISABLED, relief=RIDGE)
bt36.grid(row=5, column=0, sticky=S)

m = Label(f4, text="Meat", bg="light blue")
m["font"] = f
m.grid(row=6, column=0, sticky=W)

m1 = Checkbutton(f4, text="Pork:#1000", bg="light blue", activebackground="light blue", font=fnt, width=15, height=2,
                 anchor="w", variable=HH19, onvalue=1, offvalue=0, command=act18)
m1.grid(row=7, column=0, sticky=W)
l19 = Entry(f4, font=('arial', 18, 'bold'), width=5, bd=2, justify='right', textvariable=b19, state=DISABLED,
            relief=SUNKEN)
l19.grid(row=7, column=1, sticky=E)
bt37 = Button(f4, text="+", command=lambda: add18(), width=3, height=1, bg="light blue", activebackground="light blue",
              state=DISABLED, relief=RIDGE)
bt37.grid(row=7, column=0, sticky=N)
bt38 = Button(f4, text="-", command=lambda: sub18(), width=3, height=1, bg="light blue", activebackground="light blue",
              state=DISABLED, relief=RIDGE)
bt38.grid(row=7, column=0, sticky=S)

m2 = Checkbutton(f4, text="Beef:#1000", bg="light blue", activebackground="light blue", font=fnt, width=15, height=2,
                 anchor="w", variable=HH20, onvalue=1, offvalue=0, command=act19)
m2.grid(row=8, column=0, sticky=W)
l20 = Entry(f4, font=('arial', 18, 'bold'), width=5, bd=2, justify='right', textvariable=b20, state=DISABLED,
            relief=SUNKEN)
l20.grid(row=8, column=1, sticky=E)
bt39 = Button(f4, text="+", command=lambda: add19(), width=3, height=1, bg="light blue", activebackground="light blue",
              state=DISABLED, relief=RIDGE)
bt39.grid(row=8, column=0, sticky=N)
bt40 = Button(f4, text="-", command=lambda: sub19(), width=3, height=1, bg="light blue", activebackground="light blue",
              state=DISABLED, relief=RIDGE)
bt40.grid(row=8, column=0, sticky=S)

m3 = Checkbutton(f4, text="Asun:#1000", bg="light blue", activebackground="light blue", font=fnt, width=18, height=2,
                 anchor="w", variable=HH21, onvalue=1, offvalue=0, command=act20)
m3.grid(row=9, column=0, sticky=W)
l21 = Entry(f4, font=('arial', 18, 'bold'), width=5, bd=2, justify='right', textvariable=b21, state=DISABLED,
            relief=SUNKEN)
l21.grid(row=9, column=1, sticky=E)
bt41 = Button(f4, text="+", command=lambda: add20(), width=3, height=1, bg="light blue", activebackground="light blue",
              state=DISABLED, relief=RIDGE)
bt41.grid(row=9, column=0, sticky=N)
bt42 = Button(f4, text="-", command=lambda: sub20(), width=3, height=1, bg="light blue", activebackground="light blue",
              state=DISABLED, relief=RIDGE)
bt42.grid(row=9, column=0, sticky=S)

m4 = Checkbutton(f4, text="Bacon:#1500", bg="light blue", activebackground="light blue", font=fnt, width=25, height=2,
                 anchor="w", variable=HH22, onvalue=1, offvalue=0, command=act21)
m4.grid(row=10, column=0, sticky=W)
l22 = Entry(f4, font=('arial', 18, 'bold'), width=5, bd=2, justify='right', textvariable=b22, state=DISABLED,
            relief=SUNKEN)
l22.grid(row=10, column=1, sticky=E)
bt43 = Button(f4, text="+", command=lambda: add21(), width=3, height=1, bg="light blue", activebackground="light blue",
              state=DISABLED, relief=RIDGE)
bt43.grid(row=10, column=0, sticky=N)
bt44 = Button(f4, text="-", command=lambda: sub21(), width=3, height=1, bg="light blue", activebackground="light blue",
              state=DISABLED, relief=RIDGE)
bt44.grid(row=10, column=0, sticky=S)


payment = Label(f5, text="Payment Method ", bg="light blue", fg="steel blue", font=fnt).grid(row=0, column=0)
payment_values = ["Cash", "Bank Transfer", "Point of sales"]
payment_box= ttk.Combobox(f5, height=3, values=payment_values, state="readonly")
payment_box.set("Pick an option")
payment_box.grid(row=0, column=1)


total_button = Button(f5, text="Total $", bg="light blue", fg="steel blue", activebackground="light blue", command=lambda:cost(), width=5, font=fnt, relief=RIDGE)
total_button.grid(row=2, column=0, sticky=W)

total_display = Entry(f5, font=fnt, width=15, bd=2, justify="right", textvariable=v1, state=DISABLED, relief=SUNKEN)
total_display.grid(row=2, column=1, sticky=W)

amount_paid = Label(f5, text="Amount Paid", width=10, justify="right", bg="light blue", fg="steel blue", font=fnt)
amount_paid.grid(row=3, column=0, sticky=W)

amount_paid_display = Entry(f5, width=20, bd=2, justify="left", state=NORMAL, relief=SUNKEN)
amount_paid_display.grid(row=3, column=1, sticky=E)

reset_button = Button(f5, text="Reset", bg="light blue", activebackground="light blue", fg="steel blue", command=reset, width=5,
            font=fnt, relief=RIDGE)
reset_button.grid(row=2, column=2)

exit_button = Button(f5, text="Exit", bg="light blue", activebackground="light blue", fg="steel blue", width=5,
            command=lambda: Exit(), font=fnt, relief=RIDGE)
exit_button.grid(row=5, column=2)


change_butt0n = Button(f5, text="Change Due" ,bg="Light blue", fg="steel blue", activebackground="light blue", width=10,
                     font=fnt, relief=RIDGE)
change_butt0n.grid(row=4, column=0, sticky=W)

change_display = Entry(f5, width=20, bd=2,fg="lightblue", justify="left", state=DISABLED, relief=SUNKEN)
change_display.grid(row=4, column=1, sticky=E)

print_receipt = Button(f5, text="Print Receipt", width=12, fg="steel blue", bg="light blue",command=lambda:receipt(),
                       activebackground="light blue", font=fnt, overrelief=FLAT,relief=RIDGE)
print_receipt.grid(row=5, column=1)



parent.mainloop()
