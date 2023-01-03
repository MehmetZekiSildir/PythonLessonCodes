from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import datetime
from Veritabani import VeriTabani
from Grafik import Grafik
from Kur import Kur
import threading

class Doviz:
    pencere=Tk()
    tab_control=Notebook(pencere)
    tab_altin=Frame(tab_control)
    tab_dolar=Frame(tab_control)
    tab_euro=Frame(tab_control)

    tab_control.add(tab_altin,text="Altın")
    tab_control.add(tab_dolar,text="Dolar")
    tab_control.add(tab_euro,text="Euro")

    tab_control.grid(row=0,column=0,ipadx=10,ipady=10)

    @classmethod
    def zamanFormat(cls,zamanStr):
        zamanKisa=[]
        for z in zamanStr:
            zmn=datetime.datetime.strptime(z,"%d.%m.%Y %H:%M:%S")
            zmn=zmn.strftime("%d.%m %H:%M")
            zamanKisa.append(zmn)
        return zamanKisa

    @classmethod
    def tekrar(cls):
        komut="SELECT zaman,kur FROM tb_altin ORDER BY(zaman)"
        altinKur=VeriTabani.KurGetir(komut)
        x=[row[0] for row in altinKur]
        xf=cls.zamanFormat(x)
        y=[row[1] for row in altinKur]
        Grafik.Ciz(cls.tab_altin,xf,y,"Altın Kuru")

        komut = "SELECT zaman,kur FROM tb_dolar ORDER BY(zaman)"
        dolarKur = VeriTabani.KurGetir(komut)
        x = [row[0] for row in dolarKur]
        xf = cls.zamanFormat(x)
        y = [row[1] for row in dolarKur]
        Grafik.Ciz(cls.tab_dolar, xf, y, "Dolar Kuru")

        komut = "SELECT zaman,kur FROM tb_euro ORDER BY(zaman)"
        euroKur = VeriTabani.KurGetir(komut)
        x = [row[0] for row in euroKur]
        xf = cls.zamanFormat(x)
        y = [row[1] for row in euroKur]
        Grafik.Ciz(cls.tab_euro, xf, y, "Euro Kuru")

        altin=threading.Thread(target=Kur.Getir, args=["altin"])
        dolar=threading.Thread(target=Kur.Getir, args=["dolar"])
        euro=threading.Thread(target=Kur.Getir, args=["euro"])

        altin.start()
        dolar.start()
        euro.start()

        cls.pencere.after(60000,cls.tekrar)


altin = threading.Thread(target=Kur.Getir, args=["altin"])
dolar = threading.Thread(target=Kur.Getir, args=["dolar"])
euro = threading.Thread(target=Kur.Getir, args=["euro"])

altin.start()
dolar.start()
euro.start()

Doviz.tekrar()
Doviz.pencere.mainloop()