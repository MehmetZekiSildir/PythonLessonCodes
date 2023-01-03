### KOLEKSİYONLAR ###
"""
List,Tuple,Set,Dict

List: B irden fazladeğeri tutabilen yapılardır.Elemanlarını INDEX adı verilen ve default olarak 0 dan başlayan 1 1 artan bir numaralandırma yöntemi ile tutarlar.
"""

## Boş liste tanımı
# sayilar=[]
# sayilar = list()
# print(type(sayilar))


## Dolu liste tanımı
# sayilar=[11,22,33,44]
# print(sayilar)

## Liste elemanları yazdırma
# print(sayilar[0])
# print(sayilar[1])
# print(sayilar[2])
# print(sayilar[3])
# print(sayilar[4]) # Olmayan Index değerine ulaşma => IndexError: list index out of range


## Listeler karışık veritipinde elemanlar alabilirler.

# karisikListe=[1,"Adana",2,"Adıyaman",34,"İstanbul"]
# print(karisikListe)

## Eleman Sayısı
print(len(karisikListe))

# for i in range(6):
#     print(f"{i}. indexdeki eleman:{karisikListe[i]}")

### SORU: Tanımlı listeden rastgele değer alma
# import random
# index= random.randint(0,len(karisikListe)-1)
# print(karisikListe[index])

## Listeye eleman ekleme
# karisikListe+=[75]
# karisikListe+=["Ardahan"]
#
# karisikListe.append(36)
# karisikListe.append("Kars")

# Çoklu eleman ekleme
# karisikListe+=[75,"Ardahan"]
# karisikListe.append(36,"Kars") ## append() tek eleman alır.
# karisikListe.append([36,"Kars"])
# print(karisikListe)
# print(karisikListe[8][0])
# print(karisikListe[8][1])


## Listeden eleman silme
#değer ile silme
# karisikListe.remove("Adıyaman")
#Index ile silme
# del karisikListe # Ram bellekten tanımı kalıcı olarak siler.
# del karisikListe[3] # Ram bellekten tanımlı index'i kalıcı olarak siler.
# print(karisikListe)


## Listede istenilen index'e eleman ekleme
# karisikListe.insert(3,"Mardin")
# print(karisikListe)


## Elemanın index değerini bulma
sayilar=[11,22,33,11,44,55,11,66,11,77]
# print(sayilar.index(11)) # 11 sayısının ilk indexini verir.
# print(sayilar.index(11,1))
# print(sayilar.index(11,1,4))

## SORU: bütün 11 lerin index değerlerini ekrana yazdırınız

# for index in range(len(sayilar)):
#     if sayilar[index]==11:
#         print(index)

## Listedeki bir elemanın kaç defa yazıldığını bulma

# print(sayilar.count(11))
#
# index=-1
# for i in range(sayilar.count(11)):
#     index = sayilar.index(11,index+1)
#     print(index)

# print(sayilar[len(sayilar)-1])
# print(sayilar[-1])
# print(sayilar[-2])

## Listeyi Sıralama
sehirler=["Mersin","Adana","Malatya","Bursa","Baku","Tahran","Batum","İstanbul","Çanakkale"]
# print(sehirler)
# sehirler.sort() # A->Z 0->9 sıralama yapar.
# sehirler.sort(reverse=True) # Z->A 9->0 sıralama yapar.
# print(sehirler)


## Listeyi Ters Çevirme
# sehirler.reverse()
# print(sehirler)

# if "Adana" in sehirler:
#     print("VAR")

# sayilar=[1,2,3,4,5]
# ## Listeden eleman atma
# # sayi=sayilar.pop() # en son eleman
# sayi=sayilar.pop(2) # 2.indexdeki eleman
# print(sayilar)
# print(sayi)

## Liste Birleştirme

# liste1=[1,2,3]
# liste2=[4,5,6]
# listeler=liste2+liste1
# print(listeler)

