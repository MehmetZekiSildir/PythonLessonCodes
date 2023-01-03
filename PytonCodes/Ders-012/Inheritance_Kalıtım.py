########## KALITIM - INHERITANCE ###########
"""
Inheritance veya kalıtım bir sınıfın başka bir sınıfan özelliklerini(attribute) ve metodlarını miras almasıdır.
Bu yapı aslında bizim kend anne babamızdan değişik özelliklerive davranışları miras almamıza benzetilebilir.

Örneğin, bir şirketin çalışanlarını tasarlamak için sınıflar oluşturuyoruz. Bunun için Yönetici, Proje Direktörü, İşçi gibi sınıflar oluşturmamız gerekiyor.
Aslında baktığımız zaman bu sınıfların hepsinin belli ortak metodları ve özellikleri bulunuyor.
O zaman bu ortak özellikleri ve metotları tekrar tekrar bu sınfıların içinde tanımlamak yerine, bir tane ana-temel(base) class tanımlayıp ortak özellik ve metotları bu class'ta yazıp diğer classların bu base classı miras almasını sağlayabiliriz. Inheritance'ın temel amacı budur.

OOP bir kuralı var ki her class sadece BİR TANE MİRAS ALABİLİR. NO MULTIPLE INHERITANCE

### super(): base(miras alınan sınıfı temsil eder)
"""

"""
import datetime


class Calisan:
    ad=""
    soyad=""
    tc=""
    sgkNo=0
    import datetime
    dogumTarihi=datetime.datetime.now().date()
    medeniDurum=""

    def Yaz(self):
        print(f"{self.ad} {self.soyad}")

class IK(Calisan):
    personelSayisi=0

    def Yaz(self):
        super().Yaz()
        print(self.personelSayisi)

class IT(Calisan):
    programSayisi=0

class MUH(Calisan):
    hesapSayisi=0

insanKaynaklari=IK()
# print(insanKaynaklari.dogumTarihi)
insanKaynaklari.ad="Altan"
insanKaynaklari.soyad="Emre"
insanKaynaklari.personelSayisi=5

insanKaynaklari.Yaz()

# m=MUH()
# print(m.medeniDurum)

"""

## ÖDEV
## Otomobil: Marka,Model,Renk,UretimYili,Fiyat,IlanTarihi,KasaTipi,VitesTipi  --- Kaydet() BilgiYazdir()
## Kamyon: Marka,Model,Renk,UretimYili,Fiyat,IlanTarihi,YakıtDepoSayisi,TasimaKapasitesi  ---  Kaydet() BilgiYazdir()

'''
class Arac:
    Marka=""
    Model=str()
    Renk=""
    UretimYili=""
    Fiyat=""
    from datetime import datetime
    IlanTarihi=datetime.now().date().strftime("%d/%m/%Y")

    def Kaydet(self):
        self.Marka=input("Marka:")
        self.Model=input("Model:")
        self.Renk=input("Renk:")
        self.UretimYili=input("Üretim Yılı:")
        self.Fiyat=input("Fiyat:")


    def BilgiYazdir(self):
        print(f"""{self.Marka}
{self.Model}
{self.Renk}
{self.Fiyat}
{self.UretimYili}
{self.IlanTarihi}""")


class Otomobil(Arac):
    KasaTipi=""
    VitesTipi=""

    def Kaydet(self,liste):
        super().Kaydet()
        self.KasaTipi=input("Kasa Tipi:")
        self.VitesTipi=input("Vites Tipi:")
        liste.append(self)

    def BilgiYazdir(self):
        super().BilgiYazdir()
        print(self.KasaTipi+"\n"+self.VitesTipi)

class Kamyon(Arac):
    YakitDepoSayisi=0
    TasimaKapasitesi=0

    def Kaydet(self,liste):
        super().Kaydet()
        self.YakitDepoSayisi=int(input("Yakıt Depo Sayısı:"))
        self.TasimaKapasitesi=int(input("Taşıma Kapasitesi:"))
        liste.append(self)

    def BilgiYazdir(self):
        super().BilgiYazdir()
        print(self.YakitDepoSayisi)
        print(self.TasimaKapasitesi)

# araclar=list()
#
# oto=Arac()
# oto.Kaydet(araclar)
# oto.BilgiYazdir()
# print(araclar)

# otolar=list()
# oto=Otomobil()
# oto.Kaydet(otolar)
# oto.BilgiYazdir()

# kamyonlar=list()
# kmyn=Kamyon()
# kmyn.Kaydet(kamyonlar)
# kmyn.BilgiYazdir()
'''

