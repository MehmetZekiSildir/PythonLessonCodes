"""
******** FONKSİYONLAR *********
Belirli bir işlem yapan kodların bir blok içerisinde yazılması ve bir ad verilmesiyle ihtiyaç duyulduğu kod satırında bu işlemi gerçekleştirmek için verilen ad ile çağırma işlemi sonucu tanımlı kod bloğunun aktif olarak işlemi gerçekleştirmesini sağlayan yazılım yapısıdır.
Fonskyonlar çağrılmadan çalışmazlar ve çağrılma satırından önce mutlaka tanımlanmalıdırlar.
Fonskyionları () işareti temsil eder.
** Functiın tanımı
def functionName():
    method kod bloğu

** Function Çağırma
functionName()

"""

# def IkiSayiTopla():
#     sayi1=int(input("Sayı1:"))
#     sayi2=int(input("Sayı2:"))
#     toplam=sayi1+sayi2
#     print(toplam)
#
# IkiSayiTopla()

"""
Fonksiyonlar 2'ye ayrılır.
    1-Değer Döndürmeyen(parametreli,parametresiz)
    2-Değer Döndüren(parametreli,parametresiz)
    
** Parametre
    Method tanımlanırken verilen paramtre isimleri çağrılma anında ayrı isimle gönderilmek zorunda değildir.
    Önemli olan kısım tanımda kaç adet parametre olduğu ve veri tipinin ne olduğudur.
"""

### Parametresiz Fonksiyon
# def IkiSayiTopla():
#     sayi1=int(input("Sayı1:"))
#     sayi2=int(input("Sayı2:"))
#     toplam=sayi1+sayi2
#     print(toplam)

### Parametreli Fonksiyon
# def IkiSayiTopla(s1,s2):
#     toplam=s1+s2
#     print(toplam)


# sayi1=int(input("Sayı1:"))
# sayi2=int(input("Sayı2:"))
# IkiSayiTopla(sayi1,sayi2)


"""
ARMSTRONG SAYI:
1634 => 1^4 + 6^4 + 3^4 + 4^4 = 1634 armstrong sayıdır
25 => 2^2 + 5^2 = 29 armstrong sayı


def ArmstrongKontrol(sayi):
    uzunluk=len(sayi)

    toplam=0
    for i in sayi:
        toplam+=int(i)**uzunluk

    if int(sayi)==toplam:
        print("ARMSTRONG SAYIDIR.")
    else:
        print("ARMSTRONG DEĞİLDİR.")

ArmstrongKontrol("1634")
"""

## ALIŞTIRMALAR ##
# SORU: Kullanıcıdan kaç kardeşi olduğunu öğrenip bütün kardeşlerin yaşları toplamını ekrana yazdıran method?

# def kardesYaslari():
#     kardesSayi = int(input("Kardeş Sayısı:"))
#
#     toplam = 0
#     for i in range(kardesSayi):
#         yas = int(input("Yaş:"))
#         toplam += yas
#     print(toplam)

# SORU: Kullanıcıdan 2 sayı 1 işlem alalım ve bu 2 sayıya girilen işlemi uygulayarak sonucu ekrana yazdıran method.
# AliReza
"""
def sum(x, y):
    print(x + y)
def ex(x, y):
    print(x - y)
def mul(x, y):
    print(x * y)
def div(x, y):
    print(x / y)
print("enter the operation.")
print("=======================")
print("1.+")
print("2.-")
print("3.*")
print("4./")
choose= input("pick one (1/2/3/4):")
number1 = int(input("1. no: "))
number2 = int(input("2. no: "))
if choose == '1':
    sum(number1, number2)
elif choose == '2':
    ex(number1, number2)
elif choose == '3':
    mul(number1, number2)
elif choose == '4':
    div(number1, number2)
else:
    print("Wrong select")
"""

