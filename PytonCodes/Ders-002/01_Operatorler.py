############### OPERATÖRLER #################
from goto import goto
"""
#### ATAMA OPERATÖRÜ (=)
sayi=2


#### ARİTMATİK OPERATÖRLER (+,-,*,/,//,%)
    +,-,* => toplama,çıkarma,çarpma
    /     => ondalıklı bölme
    //    => Tamsayı bölme
    **    => Üs alma
    %     => Mod alma

print(10/3)
print(10/2)

print(10//3)
print(10//2)

print(3**3)

print(10%2)
print(10%3)
print(10%4)


### İŞLEMLİ ATAMA OPERATORLERİ

sayi=5
sayi+=1 # sayi=sayi+1
sayi-=1 # sayi=sayi-1
sayi*=1 # sayi=sayi*1
sayi/=1 # sayi=sayi/1
print(sayi)


#### KARŞILAŞTIRMA OPERATORLERİ
sayi1=4
sayi2=8
print(sayi1==sayi2) # Eşit mi
print(sayi1!=sayi2) # Eşit değiller mi
print(sayi1<=sayi2) # küçük eşit
print(sayi1>=sayi2) # büyük eşit


#### MANTIKSAL OPERATÖRLER

### AND (VE)

0 0 = 0
0 1 = 0
1 0 = 0
1 1 = 1


F F = F
F T = F
T F = F
T T = T

username="altan"
password="123"

kullaniciadi=input("Username")
sifre=input("Password")

girisDurumu=kullaniciadi==username and sifre==password
print(girisDurumu)


### OR (VEYA)

0 0 = 0
0 1 = 1
1 0 = 1
1 1 = 1


username="altan"
email="altan@gmail.com"
password="123"

kullanici=input("Username/Email:")
sifre=input("Password:")

girisDurumu=(kullanici==username or kullanici==email)  and sifre==password
print(girisDurumu)
print()
"""

# sayi=5

# cevap= sayi<9 and sayi>3
# cevap= sayi>4 or sayi<9

# cevap = not sayi==5
# print(cevap)



sayi1=100.0
sayi2=100

# esitKontrol1 = sayi1 == sayi2 # sayısal eşitlik
# esitKontrol2 = sayi1 is sayi2 # yapı eşitliği int==float
# print(esitKontrol1)
# print(esitKontrol2)


# esitKontrol1 = sayi1 != sayi2 # sayısal eşitlik
# esitKontrol2 = sayi1 is not sayi2 # yapı eşitliği int==float
# print(esitKontrol1)
# print(esitKontrol2)


## in keyword

# ilce="KADIKÖY"
# print("ADI" in ilce)
# print("adı" in ilce)
# print("ADI" not in ilce)

username="zeki"
password=123
DON:
kullanici_adi=input("Lütfen kullanıcı adınızı giriniz:").lower()
sifre=int(input("Lütfen şifrenizi giriniz:"))
if (kullanici_adi==username) and (password==sifre):
    print("Giris başarılı!!")
else:
    print("Giriş başarısız:")
    goto DON
