### BEYAZ ESYA ÖRNEĞİ
# Buzdolabi: Marka,Model,Enerji,Fiyat,Hacmi,KapakSayisi   --- KAYDET(): dosyaya yazdırma işlemi yapsın
# Camaşır Makinesi: Marka,Model,Enerji,Fiyat,Yıkama Kapasitesi,HızlıYıkama --- KAYDET(): dosyaya yazdırma işlemi yapsın

'''ALİREZA
import os
if not os.path.exists("C:\\TEST"):
    os.mkdir("C:\\TEST")

import datetime
today=datetime.datetime.now()
d3 = today.strftime("%d.%m.%Y %H:%M:%S")

Document=open("C:\\TEST\\HoseholdAppliances.txt",mode="w")
class HouseholdAppliances:
    Brand=""
    ModelName=str()
    EnergyType=""
    Price=str()

    def save(self):
        self.Brand=input("Enter Brand Name:")
        self.ModelName=input("Enter Model Name:")
        self.EnergyType=input("Enter Energy Type:")
        self.Price=int(input("Enter Price Of Product: "))

    def TypeData(self):
        print (f"{self.Brand} {self.ModelName} {self.EnergyType} {self.Price}" )

class Refrigerator(HouseholdAppliances):
    Volum=0
    NumberOfCovers=0

    def save(self,list):
        super().save()
        self.Volum=input("Enter Volum:")
        self.NumberOfCovers=int(input("Enter Number Of Doors:"))
        list.append(self)

    def TypeData(self):
        super().TypeData()
        Document.write(f"Product Type\n\n{' ' * 17}Brand Name{' ' * 5}Model Name:{' ' * 5}Price{' ' * 10}Volum{' ' * 10}Number of Covers{' ' * 7}Energy Type\n")
        Document.write(f"Refrigerator: {' ' * 7}{self.Brand}{' ' * 13}{self.ModelName}{' ' * 9}{self.Price}{' ' * 8}{self.Volum}{' ' * 12}{self.NumberOfCovers}{' ' * 18}{self.EnergyType}\n\n")

class WashingMachine(HouseholdAppliances):
    WashingCapacity=0
    SpeedOfWashing=0

    def save(self,list):
        super().save()
        self.WashingCapacity=int(input("Enter Washing Capacity:"))
        self.SpeedOfWashing=int(input("Enter Speed Of Washing:"))
        list.append(self)

    def TypeData(self):
        super().TypeData()
        Document.write(f"                 Brand Nmae{' ' * 5}Model Name{' ' * 5} Price{' ' * 5}WashingCapacity{' ' * 5}SpeedOfWashing{' ' * 9}EnergyType\n")
        Document.write(f"Washing Machine: {self.Brand}{' ' * 11}{self.ModelName}{' ' * 10}{self.Price}{' ' * 11}{self.WashingCapacity}{' ' * 17}{self.SpeedOfWashing}{' ' * 16}{self.EnergyType} ")
        Document.close()
Refrigerators=list()
Ref=Refrigerator()
Ref.save(Refrigerators)
Ref.TypeData()

WashingMachines=list()
Wash=WashingMachine()
Wash.save(WashingMachines)
Wash.TypeData()
'''

