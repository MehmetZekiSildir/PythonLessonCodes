######### TKINTER ############
"""
Python diline ait UI(User Interface - Kullanıcı Arayüzü) Tkinter,pyqt5
"""



from tkinter import *

def Topla():
    s1=int(sayi1.get())
    s2=int(sayi2.get())
    toplam=s1+s2
    sonuc.insert(0,toplam)


pencere=Tk()
pencere.geometry("900x800+150+150") #widthxheight+xnoktası+ynoktası

pencere.title("İlk GUI Programınızı")

#1.Yöntem
Label(pencere,text="1.Sayı:",font=("Consolas",18)).place(x=5,y=10)

#2.Yöntem
sayi1=Entry(pencere,text="",font=("Consolas",18))
sayi1.place(x=100,y=10)

Label(pencere,text="2.Sayı:",font=("Consolas",18)).place(x=400,y=10)

#3.Yöntem
sayi2=Entry(pencere,text="",font=("Consolas",18))
sayi2.place(x=495,y=10)

btn_topla=Button(pencere,text="Topla",font=("Consolas",18),command=Topla).place(x=350,y=50)

Label(pencere,text="SONUÇ:",font=("Consolas",18)).place(x=150,y=100)

#3.Yöntem
sonuc=Entry(pencere,text="",font=("Consolas",18))
sonuc.place(x=350,y=100)





pencere.mainloop()