## SORU: Aşağıdaki listedeki en büyük ve en küçük değeri hazır bir kod olmadan bulunuz.
"""
sayilar=[12,4,78,4,5,89,-1,-6]
enbuyuk=0
enkucuk=sayilar[0]
for i in sayilar:
    if i<enkucuk:
        enkucuk=i
    if i>enbuyuk:
        enbuyuk=i
print(enkucuk)
print(enbuyuk)

print(max(sayilar))
print(min(sayilar))
print(sum(sayilar))
"""

### Tek satırda for yazma işlemi ###
# rakamlar=list()
#
# for i in range(10):
#     rakamlar.append(i)

# rakamlar=[i for i in range(10)]
# print(rakamlar)

#**********************

# rakamlar=list()
#
# for i in range(10):
#     if i%2==0:
#         rakamlar.append(i)


# rakamlar=[i for i in range(10) if i%2==0]


# rakamlar=[ x if x%2 else x*100 for x in range(1, 10) ]
#
# print(rakamlar)


## Heap Stack Memory - referans tipler
# liste1=[11,22,33]
# # liste2=liste1
#
# liste2=liste1.copy()
# print(liste1)
# print(liste2)
#
#
# liste1.append(44)
# print(liste1)
# print(liste2)

### ALIŞTIRMALAR ###
## SORU 1: 1-50 arasında rastgele 20 adet sayıyı üretip bir listeye atınız.

# import random
# liste=[]
# for i in range(20):
#     sayi=random.randint(1,50)
#     liste+=[sayi]
# print(liste)

## 2: Bu listede aynı sayılar tekrar eklenmesin.
# import random
# liste=[]
# i=0
# while i<20:
#     sayi=random.randint(1,50)
#     if sayi not in liste:
#         liste+=[sayi]
#         i+=1
#
# print(liste)
# print(len(liste))


# import random
# liste=[]
# while len(liste)<20:
#      sayi=random.randint(1,50)
#      if sayi not in liste:
#         liste+=[sayi]
# print(liste)
# print(len(liste))



# import random
# list=[]
# x1=0
# x2=1
# for i in range(50):
#     number = random.randint(1, 50)
#     while j<20:
#         if number in list:
#             continue
#     list+=[number]
#     j+=1
# print(list)


### ÇOK BOYUTLU LİSTELER ###
# cokboyutlu=[[1,2,3],[4,5,6],[7,8,9]] #3 satır 3 sütun matris
"""
    1 2 3  
    4 5 6
    7 8 9
"""
# print(cokboyutlu[0][0])
# print(cokboyutlu[0][1])
# print(cokboyutlu[0][2])
# print(cokboyutlu[1][0])
# print(cokboyutlu[1][1])
# print(cokboyutlu[1][2])
# print(cokboyutlu[1][3]) # list index of range HATASI

# cokBoyutlu2=[0]*5
#
# print(cokBoyutlu2)
#
# for i in range(len(cokBoyutlu2)):
#     cokBoyutlu2[i]=[0]*5
#
# print(cokBoyutlu2)


# cokboyutlu=[[1,2,3],[4,5,6],[7,8,9]]
#
# for satir in cokboyutlu:
#     for sutun in satir:
#         print(sutun,end=" ")
#     print()

"""
SORU: 4x4'lük bir matris içerisinde
    1.satır 1-100 arasında rastgele sayılar ile doldurulsun
    2.satır Kullanıcıdan alınan sayılar ile doldurulsun
    3.satır 1.satırdaki sayıların kareleri ile doldurulsun
    4.satır 2.satırdaki sayıların 5 fazlası ile doldurulsun.
"""

matris=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

import random

for satir in range(4):
    for sutun in range(4):
        if satir==0:
            matris[satir][sutun]=random.randint(1,100)
        if satir==1:
            matris[satir][sutun]=int(input("Sayı:"))
        if satir==2:
            matris[satir][sutun] = matris[0][sutun]**2
        if satir==3:
            matris[satir][sutun] = matris[1][sutun]+5

print(matris)












