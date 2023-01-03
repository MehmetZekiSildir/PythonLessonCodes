"""
i=1
while(i<10):
    print(i)
    i+=1
"""
## Aralık Tanılama
#range default olarak 0'dan başlar ve bitiş değerini dahil etmez.
range(5)    # Bitiş 0,1,2,3,4
range(1,9)  # başlangıç,bitiş 1,2,3,4,5,6,7,8
range(1,9,2)# başlangıç,bitiş,step 1,3,5,7

# for i in range(5):
#     print(i)
#
# for i in range(1,9):
#     print(i)
# #
# for i in range(1,9,2):
#     print(i)
'''
 ilce="Kadıköy"

 for i in ilce:
     print(i)
'''
## ALIŞTIRMALAR ##
## SORU: 1 ile 40 arasındaki sayıları toplayarak ekrana yazdırınız
# toplam=0
# for i in range(1,41):
#     toplam+=i
#
# print("Toplam:",toplam)

## SORU: 20-40 arasındaki çift ve tek sayıları ayrı ayrı toplayarak ekrana yazdırınız.
# tektoplam=0
# cifttoplam=0
# for i in range(20,41):
#     if i%2==0:
#         cifttoplam+=i
#     else:
#         tektoplam+=i
#
# print("Çift toplam=",cifttoplam)
# print("Tek toplam=",tektoplam)


### SORU: 1'den başlayarak kullanıcıdan alınan sayıya kadar olan sayılardan 4'e tam bölünenlerin çarpımını ekrana yazdırınız.

# sayi=int(input('Bir sayi giriniz:'))
# carpim=1
# for i in range(1,sayi+1):
#     if i%4==0:
#         carpim*=i
# print('Carpim=', carpim)


## SORU: Kullanıcıdan alınan sayının rakamları toplamını ekrana yazdırınız
#1234 => 10

# Sayi = input("Bir sayı giriniz: ")
# Toplam = 0
# for rakam in Sayi:
#     Toplam += int(rakam)
#
# print("Sayının rakamları toplamı:", Toplam)

##SORU: aşağıdaki şekilleri for döngüsü ile çizdiriniz
"""
*
**
***
****
*****
******
"""

# for i in range(1,8): #i:1,2,3,4,5,6,7
#     print("*"*i)

"""
******
*****
****
***
**
*
"""
# for i in range(8,0,-1):
#     print("*"*i)

"""
*************
*           *
*           *
*           *
*           *
*           *
*************
"""
# for i in range(1,8):
#     if i==1 or i==7:
#         print("*"*10)
#     else:
#         print("*"+" "*8+"*")
"""
    *
   ***
  *****
 *******
*********

"""

# bosluk=5
# for i in range(1,11,2):
#     print(bosluk*" "+"*"*i)
#     bosluk-=1


##SORU: Çarpım Tablosu Yapınız
"""
1x1=1   2x1=2
1x2=2   2x2=4
...
...
...
"""
# for a in range(1, 11):
#     for b in range(1,11):
#         print(b,"x",a,"=",(a*b),end="\t\t")
#     print()

## SORU: Kullanıcıdan personel sayısını alınız.
# Her personelin kaç çocuğu olduğunu öğreniniz ve çocuk sayısı kadar ekrana "Çocuğunuz adına bir ağaç dikildi." yazdırılsın.
# Program bittiğinde toplam dikilen ağaç sayısı ekrana yazdırılsın.

# toplamAgac=0
# personelSayisi = int(input("Kaç personeliniz vardır?")) #3
# for i in range(1,personelSayisi+1): # 0,1,2 <=> 1,2,3
#     cocukSayisi=int(input(f"{i}. personelin çocuk sayısı:"))
#     for j in range(cocukSayisi):
#         print("Çocuğunuz adına bir ağaç dikildi.")
#     toplamAgac+=cocukSayisi
#
# print("Toplam Ağaç:",toplamAgac)


# import random
# sayi=random.randint(1,100)
#
# print(sayi)

"""ÖDEV SAYI TAHMİN OYUNU
Bilgisayar 1-100 arasında 1 sayı tutsun.
Kullanıcının 5 hakkı olsun ve sayıyı bilmeye çalışsın
Bilirse 'TEBRİKLER'. Bilemezse 'TEKRAR DENEYİNİZ'. Hakkı Biterse 'HAKKINIZ BİTTİ' yazsın.
BONUS: Kullanıcıyı tahmini sonrasında yönlendiriniz.
    Tahmini rastgele değerden büyük ise Tahmini Küçültünüz
    Tahmini rastgele değerden küçük ise Tahmini Büyültünüz
"""
import random
rastgele=random.randint(1,100)
print(rastgele)
# for hak in range(1,6): #hak:1,2,3,4,5
#     tahmin=int(input(f"{hak}. hakkınız:"))
#     if tahmin==rastgele:
#         print("TEBRİKLER")
#         break
#     elif tahmin>rastgele and hak<5:
#         print("Tahmininizi küçültünüz")
#     elif tahmin<rastgele and hak<5:
#         print("Tahmininizi büyültünüz")
#
#     else:
#         print("HAKKINIZ BİTTİ")


# hak=1
# while(hak<6):
#     tahmin = int(input(f"{hak}. hakkınız:"))
#     if tahmin==rastgele:
#         print("TEBRİKLER")
#         break
#     elif tahmin>rastgele and hak<5:
#         print("Tahmininizi küçültünüz")
#     elif tahmin<rastgele and hak<5:
#         print("Tahmininizi büyültünüz")
#
#     else:
#         print("HAKKINIZ BİTTİ")
#     hak+=1














