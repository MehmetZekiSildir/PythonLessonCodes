from tkinter import *

AnaPencere = Tk()
AnaPencere.geometry("800x800")
AnaPencere.title("Tkinter-Frame")

AnaPencere.config(bg="beige")

### Cerceve_1 elemanları alt alta hizalama ###
Cerceve_1=Frame(AnaPencere,bg="firebrick",cursor="pirate")
Cerceve_1.pack(fill=X,padx=10,pady=5,ipadx=4,ipady=4)

"""
fill=X => Frame'in x düzelminde yerleşmesini sağlar.
padx => Frame'in dışarıdaki diğer elemanlar ile arasına x düzelemin vereceği aralık değeridir
pady => Frame'in dışarıdaki diğer elemanlar ile arasına y düzelemin vereceği aralık değeridir
ipadx => Frame'in içindeki elemanlar ile arasına x düzelemin vereceği aralık değeridir
ipady => Frame'in içindeki elemanlar ile arasına y düzelemin vereceği aralık değeridir
"""

yazi_1=Label(Cerceve_1,bg="#DAB123",text="MERHABA",font=("Comic Sans",16),fg="#455625")
yazi_1.pack(fill=X,padx=50,pady=100,ipadx=25,ipady=55)

girdi_1=Entry(Cerceve_1,bg="pink",font=("Comic Sans",15),fg="red")
girdi_1.pack(fill=X,padx=50,pady=50)


### Cerceve_2'de elemanları yan yana hizalama
Cerceve_2=Frame(AnaPencere,bg="teal",cursor="star")
Cerceve_2.pack(fill=X,padx=10,pady=10,ipadx=4,ipady=5)

yazi_2=Label(Cerceve_2,bg="#DAB456",text="DÜNYA",font=("Comic Sans",16),fg="indigo")
yazi_2.pack(side=LEFT,padx=10,pady=5,ipadx=10,ipady=10)

btn_2=Button(Cerceve_2,bg="Khaki",text="BUTON 2")
btn_2.pack(side=LEFT,padx=10,pady=5,ipadx=10,ipady=10)

girdi_2=Entry(Cerceve_2,bg="white",font=("Comic Sans",15))
girdi_2.pack(side=RIGHT,padx=10,pady=10,ipadx=6,ipady=5)


### Cerceve_3 ve Cerceve_4 Framelerini yan yana hizalama

Cerceve_3=Frame(AnaPencere,bg="chocolate",cursor="clock")
Cerceve_3.pack(side=LEFT,padx=10,pady=10,ipadx=4,ipady=5)
yazi_3=Label(Cerceve_3,bg="#DAB456",text="DÜNYA",font=("Comic Sans",16),fg="indigo",borderwidth=10,relief="sunken")
yazi_3.pack(side=LEFT,padx=10,pady=5,ipadx=10,ipady=10)

img = PhotoImage(file="kus.gif")
img1 = img.subsample(5,5)
Label(Cerceve_3,image=img1).pack(side=LEFT,padx=10,pady=10)


Cerceve_4=Frame(AnaPencere,bg="chocolate",cursor="clock")
Cerceve_4.pack(side=LEFT,padx=10,pady=10,ipadx=4,ipady=5)
yazi_4=Label(Cerceve_4,bg="#DAB456",text="DÜNYA",font=("Comic Sans",16),fg="indigo")
yazi_4.pack(side=LEFT,padx=10,pady=5,ipadx=10,ipady=10)


AnaPencere.mainloop()