def Topla():
    s1=int(txt1.get())
    s2=int(txt2.get())
    sonuc=s1+s2
    txt_sonuc.delete(0, END)
    txt_sonuc.insert(0,sonuc)

def Cikar():
    s1=int(txt1.get())
    s2=int(txt2.get())
    sonuc=s1-s2
    txt_sonuc.delete(0,END)
    txt_sonuc.insert(0,sonuc)

def Carp():
    s1=int(txt1.get())
    s2=int(txt2.get())
    sonuc=s1*s2
    txt_sonuc.delete(0, END)
    txt_sonuc.insert(0,sonuc)

def Bol():
    s1=int(txt1.get())
    s2=int(txt2.get())
    sonuc=s1//s2
    txt_sonuc.delete(0, END)
    txt_sonuc.insert(0,sonuc)

from tkinter import *

pencere=Tk()
pencere.config(bg="pink")
pencere.title("Yanyana Ekleme")
pencere.geometry("670x130+150+500") #widthxheight+x koordinat+y koordinat
pencere.maxsize(750,750)
pencere.minsize(650,250)
txt1=Entry(pencere,text="", fg="Red", font=("Consolas",15),bd=5)
txt1.place(x=5,y=10)
txt2=Entry(pencere,text="", fg="Red", font=("Consolas",15),bd=5)
txt2.place(x=5,y=60)


btn_arti=Button(pencere,text="+",width=4,height=2,command=Topla)
btn_arti.place(x=5,y=100)

btn_eksi=Button(pencere,text="-",width=4,height=2,command=Cikar)
btn_eksi.place(x=45,y=100)

btn_carp=Button(pencere,text="*",width=4,height=2,command=Carp)
btn_carp.place(x=85,y=100)


btn_bol=Button(pencere,text="/",width=4,height=2,command=Bol)
btn_bol.place(x=125,y=100)

lbl_sonuc=Label(pencere,text="SONUC:",font=("Consolas",15))
lbl_sonuc.place(x=255,y=10)
txt_sonuc=Entry(pencere,text="", fg="Red", font=("Consolas",15),bd=5)
txt_sonuc.place(x=335,y=10)


pencere.mainloop()