from tkinter import *
import tkinter.font as font
import math

root = Tk()
root.title("KALKULATOR")
root.geometry("310x400")
root["bg"] = "#E0FFFF"

myfont = font.Font(size=15)

e = Entry(root, width=25, borderwidth=0)
e["font"] = myfont
e["bg"] = "#ADD8E6"
e.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

def number(score):
    before = e.get()
    e.delete(0, END)
    e.insert(0, str(before) + str(score))

def penambahan():
    first_num = e.get()
    global f_num
    global mat
    mat = "penambahan"
    f_num = int(first_num)
    e.delete(0, END)

def pengurangan():
    first_num = e.get()
    global f_num
    global mat
    mat = "pengurangan"
    f_num = int(first_num)
    e.delete(0, END)

def perkalian():
    first_num = e.get()
    global f_num
    global mat
    mat = "perkalian"
    f_num = int(first_num)
    e.delete(0, END)

def pembagian():
    first_num = e.get()
    global f_num
    global mat
    mat = "pembagian"
    f_num = int(first_num)
    e.delete(0, END)

def akar():
    first_num = e.get()
    global f_num
    f_num = int(first_num)
    e.delete(0, END)
    e.insert(0, math.sqrt(f_num))

def sisa():
    first_num = e.get()
    global f_num
    global mat
    mat = "sisa"
    f_num = int(first_num)
    e.delete(0, END)

def pangkat():
    first_num = e.get()
    global f_num
    f_num = int(first_num)
    e.delete(0, END)
    e.insert(0, f_num **2)

def hapus():
    e.delete(0, END)

def hasil():
    end_num = e.get()
    e.delete(0, END)
    if mat == "penambahan":
        e.insert(0, f_num + int(end_num))
    elif mat == "pengurangan":
        e.insert(0, f_num - int(end_num))
    elif mat == "perkalian":
        e.insert(0, f_num * int(end_num))
    elif mat == "pembagian":
        try:
            countt = f_num / int(end_num)
            e.insert(0, countt)
        except ZeroDivisionError:
            e.insert(0, '-Maaf, perhitungan tidak valid-')
    elif mat == "sisa":
        e.insert(0, f_num % int(end_num))






btn1 = Button(root, text="1", padx=30, bg="#5F9EA0", fg="black", pady=20, command=lambda:number(1))
btn2 = Button(root, text="2", padx=30, bg="#5F9EA0", fg="black", pady=20, command=lambda:number(2))
btn3 = Button(root, text="3", padx=30, bg="#5F9EA0", fg="black", pady=20, command=lambda:number(3))
btn4 = Button(root, text="4", padx=30, bg="#5F9EA0", fg="black", pady=20, command=lambda:number(4))
btn5 = Button(root, text="5", padx=30, bg="#5F9EA0", fg="black", pady=20, command=lambda:number(5))
btn6 = Button(root, text="6", padx=30, bg="#5F9EA0", fg="black", pady=20, command=lambda:number(6))
btn7 = Button(root, text="7", padx=30, bg="#5F9EA0", fg="black", pady=20, command=lambda:number(7))
btn8 = Button(root, text="8", padx=30, bg="#5F9EA0", fg="black", pady=20, command=lambda:number(8))
btn9 = Button(root, text="9", padx=30, bg="#5F9EA0", fg="black", pady=20, command=lambda:number(9))
btn0 = Button(root, text="0", padx=30, bg="#5F9EA0", fg="black", pady=20, command=lambda:number(0))

plus = Button(root, text="+", padx=30, bg="#ADD8E6", fg="black", pady=20, command=penambahan)
mins = Button(root, text="-", padx=30, bg="#ADD8E6", fg="black", pady=20, command=pengurangan)
mult = Button(root, text="x", padx=30, bg="#ADD8E6", fg="black", pady=20, command=perkalian)
dist = Button(root, text="/", padx=30, bg="#ADD8E6", fg="black", pady=20, command=pembagian)
dlte = Button(root, text="C", padx=30, bg="#7FFFD4", fg="black", pady=20, command=hapus)
rlst = Button(root, text="=", padx=70, bg="#7FFFD4", fg="black", pady=20, command=hasil)

squro = Button(root, text="√", padx=30, bg="#ADD8E6", fg="black", pady=20, command=akar)
rest = Button(root, text="//2", padx=30, bg="#ADD8E6", fg="black", pady=20, command=sisa)
squis = Button(root, text="²", padx=30, bg="#ADD8E6", fg="black", pady=20, command=pangkat)

btn1.grid(row=3, column=0, pady=2)
btn2.grid(row=3, column=1, pady=2)
btn3.grid(row=3, column=2, pady=2)
btn4.grid(row=2, column=0, pady=2)
btn5.grid(row=2, column=1, pady=2)
btn6.grid(row=2, column=2, pady=2)
btn7.grid(row=1, column=0, pady=2)
btn8.grid(row=1, column=1, pady=2)
btn9.grid(row=1, column=2, pady=2)
btn0.grid(row=4, column=1, pady=2)

plus.grid(row=1, column=3, pady=2)
mins.grid(row=2, column=3, pady=2)
mult.grid(row=3, column=3, pady=2)
dist.grid(row=4, column=3, pady=2)
dlte.grid(row=4, column=0, pady=2)
rlst.grid(row=5, column=2, pady=2, columnspan=2)

squro.grid(row=5, column=0, pady=2)
rest.grid(row=4, column=2, pady=2)
squis.grid(row=5, column=1, pady=2)





root.mainloop()