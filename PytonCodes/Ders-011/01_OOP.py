###############################################################
############## OOP : Object Oriented Programming ##############
###############################################################
#region TEMEL ANLATIM
"""
uyeler=list()


ad="Ali"
soyad="Veli"
username="aliveli"
password="123"

uyeler.append(ad)
uyeler.append(soyad)
uyeler.append(username)
uyeler.append(password)



ad2="Değercan"
soyad2="Değer"
username2="degercan"
password2="1234"

uyeler.append(ad2)
uyeler.append(soyad2)
uyeler.append(username2)
uyeler.append(password2)



ad3="Berk"
soyad3="Can"
username3="berk"
password3="12345"

uyeler.append(ad3)
uyeler.append(soyad3)
uyeler.append(username3)
uyeler.append(password3)

print(uyeler)

kullaniciadi=input("Username:")
sifre=input("Password:")

for i in uyeler:
    if i==kullaniciadi:
        print()
"""
#endregion

"""
class User:
    name=""
    surname=""
    username=""
    password=""


uyeler=list()

uye = User() # uye=> object    uye=User() => instance(Örneklem)
uye.name="Değercan"
uye.surname="Değer"
uye.username="crazyboy"
uye.password="1"

uyeler.append(uye)
# print(uyeler)

# print(uye.name+" "+uye.surname)


uye = User()
uye.name="AltanEmre"
uye.surname="Demirci"
uye.username="sexi_velet"
uye.password="123"

uyeler.append(uye)

# print(uyeler)
# print()

kullaniciadi=input("Username:")
sifre=input("Password:")

for u in uyeler:
    if u.username==kullaniciadi and u.password==sifre:
        print(u.name+" "+u.surname )


"""

'''
class User:
    name=""
    surname=""  
    username="" 
    password= ""

    #Nesne Method(selfmethod): Nesneler üzerinden çağrılarak kullanılan methodlardır.
    #self: Classtan türeyen object'yi temsil eder.
    def Register(self):
        self.name = input("Name:")
        self.surname = input("Surname:")
        self.username = input("Username:")
        self.password = input("Password:")
    def show(self):
        print("Adınız:"+self.name+"\nSoyadınız: "+self.surname+"\nKullanıcı Adı: "+self.username+"\nPassword: "+self.password)


users=list()

uye=User()
uye.Register()
uye.show()

print(uye.name)
'''
class Insan:
    ad=""
    tc=""
    dogumTarihi=""

    def Kayit(self,liste):
        self.ad=input("AD:")
        self.tc=input("TC:")
        self.dogumTarihi=input("Doğum Tarihi:")
        liste.append(self)

    def Yaz(self):
        print(self.ad+" "+self.tc)

    # Class Method: Class üzerinden çağrılarak kullanılan methodlardır. Nesneye özel bir işlem yapılmayacaksa kullanılır.
    # cls: Class temsil eder.
    @classmethod
    def Giris(cls,liste):
        TC = input("TC:")
        Isim = input("Name:")

        for u in liste:
            if u.tc == TC and u.ad == Isim:
                print(u.tc + " " + u.dogumTarihi)

    # StaticMethod: İster class, ister nesne üzerinden erişilebilen ve herhangi bir özel parametresi olmayan klasik functiondır.
    @staticmethod
    def Listele(liste):
        for i in liste:
            print(f"Ad:{i.ad} TC:{i.tc} Doğum Tarihi:{i.dogumTarihi}")
'''

vatandas=Insan()
 
vatandas.Kayit(vatandaslar)


Insan.Giris(vatandaslar)



vatandaslar=list()
for i in range(3):
    v=Insan()
    v.Kayit(vatandaslar)

v.Listele(vatandaslar)

Insan.Listele(vatandaslar)

'''
### CONSTRUCTOR METHOD ###
"""
Kurucu method: class'tan instance alındığında otomatik çalışan methoddur.
"""
"""
class Uye:
    # gizli olarak arkaplanda bu şekilde tanımlı.
    # def __init__(self):
    #     pass

    # def __init__(self):
    #     self.Ad=input("Ad:")
    #     self.Soyad=input("Soyad:")
    #     self.Yaz()

    def __init__(self,isim,soyisim):
        self.Ad=isim
        self.Soyad=soyisim
        self.Yaz()

    def Yaz(self):
        print(self.Ad+" "+self.Soyad)

isim=input("adınız:")
u=Uye(isim,"Veli")
"""

######### N KATMANLI MİMARİ ############
'''  

class DAL:
     def __init__(self):
         print("DAL:Bağlantı sağlandı.")
         self.SQLConnection()

     def SQLConnection(self):
         print("Bağlantı Yapıldı.")
         dosya=open("veri.txt","w")
         dosya.write("Altan Emre")
         dosya.close()

class BLL:
     def __init__(self):
         dal=DAL()
         print("BLL:Bağlantı sağlandı.")


class UI:
     def __init__(self):
           bll=BLL()
           print("UI:Bağlantı sağlandı.")

user=UI()

'''


### Matematik adında bir class tanımlayınız.
# bu classa ait topla(n parametreli), cikar(2 parametre), carp(n parametreli), bol(2 parametreli) method tanımlayınız ve kullanınız.


# import Matematik
# #Documentname.classname.methodname
# Matematik.Matematik.Topla(12,13,14)


