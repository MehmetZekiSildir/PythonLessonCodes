######## VERİ TİPLERİ #########
"""
SAYISAL VERİTİPLERİ(INTEGER):
    int: Tamsayıları temsil eder.
        sayi=5
        print(type(sayi))
    float: Ondalıklı sayıları temsil eder.
        sayi=5.6
        print(type(sayi))

SÖZEL VERİTİPİ(STRING): str
    str: Bütün karakterleri tanımlar. Tanımlarken ' veya " tırnak kullanılmalıdır.
        ad="Altan'Kübra"
        ad2='KübraNur'
        print(ad)
        print(ad2)
MANTIKSAL VERİTİPİ(BOOLEAN):
    bool: Sadece True veya False değerleri alır.
        cevap=3>5
        print(cevap)
        print(type(cevap))
"""

# Python'da console ekranına yazdırma komutu PRINT()
# Python'da console ekranından data alma INPUT()
#
# print("Adınız:")
# ad=input("Adınız:")
# print(ad)

# '+' operatörü str+str => birleştirme yapar
# '+' operatörü int+int => toplama yapar
# '+' operatörü str+int => HATA verir.

# ad="Altan"
# soyad="Emre"
# adsoyad=ad+soyad
# print(ad+soyad)
# print(adsoyad)

# sayi=12
# sayi2=15
# print(sayi+sayi2)


# sayi="12"
# sayi2='15'
# print(sayi+sayi2)


# ad="Altan"
# yas=32
# print(ad,yas)


"""
ad="Altan"
ad2="Emre"
soyad="Demirci"
print(ad,ad2,soyad)
## sep: seperator. print içerisndeki elemanlar arasına uygulanacak durumu tanımlar. default olarak sep=" " şeklinde tanımlıdır.
print(ad,ad2,soyad,sep=" ")
print(ad,ad2,soyad,sep="")
print(ad,ad2,soyad,sep="---")
"""

## end operand print komutu bittiğinde gerçekleştirilecek işlemi tanımlar. default olarak end="\n" şeklinde tanımlıdır.
# print("Altan Emre Demirci")
# print("Altan Emre Demirci",end="\n")
# print("Altan Emre Demirci",end="")
# print("Altan Emre Demirci")


### STRING KAÇIŞ KARAKTERLERİ
"""
# \n : alt satıra geçmeyi tanımlar.
# \t : bir tab(4) boşluk vermeyi tanımlar.
# \r : satır başına gitmeyi tanımlar.
# \a : bip sesini tanımlar.
"""

# print("Bugün\nHava\n\tÇok\nGüzel.")

# "=" atama operatörü
# sayi=5
# print(sayi)

# c1=c2=c3=11
# print(c1)
# print(c2)
# print(c3)

# v1,v2,v3=11,12,13
# print(v1)
# print(v2)
# print(v3)




"""
x1=12
x2=34
# yukarıdaki değişken değerleri takas ediniz. NOT: 3. bir değişken kullanmayınız.

x1,x2=x2,x1
print(x1)
print(x2)
"""

## '=='  Eşit mi?

# print(5==5)
# print("altan"=="altan")
# print("altan"=="Altan")

# print(ord('A'))
# print(ord('a'))
# print(ord('1'))
#
# print(chr(65))

# print(5=="5")

### KULLANICI GİRİŞİ ###
"""
username="altanemre"
password="123"

kullaniciadi=input("Username:")
sifre=input("Password:")

girisKontrol=kullaniciadi==username and sifre==password
print("Giriş kontrol:",girisKontrol)
"""


# print("Altan"
#
#
#       "Emre"
#       "Demirci")



# print("""
#             ALTAN
# EMRE
#                     DEMİRCİ""")