# ARAS
"""
def İslem():
    sayi1=int(input('Sayi giriniz:'))
    sayi2=int(input('Sayi giriniz:'))
    islem=input('Toplama, Cıkarma, Carpma, Bolme:').upper()
    if islem=='TOPLAMA':
        print(sayi1+sayi2)
    elif islem=='CIKARMA':
        print(sayi1-sayi2)
    elif islem=='CARPMA':
        print(sayi1*sayi2)
    elif islem=='BOLME':
        print(sayi1/sayi2)

İslem()
"""
#
# def DortIslem(s1,s2,islem):
#     if islem=="+":
#         print(s1+s2)
#     elif islem=="-":
#         print(s1-s2)
#     elif islem=="*":
#         print(s1*s2)
#     elif islem=="/":
#         if s2==0:
#             print("Sıfıra Bölme Hatası")
#         else:
#             print(s1/s2)
#
# sayi1=float(input("Sayı 1:"))
# sayi2=float(input("Sayı 2:"))
# operator=input("İşlem Seçiniz(+,-,*,/):")
# DortIslem(sayi1,sayi2,operator)


# SORU: Parametre olarak verilen bir sayi listesindeki tek sayıları ekrana yazdıran method?

#ALİREZA

# def odd_number(list):
#     for i in list:
#         if i%2!=0:
#             print(i)
#
# list=[1,2,3,4,5,6]
# odd_number(list)

"""
def TekSayilar(list):
    for sayi in list:
        if type(sayi)==str and sayi.isdigit():
            sayi=int(sayi)
        if type(sayi)==int or type(sayi)==float:
            if sayi%2!=0:
                print(sayi)

liste=[11,2,"Altan",3,45.7,True,45,"23",65,76]
TekSayilar(liste)
"""


### Belirsiz Sayıda Parametre Alan Method

# def Topla(s1,s2):
#     print(s1+s2)
#
# def Topla3(s1,s2,s3):
#     print(s1+s2+s3)
#
# def Topla4(s1,s2,s3,s4):
#     print(s1+s2+s3+s4)
"""
def Topla(*sayi):
    print(type(sayi))
    toplam=0
    for i in sayi:
        toplam+=i
    print(toplam)

Topla(1,2)
Topla(1,2,3)
Topla(1,2,3,4)
Topla(1,2,3,4,5)
"""

# SORU: Kendisine gönderilen karakter,en ve boy parametrelerine göre ekrana karakterden belirtilen en ve boya göre geometrik şekil çizen method
"""
*,4,5
"""

# def Ciz(karakter,en,boy):
#     for i in range(boy):
#         print(karakter*en)
#
# Ciz("o",4,5)


### GLOBAL KEYWORD
"""
def Degistir():
    global sayi1,sayi2
    sayi1,sayi2=10,20
    # print(sayi1)
    # print(sayi2)

sayi1,sayi2=100,200

Degistir()

print(sayi1)
print(sayi2)
"""

## DEĞER DÖNDÜREN FONKSİYONLAR ##
# değer döndürme keyword'ü 'return' komutudur.
"""
def Topla(s1,s2):
    print(s1+s2)

def Topla2(s1,s2):
    return s1+s2

# Topla(11,22)
# print(Topla2(11,22))
sonuc=Topla2(12,13) # sonuc=25
print(sonuc)
"""
"""
kare = pow(4,2)
print(kare)

def kuvvet(taban,us):
    return taban**us

karesi=kuvvet(4,2)
print(karesi)
"""

## ÖDEV: Bir müşteri döviz bürosuna gidip dolarını euro ya çevirmek istiyor. Çalışan kişi dolar/euro endeksini bilmediği için önce doları liraya çeviriyor sonra lirayı euro ya çevirerek bu işi yapıyor.

### FURKAN GENÇ ###
# def change(para):
#     lira_dolar  = 15.90
#     lira_euro = 16.79
#
#     cevir = para * lira_dolar
#     sonuc = cevir / lira_euro
#     print("%.3f" % sonuc,"€ vardır.")
# para = float(input("Kaç dolarınızı Euro'ya çevirmek istiyorsunuz: "))
# change(para)