# from Matematik import Matematik

# Matematik.Topla(12,13,14)
# Matematik.Cikar(12,13)
# Matematik.Carp(12,13,14)
# Matematik.Bol(12,0)

""" SARVAR
class Matematik:
    def sayi(self):
        a = float(input("1. sayi gir: "))
        b = float(input("2. sayi gir: "))
        c = float(input("3. parametre seç: "))
        if c == "+":
            self.topla(a,b)
        elif c == "-":
            self.cikar(a,b)
        elif c == "*":
            self.carp(a,b)
        elif c == "/":
            self.bol(a,b)
    def topla(self,s1,s2):
        print(s1+s2)
    def cikar(self,s1,s2):
        print(s1-s2)
    def carp(self,s1,s2):
        print(s1*s2)
    def bol(self,s1,s2):
        print(s1/s2)

Matematik.sayi()
"""



### SORU::
# Bir Ders class'ı oluşturunuz.
# class Ders: DersAdi,DersSaati,DersOgretmeni,DersBaslamaTarihi
# class'dan bir nesne oluşturulduğunda field'lar oluşturularak içleri doldurulsun ve  Dersler.txt dosyasına kayıt işlemi gerçekleştirilsin.
# Başka class başka bir dosyada tutulsun.
"""
class Ders:
    def __init__(self,DA,DS,DO,DBT):
        self.dersAdi=DA
        self.dersSaati=DS
        self.dersOgretmeni=DO
        self.derBaslatmaTarihi=DBT
        self.Save()


    def Save(self):
        a=open("Dersler.txt","w")
        a.write(self.dersAdi+" "+self.dersSaati+" "+self.dersOgretmeni+" "+self.derBaslatmaTarihi)

d=Ders("python","19:00","Altan Emre","21/06/2022")
"""


##ÖDEV
"""
Otomobil isimli bir sınıfı Otomobil.py dosyasında tanımlayın
    Nesne Nitelikleri: Marka,Model,Renk,MotorHacmi,UretimYili
    Nesne Fonksiyonları: __init()__: Parametre olarak nesne niteliklerini alalım ve nesneyi oluşturalım
    Kaydet(): metodu sınıfa ait bilgileri o güne ait OTO_09_06_2022.txt şeklinde bir dosyaya kaydetsin
    init otomatik olarak kayıt işlemini gerçekleştirsin    
"""
## SARVAR
from Otomobil import Otomobil
oto=Otomobil()


### GULU
"""
import datetime
t=datetime.datetime.now()
class Cars:
    def _init_(self,mrk,mdl,renk,mh,yil):
        self.arabanin_markasi=mrk
        self.arabanin_modeli=mdl
        self.arabanin_rengi=renk
        self.arabanin_motorhacmi=mh
        self.arabanin_uretim_yili=yil
    def save(self):
        dosya=open("C:\\Users\\PC\\PycharmProjects\\cars.txt","a")
        dosya.write("Arabanin markasi:"+self.arabanin_markasi+" "+"Arabanin modeli:"+self.arabanin_modeli+" "+"Arabanin rengi:"+self.arabanin_rengi+" "+"Arabanin motor hacmi:"+self.arabanin_motorhacmi+" "+"Arabanin uretim yili:"+self.arabanin_uretim_yili+"   "+"Kayit Tarihi:"+str(t)+"\n")

print("* Hello *")
while True:
    k=input("\n(K)-Kayit yapmak: ").upper()
    if k=="K":
        s1=input("Arabanin markasi:").upper()
        s2=input("Arabanin modeli:").upper()
        s3=input("Arabanin rengi:").upper()
        s4=input("Arabanin motor hacmi:").upper()
        s5=input("Arabanin uretim yili:").upper()

        a=Cars(s1,s2,s3,s4,s5)
        b=Cars.save(a)
        print("Araba kayit oldu.")
    else:
        print("Kayit yapmak icin \'K\' tuslayiniz.")
        continue

"""
"""
class Dog:
    name=""
    age=""
    gender=""

    def Kayit(self,liste):
        self.name=input("dog's name:").capitalize()
        self.age=int(input("dog's age:"))
        self.gender=input("dog's gender:").capitalize()
        liste.append(self)

    def KopeginBilgileriniEkranaYazdir(self,whats_your_dogs_name,liste):
        if len(liste)>0:
            find=False
            for d in liste:
                if whats_your_dogs_name==d.name:
                    print("\ndog's name=",d.name,"\ndog's age=",d.age,"\ndog's gender=",d.gender)
                    find=True
                    break
            if find==False:
                print("\nThere isn't dog by this name.\n")                
        else:
            print("List is null")



dogs_listem=list()

print("* Hello *")
while True:
    try:
        soru=int(input("How can I help you?\n1-Registration\n2-Information about the dog\n:"))
        if soru==1:
            kopek=Dog()
            kopek.Kayit(dogs_listem)
            print("\nRegistration completed successfully.\n")
        elif soru==2:
            soru2=input("\nPlease, write dog's name:").capitalize()
            kopek=Dog()
            kopek.KopeginBilgileriniEkranaYazdir(soru2,dogs_listem)
        else: print("\nYou made the wrong choice. Please try again...\n")
    except ValueError: print("\nPlease, use numbers.\n")
"""




