### DÖNGÜLER - LOOPS ###

"""
Tekrar eden işlemler için tekrar tekrar kod yazmaktan bizi kurtaran yapılardır. Kendisine belirtilen tur sayısı kadar tekrar tekrar çalışan ve içindeki kod bloğunu çalıştıran yapılardır.

WHILE DONGUSU - FOR DONGUSU
"""
# 1-10 arasındaki sayıları ekrana yazdırnız
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)
# print(7)
# print(8)
# print(9)
# print(10)

# i=1
# while i<11: # while kendisine verilen koşul TRUE olduğu sürece çalışır. 1,2,3,4,5,6,7,8,9,10
#     print(i)
#     i += 1

## SORU: 90-100 arasındaki sayıları ekrana yazdırınız.

# i = 90
# while i <101:
#     print(i)
#     i+=1

## SORU: 70 - 55 arasındaki sayılarda 3'e tam bölünen sayıları ekrana yazdırınız.

# a=70
# while a>55:
#     if a%3==0:
#         print(a)
#     a-=1

## SORU: Kullanıcıdan 4 adet sayı alıp toplamlarını ekrana yazdırınız

# toplam=0
# i=1
# while i<5:
#     sayi=int(input("Sayı:"))
#     toplam+=sayi # toplam= toplam+sayi
#     i+=1
#
# print(toplam)

## SORU: 7 - 77 arasındaki bütün sayıları toplamını ekrana yazdıran döngü
#
# toplam= 0
# i=7
# while i<77:
#     toplam+=i
#     i+=1
# print(toplam)

## SORU: Başlangıç ve bitiş değerini kullanıcıdan alalım ve aralıktaki tek sayıların karesi ekrana yazdırınız.

# basla=int(input('Baslangic sayisini giriniz:')) # 5
# bitis=int(input('Bitis sayisini giriniz:')) # 10
# if basla>bitis:
#     basla,bitis = bitis,basla
#
# while basla<=bitis: #5<=10
#      if basla%2==1: # Tek sayı kontrolü
#          print(basla**2)
#      basla+=1


## SORU:Klavyeden girilen sayının faktöriyelini hesaplayan döngü
# faktöriyel 5 => 5*4*3*2*1= 120

# sayi=int(input("Sayı Giriniz:"))
# faktoriyel=1
# while sayi>0:
#     faktoriyel*=sayi
#     sayi-=1
#
# print(faktoriyel)


### Kullanıcıdan bir sayı alınız alınan sayının asal olup olmadığını ekrana yazdırınız.
# asal sayı: kendisinden ve 1 den başka sayıya bölünmeyen sayı demektir. 2,3,5,7,11,13,...
# sayi=int(input("Kontrol edilecek sayı:")) #7
# asalMi=True
#
# bolen=2
# while bolen<sayi: #sayı:8 ise 2,3,4,5,6,7 bölünme kontrolü
#     if sayi%bolen==0:
#         asalMi=False
#         break
#     bolen+=1
#
# if asalMi:
#     print("Sayı asaldır")
#
# else:
#     print("Sayı asal Değildir.")



### SORU:1-1000 arasındaki asal sayıları ekrana yazdırınız.

# i=2
# while i<1000:
#     sayi = i
#     asalMi=True
#
#     bolen=2
#     while bolen<sayi: #sayı:8 ise 2,3,4,5,6,7 bölünme kontrolü
#         if sayi%bolen==0:
#             asalMi=False
#             break
#         bolen+=1
#
#     if asalMi:
#         print(sayi)
#     i+=1


# def prime(n):
#     asal = True
#     for i in range(2,n):
#         if n%i == 0:
#             asal = False
#     if asal:
#         return n
#
# for x in range(2,201):
#     if prime(x):
#         print (x)


### SORU:Kullanıcıdan 0 sayıyı alınana kadar girilen bütün sayıları toplayınız ve 0 sayıyı girildiğinde döngü bitsin toplam ekrana yazdırılsın.
# sum=0
# while True:
#     sayi = int(input("Bir sayı giriniz:"))
#     if sayi==0:
#         break
#     sum+=sayi
#
# print("Toplam:",sum)


## 2.Yöntem
# toplam=0
# sayi=int(input("Sayı:"))
# while sayi!=0:
#     toplam+=sayi
#     sayi = int(input("Sayı:"))
#
# print("Toplam:",toplam)


### 1-10 kadar sayılar ekrana yazdırılırken 3 sayıyı atlansın ve 7 sayısında döngü bitsin

# i=1
# while i<11:
#     if i==3:
#         i+=1
#         continue # program bu komutu gördüğünde bulunduğu satırdan döngü koşul satırına döner.
#     if i==7:
#         break
#     print(i)
#     i+=1

### SORU: Klavyeden girilen  deger 'cik' ise döngüden çıkılsın değilse girilen değerin sayı olduğu düşünülerek toplama yapılsın.
# kullanıcı cik yazdığında ekrana toplam yazılsın.
# toplam=0
# while True:
#     sayi=input("Sayı giriniz:")
#     if sayi=="cik":
#         break
#     else:
#         toplam= toplam + int(sayi)
#
# print(f"Toplam:{toplam}")
# print("Toplam:{}".format(toplam))
# print("Toplam:",toplam)

### SORU: 1-100 arasıdaki sayıların toplayan program. Ancak aşağıdaki durumlarda sayıyı toplama dahil etmesin.
# * Sayı 7'nin katı ise toplama eklenmesin
# * Sayı'nın 3 katının 7 fazlası 37'nin katı ise döngüden çıkılsın.

# sayi=1
# toplam=0
# while sayi<100:
#     kat=(3*sayi)+7
#     if kat%37==0:
#         break
#     if sayi%7!=0:
#        toplam+=sayi
#     sayi+=1
# print(toplam)










