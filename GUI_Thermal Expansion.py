from tkinter import *
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from PIL import ImageTk, Image

root = Tk()
root.title ('Farah Judith GUI')
root.geometry('450x150+10+10')
Label(root, text = 'Thermal Expansion',  
          background = 'skyblue', foreground ='white',  
          font = ('Arial', 15)).place(x=130, y=0)
root.config (bg = '#243447')

def length():
    topL = Toplevel()
    topL.title('Length Expansion')
    topL.geometry('1400x500+10+10')
    topL.config(bg = '#243447')

    lbl1=Label(topL, text='Length Expansion', font ='Arial 14 bold underline', bg = '#243447', fg = 'white',)
    lbl1.place(x=400, y=50)

#entry of coefficient
    
    lbl2=Label(topL, text='Coefficient α', font = ('Arial', 12), bg = '#243447', fg = 'white')
    lbl2.place(x=100, y=100)
    lbl2b=Label(topL, text='1/°C', font = ('Arial', 12), bg = '#243447', fg = 'white')
    lbl2b.place(x=400, y=100)
    α=Entry(topL, borderwidth=3)
    α.place(x=250, y=100)

#entry of X0
    
    lbl3=Label(topL, text='Original Length', font = ('Arial', 12), bg = '#243447', fg = 'white')
    lbl3.place(x=100, y=150)
    lbl3b=Label(topL, text='m', font = ('Arial', 12), bg = '#243447', fg = 'white')
    lbl3b.place(x=400, y=150)
    X0=Entry(topL, borderwidth=3)
    X0.place(x=250, y=150)

#entry of T0
    
    lbl4=Label(topL, text= 'Initial Temperature', font = ('Arial', 12), bg = '#243447', fg = 'white')
    lbl4.place(x=100, y=200)
    lbl4b=Label(topL, text='°C', font = ('Arial', 12), bg = '#243447', fg = 'white')
    lbl4b.place(x=400, y=200)
    T0=Entry(topL, borderwidth=3)
    T0.place(x=250, y=200)
    
#entry of Tf
    
    lbl5=Label(topL, text= 'Final Temperature', font = ('Arial', 12), bg = '#243447', fg = 'white')
    lbl5.place(x=100, y=250)
    lbl5b=Label(topL, text='°C', font = ('Arial', 12), bg = '#243447', fg = 'white')
    lbl5b.place(x=400, y=250)
    T=Entry(topL, borderwidth=3)
    T.place(x=250, y=250)

#reset button

    def reset():
        α.delete(0, END)
        X0.delete(0, END)
        T0.delete(0, END)
        T.delete(0, END)
    btReset=Button(topL, text = 'Reset', bg = '#800000', fg='white', font = ('Arial', 13), command = reset).place(x=135, y=300)
    
#calculate button

    def result():
        ΔT = float(T.get()) - float(T0.get())
        A = float(α.get())*float(ΔT)
        L = float(X0.get())*(1+float(A))
        Ltotal = float(L)+float(X0.get())
        ltotal = Label(topL, text = str(Ltotal) + ' m', font = ('Arial', 12)).place(x = 270, y = 400)
        ΔL = Label(topL, text = str(L) + ' m', font = ('Arial', 12)).place(x = 270, y = 350)
        
    btCalculate=Button(topL, text = 'Calculate', bg = 'green', fg = 'white', font = ('Arial', 13), command = result).place(x=220, y=300)

    lbl6=Label(topL, text = 'Results', font = ('Arial', 12), bg = '#243447', fg = 'white').place(x = 100, y = 350)
    lbl7=Label(topL, text = 'Total Length Expansion', font = ('Arial', 12), bg = '#243447', fg = 'white').place(x = 100, y = 400)

    def graph():
        ΔT = float(T.get()) - float(T0.get())
        A = float(α.get())*float(ΔT)
        L = float(X0.get())*(1+float(A))
        d = float(X0.get())*float(ΔT)
        xAxis = [0, d] 
        yAxis = [0, L] 
        fig1 = Figure(figsize=(5,4), dpi=100)
        sb1 = fig1.add_subplot(211)
        sb1.plot(xAxis,yAxis, color = 'black')
        fig = FigureCanvasTkAgg(fig1, topL)
        fig.get_tk_widget().pack(side=tk.RIGHT, fill=tk.NONE, expand=0)
        sb1.set_xlabel ('L0.ΔT')
        sb1.set_ylabel ('Length Expansion ΔL')
        sb1.set_title ('Length Expansion Graphic')
        
    btGraph=Button(topL, text = 'Show Graph', bg = 'Black', fg = 'white', font = ('Arial', 13), command = graph).place(x=330, y=300)

#image
    
    path='D:\\RED\\Algorithm\\linear.png'
    img = Image.open(path)
    photo = ImageTk.PhotoImage(img)
    labelL=Label(topL, image=photo)
    labelL.image = photo
    labelL.place(x=500,y=100)