# def DolarToLira(dolar):
#     lira=dolar*15.87
#     return lira # return dolar*15.87
#
# def LiraToEuro(lira):
#     euro=lira/16.75
#     print(euro)
#
#
# para=int(input("Kaç Dolar Euro Çevrimi Yapılacak?"))
# lira=DolarToLira(para)
# LiraToEuro(lira)


## Kendisine gönderilen 4 sınıfa ait not listelerinin ortalamalarını bularak kıyaslayan ve en başarılı sınıfı ile ne başarısız sınıfı ekrana yazdıran method.

### FURKAN GENÇ ###

"""
def hesaplayici(a,b,c,d):
    ortalamalar = {}
    toplam = 0    
    
    for i in a:
        toplam += i
    ort = toplam / len(a)
    ortalamalar["Sınıf1"] = ort
    toplam = 0
    for i in b:
        toplam += i
    ort = toplam / len(b)
    ortalamalar["Sınıf2"] = ort
    toplam = 0
    for i in c:
        toplam += i
    ort = toplam / len(c)
    ortalamalar["Sınıf3"] = ort
    toplam = 0
    for i in d:
        toplam += i
    ort = toplam / len(d)
    ortalamalar["Sınıf4"] = ort
        

    en_iyi = ortalamalar[max(ortalamalar)]
    en_dusuk = ortalamalar[min(ortalamalar)]
    print(f"En başarılı sınıf " "%.2f" % en_iyi,  f"ile {max(ortalamalar)}")
    print(f"En başarısız sınıf " "%.2f" % en_dusuk,  f"ile {min(ortalamalar)}")


sinif1 = [50,60,70,80,90,55,71,26]
sinif2 = [53,60,90,83,90,]
sinif3 = [58,60,90,10,98,100,77,46,83,45]
sinif4 = [91,73,88,15,30,21]

hesaplayici(sinif1,sinif2,sinif3,sinif4)
"""
"""
def Hesapla(*sinif):
    ortalama={}
    key="Sinif"
    i=1
    for s in sinif:
        ortalama[key+str(i)]= sum(s)/len(s)
        i+=1
    # ortalama[key+str(i)]=[sum(s)/len(s) for s in sinif]
    print(ortalama)
    # region I.YOL
    # enYuksek=max(ortalama.values())
    # enDusuk=min(ortalama.values())
    # for item in ortalama:
    #     if ortalama[item]==enYuksek:
    #         print(f"EN BAŞARILI: {item}:{enYuksek}")
    #     elif ortalama[item]==enDusuk:
    #         print(f"EN BAŞARISIZ: {item}:{enDusuk}")
    #endregion
    # maxkey=max(ortalama,key=ortalama.get)
    # print(f"{maxkey}: {ortalama[maxkey]}")
    print(f"{max(ortalama,key=ortalama.get)}: {ortalama[max(ortalama,key=ortalama.get)]}")
    print(f"{min(ortalama,key=ortalama.get)}: {ortalama[min(ortalama,key=ortalama.get)]}")

sinif1 = [50,60,70,80,90,55,71,26]
sinif2 = [53,60,90,83,90,]
sinif3 = [58,60,90,10,98,100,77,46,83,45]
sinif4 = [91,73,88,15,30,21]

Hesapla(sinif1,sinif2,sinif3,sinif4)

"""


### Bir fonksiyon içinde fonksiyon çağrılması ###

# def Buyuk2(x,y):
#     if x>y:
#         return x
#     return y
#
# def Buyuk3(a,b,c):
#     return Buyuk2(a,Buyuk2(b,c))
#
# print(Buyuk3(11,2,3))

### Recursive Method ###

"""
def Yaz():
   global i
   print(i)
   i+=1
   if i<9:
       Yaz()

i=1

Yaz()
"""

### TEK SATIRDA FONKSİYON TANIMLAMA ###

# def kare(s):
#     return s*s
#
# print(kare(4))

# kare = lambda s:s*s
# print(kare(4))


# topla=lambda x,y,z: x+y+z
#
# print(topla(1,2,3))