'''
import os
if not os.path.exists("C:\\TEST"):
    os.mkdir("C:\\TEST")
from datetime import datetime
today = datetime.now()

d3 = today.strftime("%d-%m-%Y--%H:%M:%S")
print("d3 =", d3)

dosya=open("C:\\TEST\\ask.txt",mode="w")

class Beyaz_Esya:
    Marka=""
    Model=str()
    Enerji=""
    Fiyat=""

    def Kaydet(self):
        self.Marka=input("Marka:")
        self.Model=input("Model:")
        self.Enerji=input("Enerji:")
        self.Fiyat=input("Fiyat:")

    def BilgiYazdir(self):
        print(f"""{self.Marka}
                {self.Model}
                {self.Enerji}
                {self.Fiyat}""")

class Buzdolabi(Beyaz_Esya):
    Hacim=""
    Kapak_Sayisi=""


    def Kaydet(self,liste):
        super().Kaydet()
        self.Hacim=input("Hacim:")
        self.Kapak_Sayisi=int(input("Kapak sayısı:"))
        liste.append(self)

    def BilgiYazdir(self):
        super().BilgiYazdir()
        dosya.write(f"ÜRÜN\nMARKA\nMODEL\nFİYAT\nHACİM\nKAPAK SAYISI\nENERJİ\n")
# print(self.KasaTipi+"\n"+self.VitesTipi)
# dosya.write("Herşeye rağmen adamsın.\n")
        dosya.write(f"BUZDOLABI: {' '*10}{self.Marka}{' ' * 10}{self.Model}{' ' * 10}{self.Fiyat}{' ' * 10}{self.Hacim}{' ' * 10}{self.Kapak_Sayisi}{' ' * 10}{self.Enerji}\n\n")

class Bulasik_Makinesi:
    Yikama_Kapasitesi=""
    Hizli_Yikama=""

    def Kaydet(self,liste):
        super().Kaydet()
        self.Yikama_Kapasitesi=int(input("Yıkama Kapasitesi:"))
        self.Hizli_Yikama=int(input("Hızlı yıkama programı:"))
        liste.append(self)

    def BilgiYazdir(self):
        dosya.write(f"ÜRÜN\nMARKA\nMODEL\nFİYAT\nYIKAMA KAPASİTESİ\nHIZLI YIKAMA\nENERJİ\n")
        dosya.write(f"BULAŞIK MAKİNESİ: {' ' * 10}{self.Marka}{' ' * 10}{self.Model}{' ' * 10}{self.Fiyat}{' ' * 10}{self.Yikama_Kapasitesi}{' ' * 10}{self.Hizli_Yikama}{' ' * 10}{self.Enerji}\n\n")
        dosya.close()

Beyaz_Esya=list()

Buz=Buzdolabi()
Buz.Kaydet(Beyaz_Esya)
Buz.BilgiYazdir()
print(Beyaz_Esya)

Bul=Bulasik_Makinesi()
Bul.Kaydet(Beyaz_Esya)
Bul.BilgiYazdir()
print(Beyaz_Esya)
'''

