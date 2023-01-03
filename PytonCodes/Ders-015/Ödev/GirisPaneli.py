from Uye import Uye
from tkinter import *
from tkinter import messagebox


def kayityapma():
    pencere.destroy()
    import KayitPaneli
    KayitPaneli.pencere.mainloop()

def girisyapma():
    parola=sifregiris.get()
    kullaniciadi=kullaniciadigiris.get()
    if(parola!="" and kullaniciadi!=""):
        uye=Uye()
        uye=Uye.LoginUser(kullaniciadi,parola)
        if(uye!=-1 and uye.Username!="" and uye.Password!=""):
            messagebox.showinfo("BİLGİ","GİRİŞ BAŞARILI")
        else:
            messagebox.showerror("HATA","GİRİŞ BAŞARISIZ")
            messagebox.showerror("HATA","KAYITLI KULLANICI BULUNAMADI")
            kullaniciadigiris.delete(0,END)
            sifregiris.delete(0,END)
    else:
        messagebox.showwarning("UYARI","Kullanıcı adı ve Şifre alanlarını boş geçemezsiniz!!!")


pencere=Tk()
pencere.geometry("400x240")
pencere.title("GİRİŞ PANELİ")

kullaniciadi=Label(text="Username:",font=("Consolas",12))
kullaniciadi.place(x=5,y=10)
kullaniciadigiris=Entry(text="",width=45,bd=3)
kullaniciadigiris.place(x=105,y=10)


sifre=Label(text="Şifreniz:",font=("Consolas",12))
sifre.place(x=5,y=40)
sifregiris=Entry(text="",width=45,bd=3)
sifregiris.place(x=105,y=40)

giris=Button(text="GİRİŞ",width=25,bd=3,command=girisyapma)
giris.place(x=5,y=70)
giris=Button(text="KAYIT",width=25,bd=3,command=kayityapma)
giris.place(x=195,y=70)

pencere.mainloop()