### SORU:Kendi isminiz ile bir modül oluşturunuz.
# Modül içerisnde bir sansur(cumlelistesi,yasaklıkelime,yenikelime) isminde bir metot oluşturun
# Bu metot kendisine gönderilen cümle listesindeki yasaklı kelimeyi yeni kelimeyle sansürlesin
# sansur("Çocuklar kahve içerse kararır.","kahve","k")


# from sansur import Sansur
#
# cumleListesi=["Çocuklar kahve içerse kararır.","Çocuklar Kahve sade içilir.","Insanlar KAHVE olamdan uyanamaz."]
#
# yeniCumleListesi=Sansur(cumleListesi,"kahve","k")
#
# print(yeniCumleListesi)

### ÖDEV:
"""
# Kullanıcıdan 2 tane değer alan DegerleriAl() fonk. vardır. eger bu degerleri sayi degerleri döndürür, herhangi biri sayı değilse False döndürür.

-ObebHesapla(s1,s2) -> gelen bu iki sayının obeb degerlerini hesaplar ve geri döndürür.
-OkekHesapla(obeb) -> s1*s2=obeb*okek formulunden okek bulunur ve okek obeb yazdırılır.
"""

def DegerAl():
    sayi1=input("1.Sayı:")
    sayi2=input("2.Sayı:")

    if sayi1.isdigit() and sayi2.isdigit():
        return int(sayi1),int(sayi2)
    return False

def ObebHesapla(s1,s2):
    obeb=1
    for i in range(2,min(s1,s2)+1):
        if s1%i==0 and s2%i==0:
            obeb=i
    return obeb

def OkekHesapla(obeb):
    okek=int(donen[0]*donen[1]/obeb)
    print("OKEK: {}\nOBEB: {}".format(okek,obeb))


donen=DegerAl()

if not donen==False:
    OkekHesapla(ObebHesapla(donen[0],donen[1]))

else:
    print("Hatalı Giriş")

### FURKAN GENÇ ###


# def ebob(a, b):
#     liste1 = [a, b]
#     cevap = 0
#     for i in range(1, max(liste1) + 1):
#         if a % i == 0 and b % i == 0:
#             cevap = i
#     return cevap
#
#
#
# def ekok(x,y):
#     global ebob_cevabi
#     islem1 = x * y
#     ekok_cevabi = islem1 / ebob_cevabi
#     return  ekok_cevabi
#
#
# sayi1 = int(input("1. Sayi: "))
# sayi2 = int(input("2. Sayi: "))
# ebob_cevabi = ebob(sayi1,sayi2)
# ekok_cevabi = ekok(sayi1,sayi2)
#
# print(f"Ebob: {ebob_cevabi}, \nEkok: {ekok_cevabi}")




# def DegerleriAl(a,b):
#     kontrol1 = str(a)
#     kontrol2 = str(b)
#     if kontrol1.isdigit() == True and kontrol2.isdigit() == True:
#         print("Bütün karakterler sayıdır.")
#     else:
#         print("Bütün karakterler sayı değildir.")
#
# DegerleriAl("sdfdsf",20)

## DEGERCAN ###

# def compute_lcm(x, y):
#
#    # choose the greater number
#    if x > y:
#        greater = x
#    else:
#        greater = y
#
#    while(True):
#        if((greater % x == 0) and (greater % y == 0)):
#            lcm = greater
#            break
#        greater += 1
#
#    return lcm
#
# num1 = 22
# num2 = 33
#
# def compute_hcf(x, y):
#
# # choose the smaller number
#
#     for i in range(1, min(x,y)+1):
#         if((x % i == 0) and (y % i == 0)):
#             hcf = i
#     return hcf
#
# num1 = 24
# num2 = 12

### GULU ###
# def DegerleriAl(s1,s2):
#     a,b,=s1,s2
#     while a!=b:
#         if a>b: a-=b
#         else: b-=a
#     print("EBOB=",a,"\nEKOK=",s1*s2//a)
# DegerleriAl(7,36)