''' SARVAR
class Beyazesya:
    Marka=""
    Model=""
    Enerji=""
    Fiyat=""
    def Kaydet(self):
        self.Marka=input("Marka giriniz:")
        self.Model=(input("Model giriniz:"))
        self.Enerji=(input("Enerji giriniz:"))
        self.Fiyat=(input("Fiyat giriniz:"))

class Buzdolabi(Beyazesya):
    Hacmi=""
    Kapaksayisi=""
    def Kaydet(self,liste):
        super().Kaydet()
        self.Hacmi=(input("Hacmi giriniz: "))
        self.Kapaksayisi=(input("Kapak Sayısı giriniz: "))
        liste.append(self)
        print(f"""*Buz dolabı özellikleri*
    Marka        : {self.Marka}
    Model        : {self.Model}
    Enerji       : {self.Enerji}
    Fiyat        : {self.Fiyat}
    Hacmi        : {self.Hacmi}
    Kapak sayısı : {self.Kapaksayisi}""")

class CamasirMakinesi(Beyazesya):
    YikamaKapasitesi=""
    YikamaHizi=""
    def Kaydet(self,liste):
        super().Kaydet()
        self.YikamaHizi=(input("Yıkama Hızı giriniz: "))
        self.YikamaKapasitesi=(input("Yıkama Kapasitesi giriniz: "))
        liste.append(self)
        print(f"""*Çamaşır Makinesi özellikleri*
    Marka             : {self.Marka}
    Model             : {self.Model}
    Enerji            : {self.Enerji}
    Fiyat             : {self.Fiyat}
    Yıkama Hızı       : {self.YikamaHizi}
    Yıkama Kapasitesi : {self.YikamaKapasitesi}""")
try:
    secim = int(input("\t**Bir Seçim Yapınız**\n1.Buz Dolabı\n2.Çamaşır Makinesi\n\nSeçiminiz: "))
    if secim == 1:
        BEsyalar1 = list()
        ByzEsy1 = Buzdolabi()
        ByzEsy1.Kaydet(BEsyalar1)
    elif secim == 2:
        BEsyalar2 = list()
        ByzEsy2 = CamasirMakinesi()
        ByzEsy2.Kaydet(BEsyalar2)
except ValueError:
    print("\nLütfen Sayı giriniz!!!\n")
    secim = int(input("\t**Bir Seçim Yapınız**\n1.Buz Dolabı\n2.Çamaşır Makinesi\n\nSeçiminiz: "))
    if secim == 1:
        BEsyalar1 = list()
        ByzEsy1 = Buzdolabi()
        ByzEsy1.Kaydet(BEsyalar1)
    elif secim == 2:
        BEsyalar2 = list()
        ByzEsy2 = CamasirMakinesi()
        ByzEsy2.Kaydet(BEsyalar2)
'''

''' GULU
class beyazEsya:
    def _init_(self,marka,model,enerji,fiyat):
        self.marka=marka
        self.model=model
        self.enerji=enerji
        self.fiyat=fiyat
    def get_info(self):
        print(f"""
        Marka: {self.marka}
        Model: {self.model}
        Enerji: {self.enerji}
        Fiyat: {self.fiyat}""")

class buzdolabi(beyazEsya):
    def _init_(self,marka,model,enerji,fiyat,hacmi,kapaksayisi):
        super(buzdolabi,self)._init_(marka,model,enerji,fiyat)
        self.hacmi=hacmi
        self.kapakSayisi=kapaksayisi
    def get_info(self):
        super().get_info()
        print(f"""
        Hacmi: {self.hacmi}
        Kapak Sayisi: {self.kapakSayisi}""")

class camasirMakinesi(beyazEsya):
    yikamaKapasitesi=None
    hizliYikama=None
    def _init_(self,marka,model,enerji,fiyat,yikamakapasitesi,hizliyikama):
        super(camasirMakinesi, self)._init_(marka,model,enerji,fiyat)
        self.yikamaKapasitesi=yikamakapasitesi
        self.hizliYikama=hizliyikama
    def get_info(self):
        super().get_info()
        print(f"""
        Yikama Kapasitesi: {self.yikamaKapasitesi}
        Hizli Yikama: {self.hizliYikama}""")

print("* Hello *")
while True:
        try:
            k=int(input("\n(1)-Buz Dolabi\n(2)-Camasir Makine: "))
            if k==1:
                s1=input("Marka:").upper()
                s2=input("Modeli:").upper()
                s3=input("Enerji:").upper()
                s4=input("Fiyat:").upper()
                s5=input("Hacmi:").upper()
                s6=input("Kapak Sayisi:").upper()
                buz = buzdolabi(s1,s2,s3,s4,s5,s6)
                buz.get_info()
                print("\nIsleminiz Gerceklesti.")
            elif k==2:
                s1 = input("Marka:").upper()
                s2 = input("Modeli:").upper()
                s3 = input("Enerji:").upper()
                s4 = input("Fiyat:").upper()
                s5 = input("Hacmi:").upper()
                s6 = input("Kapak Sayisi:").upper()
                cam = camasirMakinesi(s1,s2,s3,s4,s5,s6)
                cam.get_info()
                print("\nIsleminiz Gerceklesti.")
            else:
                print("\n** DOGRU SECIM EDINIZ **")
                continue
        except ValueError:
            print("\n** LUTFEN RAKAM KULLANINIZ **")
'''