#area Expansion#
    
def area():
    topA = Toplevel()
    topA.title('Area Etention')
    topA.geometry('1200x500+10+10')
    topA.config(bg = '#243447')

    lbl1=Label(topA, text='Area Expansion', font = 'Arial 14 bold underline', bg = '#243447', fg = 'white',)
    lbl1.place(x=400, y=50)

#entry of coefficient

    lbl2=Label(topA, text='Coefficient α', font = ('Arial', 12), bg = '#243447', fg = 'white')
    lbl2.place(x=100, y=100)
    lbl2b=Label(topA, text='1/°C', font = ('Arial', 12), bg = '#243447', fg = 'white')
    lbl2b.place(x=400, y=100)
    α=Entry(topA, borderwidth=3)
    α.place(x=250, y=100)

#entry of X0

    lbl3=Label(topA, text='Original Area', font = ('Arial', 12), bg = '#243447', fg = 'white')
    lbl3.place(x=100, y=150)
    lbl3b=Label(topA, text='m²', font = ('Arial', 12), bg = '#243447', fg = 'white')
    lbl3b.place(x=400, y=150)
    X0=Entry(topA, borderwidth=3)
    X0.place(x=250, y=150)

#entry of T0

    lbl4=Label(topA, text= 'Initial Temperature', font = ('Arial', 12), bg = '#243447', fg = 'white')
    lbl4.place(x=100, y=200)
    lbl4b=Label(topA, text='°C', font = ('Arial', 12), bg = '#243447', fg = 'white')
    lbl4b.place(x=400, y=200)
    T0=Entry(topA, borderwidth=3)
    T0.place(x=250, y=200)

#entry of Tf

    lbl5=Label(topA, text= 'Final Temperature', font = ('Arial', 12), bg = '#243447', fg = 'white')
    lbl5.place(x=100, y=250)
    lbl5b=Label(topA, text='°C', font = ('Arial', 12), bg = '#243447', fg = 'white')
    lbl5b.place(x=400, y=250)
    T=Entry(topA, borderwidth=3)
    T.place(x=250, y=250)

#reset button
    
    def reset():
        α.delete(0, END)
        X0.delete(0, END)
        T0.delete(0, END)
        T.delete(0, END)
    btReset=Button(topA, text = 'Reset', bg = '#800000', fg='white', font = ('Arial', 13), command = reset).place(x=135, y=300)

#calculate button

    def result():
        ΔT = float(T.get()) - float(T0.get())
        A = 2*float(α.get())*float(ΔT)
        L = float(X0.get())*(1+float(A))
        Ltotal = float(L)+float(X0.get())
        ltotal = Label(topA, text = str(Ltotal) + ' m²', font = ('Arial', 12)).place(x = 260, y = 400)
        ΔL = Label(topA, text = str(L) + ' m²', font = ('Arial', 12)).place(x = 260, y = 350)
        
    btCalculate=Button(topA, text = 'Calculate', bg = 'green', fg = 'white', font = ('Arial', 13), command = result).place(x=220, y=300)

    lbl6=Label(topA, text = 'Results', font = ('Arial', 12), bg = '#243447', fg = 'white').place(x = 100, y = 350)
    lbl7=Label(topA, text = 'Total Area Expansion', font = ('Arial', 12), bg = '#243447', fg = 'white').place(x = 100, y = 400)

#graph
    
    def graph():
        ΔT = float(T.get()) - float(T0.get())
        A = 2*float(α.get())*float(ΔT)
        L = float(X0.get())*(1+float(A))
        d = float(X0.get())*float(ΔT)
        xAxis = [0, d] 
        yAxis = [0, L] 
        fig1 = Figure(figsize=(4,4), dpi=100)
        sb1 = fig1.add_subplot(211)
        sb1.plot(xAxis,yAxis, color = 'black')
        fig = FigureCanvasTkAgg(fig1, topA)
        fig.get_tk_widget().pack(side=tk.RIGHT, fill=tk.NONE, expand=0)
        sb1.set_xlabel ('A0.ΔT')
        sb1.set_ylabel ('Area Expansion ΔA')
        sb1.set_title ('Area Expansion Graphic')


    btGraph=Button(topA, text = 'Show Graph', bg = 'Black', fg = 'white', font = ('Arial', 13), command = graph).place(x=330, y=300)
#image
    
    path='D:\\RED\\Algorithm\\area.png'
    img = Image.open(path)
    photo = ImageTk.PhotoImage(img)
    labelA=Label(topA, image=photo)
    labelA.image = photo
    labelA.place(x=500,y=100)


#volume Expansion#
    
def vol():
    topV = Toplevel()
    topV.title('Volume Extension')
    topV.geometry('1200x500+10+10')
    topV.config(bg = '#243447')

    lbl1=Label(topV, text='Volume Expansion', font = 'Arial 14 bold underline', bg = '#243447', fg = 'white',)
    lbl1.place(x=400, y=50)

#entry of coefficient

    lbl2=Label(topV, text='Coefficient α', font = ('Arial', 12), bg = '#243447', fg = 'white')
    lbl2.place(x=100, y=100)
    lbl2b=Label(topV, text='1/°C', font = ('Arial', 12), bg = '#243447', fg = 'white')
    lbl2b.place(x=400, y=100)
    α=Entry(topV, borderwidth=3)
    α.place(x=250, y=100)

#entry of X0

    lbl3=Label(topV, text='Original Volume', font = ('Arial', 12), bg = '#243447', fg = 'white')
    lbl3.place(x=100, y=150)
    lbl3b=Label(topV, text='m³', font = ('Arial', 12), bg = '#243447', fg = 'white')
    lbl3b.place(x=400, y=150)
    X0=Entry(topV, borderwidth=3)
    X0.place(x=250, y=150)

#entry of T0

    lbl4=Label(topV, text= 'Initial Temperature', font = ('Arial', 12), bg = '#243447', fg = 'white')
    lbl4.place(x=100, y=200)
    lbl4b=Label(topV, text='°C', font = ('Arial', 12), bg = '#243447', fg = 'white')
    lbl4b.place(x=400, y=200)
    T0=Entry(topV, borderwidth=3)
    T0.place(x=250, y=200)

#entry of Tf

    lbl5=Label(topV, text= 'Final Temperature', font = ('Arial', 12), bg = '#243447', fg = 'white')
    lbl5.place(x=100, y=250)
    lbl5b=Label(topV, text='°C', font = ('Arial', 12), bg = '#243447', fg = 'white')
    lbl5b.place(x=400, y=250)
    T=Entry(topV, borderwidth=3)
    T.place(x=250, y=250)

#reset button

    def reset():
        α.delete(0, END)
        X0.delete(0, END)
        T0.delete(0, END)
        T.delete(0, END)
    btReset=Button(topV, text = 'Reset', bg = '#800000', fg='white', font = ('Arial', 13), command = reset).place(x=135, y=300)

#calculate button
    
    def result():
        ΔT = float(T.get()) - float(T0.get())
        A = 3*float(α.get())*float(ΔT)
        L = float(X0.get())*(1+float(A))
        Ltotal = float(L)+float(X0.get())
        ltotal = Label(topV, text = str(Ltotal) + ' m³', font = ('Arial', 12)).place(x = 280, y = 400)
        ΔL = Label(topV, text = str(L) + ' m³', font = ('Arial', 12)).place(x = 280, y = 350)
        
    btCalculate=Button(topV, text = 'Calculate', bg = 'green', fg = 'white', font = ('Arial', 13), command = result).place(x=220, y=300)

    lbl6=Label(topV, text = 'Results', font = ('Arial', 12), bg = '#243447', fg = 'white').place(x = 100, y = 350)
    lbl7=Label(topV, text = 'Total Volume Expansion', font = ('Arial', 12), bg = '#243447', fg = 'white').place(x = 100, y = 400)

#graph

    def graph():
        ΔT = float(T.get()) - float(T0.get())
        A = 3*float(α.get())*float(ΔT)
        L = float(X0.get())*(1+float(A))
        d = float(X0.get())*float(ΔT)
        xAxis = [0, d] 
        yAxis = [0, L] 
        fig1 = Figure(figsize=(4,4), dpi=100)
        sb1 = fig1.add_subplot(211)
        sb1.plot(xAxis,yAxis, color = 'black')
        fig = FigureCanvasTkAgg(fig1, topV)
        fig.get_tk_widget().pack(side=tk.RIGHT, fill=tk.NONE, expand=0)
        sb1.set_xlabel ('V0.ΔT')
        sb1.set_ylabel ('Volume Expansion ΔV')
        sb1.set_title ('Volume Expansion Graphic')

    btGraph=Button(topV, text = 'Show Graph', bg = 'Black', fg = 'white', font = ('Arial', 13), command = graph).place(x=330, y=300)
    
#image
    
    path='D:\\RED\\Algorithm\\volume.png'
    img = Image.open(path)
    photo = ImageTk.PhotoImage(img)
    labelV=Label(topV, image=photo)
    labelV.image = photo
    labelV.place(x=500,y=100)
    
lbl1=Label(root, text='Type of Expansion', font = ('Arial', 13), bg = '#243447', fg = 'white')
lbl1.place(x=140, y=50)
bt1=Button (root, text = 'Length',  font = ('Arial', 12), command = length).place(x=100, y=100)
bt2=Button (root, text = 'Area',  font = ('Arial', 12), command = area).place(x=180, y=100)
bt3=Button (root, text = 'Volume',  font = ('Arial', 12), command = vol).place(x=250, y=100)                                         

root.mainloop()