'''
import os
import datetime

if not os.path.exists("C:\\TEST"):
    os.mkdir("C:\\TEST")

today=datetime.datetime.now()
d = today.strftime("%D.%M.%Y %H:%M:%S")



class beyazEsya:
    Marka=""
    Model=""
    Enerji=""
    Fiyat=""
    ilanTarihi = d

    def Kaydet(self):
        self.Marka=input("Marka:")
        self.Model=input("Model:")
        self.Enerji=input("Enerji:")
        self.Fiyat=input("Fiyat:")
        self.kapakSayisi=input("kapakSayisi:")

    def yazdir(self):
        dosya.write(f"{self.Fiyat}, {self.Enerji}, {self.Model}, {self.Marka}, {self.ilanTarihi}")




class Buzdolabı(beyazEsya):
    Hacim=""
    kapakSayisi=""
    ilanTarihi = d

    def Kaydet(self):
        super().Kaydet()
        self.Hacim=input("Hacim: ")
        self.kapakSayisi = input("Kapak Sayisi: ")

    def yazdir(self):
        Buzdoloabı = open("C:\\TEST\\Buzdolabı.txt", mode="w")
        Buzdoloabı.write(f"Fiyat{' ' * 10} Enerji {' ' * 10}, Kapak Sayisi{' ' * 10} Moderl{' ' * 10} Marka{' ' * 10} Hacim{' ' * 10} İlan Tarihi{' ' * 10} \n\n")
        Buzdoloabı.write(f"{self.Fiyat}, {self.Enerji}, {self.kapakSayisi}, {self.Model}, {self.Marka}, {self.Hacim}, {self.ilanTarihi}")
        Buzdoloabı.close()

class CamasirMak(beyazEsya):
    yikamaKapasitesi =""
    hizliYıkama =""

    def kaydet(self):
        super().Kaydet()
        self.yikamaKapasitesi = input("Yikama Kapasitesi:")
        self.hizliYıkama = input("Kapak Sayisi:")

    def yazdir(self):
        Camasir_Makinesi = open("C:\\TEST\\Camasir Makinesi.txt", mode="w")
        Camasir_Makinesi.write(f"Fiyat{' ' * 10} Enerji {' ' * 10}, Yikama Kapasitesi{' ' * 10} Model{' ' * 10} Marka{' ' * 10} Hizli Yıkama{' ' * 10} İlan Tarihi{' ' * 10}   \n\n")
        Camasir_Makinesi.write(f"{self.Fiyat}, {self.Enerji}, {self.yikamaKapasitesi}, {self.Model}, {self.Marka}, {self.hizliYıkama}, {self.ilanTarihi}")
        Camasir_Makinesi.close()

camasir = CamasirMak()
buzdolabi = Buzdolabı()
buzdolabi.Kaydet()
camasir.yazdir()
buzdolabi.yazdir()










'''

from Buzdolabi import Buzdolabi
b=Buzdolabi()
b.Marka="Arçelik"
b.Model="A123"
b.Fiyat=40000
b.Hacim=500
b.Enerji="A++"
b.KapakSayisi=2

# b.Kaydet()
# b.BilgiListele()

import CamasirMakinesi
c=CamasirMakinesi.CamasirMakinesi()
c.Marka="Arçelik"
c.Model="A123"
c.Fiyat=40000
c.HizliYikama=True
c.Enerji="A++"
c.YikamaKapasitesi=9

# c.Kaydet()
# c.BilgiListele()


def BilgiYazdir(esya):
    esya.BilgiListele()

BilgiYazdir(c)




