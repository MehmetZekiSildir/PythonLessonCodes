############ KARAR YAPIlaRI IF-ELIF-ELSE #############
"""
Program akışında bir duruma göre karar verilmesi ve kodların bu karara göre devam etmesi için IF ELSE yapısı kullanılır.
ilk durum IF bloğuyla kontrol edilir ve bir defa yazılır. alternatif durumlar için elif bloğu kullanılır.

if koşul1:
    koşul1 doğru(true) ise bu kod bloğu çalışır.
elif koşul2:
    koşul1 doğru(true) ise bu kod bloğu çalışır.
elif koşul3:
    koşul3 doğru(true) ise bu kod bloğu çalışır.
elif koşul4:
    koşul4 doğru(true) ise bu kod bloğu çalışır.
else:
    if ve elif lerin koşuılları sağlanmasdığı durumlarda geriye kalan diğer durumlar için else çalışır. Bu sebeple else ye KOŞUL YAZILMAZ
"""


## SORU: kullanıcıdan alınan sayının pozitif, negatif olma durumunu ekrana yazdırınız.

# sayi=int(input("Sayı:"))
# if sayi>0:
#    print("Pozitif")
# elif sayi==0:
#     print("Sıfır")
# else:
#     print("Negatif")


####SORU: Kullanıcıdan 1-7 arasında bir gün bilgisi girmesini isteyiniz ve girilen sayıya göre gün adını ekrana yazdırınız

# gun=int(input("1-7 arasında bir sayı giriniz:"))
# if gun>0 and gun<8:
#     if gun == 1:
#         print("pazartesi")
#     elif gun == 2:
#         print("salı")
#     elif gun == 3:
#         print("çarşamba")
#     elif gun == 4:
#         print("perşembe")
#     elif gun == 5:
#         print("cuma")
#     elif gun == 6:
#         print("cumartei")
#     else:
#         print("pazar")
# else:
#     print("Hatalı Gün bilgisi!!!")


#region ARAS
"""
sayi=int(input('1 den 7 ye kadar bir sayi girin:')) #1 den 7 ye kadar bir sayi girin:99999
if sayi==1:
    print('Pazartesi')
elif sayi==2:
    print('Salı')
elif sayi==3:
    print('Carsamba')
elif sayi==4:
    print('Persembe')
elif sayi==5:
    print('Cuma')
elif sayi==6:
    print('Cumartesi')
else: 
    print('Pazar')
"""
#endregion

#region SULTAN

# gun=int(input("1-7 arasında bir sayı giriniz:"))
# if gun==1:
#     print("pazartesi")
# elif gun==2:
#     print("salı")
# elif gun == 3:
#     print("çarşamba")
# elif gun == 4:
#     print("perşembe")
# elif gun == 5:
#     print("cuma")
# elif gun == 6:
#     print("cumartei")
# elif gun == 7:
#     print("pazar")
# else:
#     print("hatalı sayı")

#endregion

### SORU: kullanıcıdan alınan sayı 100'den büyük ise karesini, 100 küçük ise küüpünü alarak ekrana yazdırınız.

# user = int(input("Choose a number"))
# if user > 100:
#     print(user**2)
# elif user < 100:
#     print(user**3)
# else:
#     print("Number:",100)


## MOD ALMA
# sayi=5
# print(sayi%2==0)

### Kullanıcıdan sayının çift mi tek mi olduğu ekrana yazdırınız.
# sayi=int(input("sayı girin"))
# if sayi%2==0:
#     print("Çifttir")
# else:
#     print("Tektir")



###ÖRNEK: Aralık tanımlama
# sayi=int(input("Sayı Giriniz"))
#
# if(sayi>0 and sayi<11):
#     print("1-10 aralığında")
# elif(10<sayi<21):   #(sayi>10 and sayi<21):
#     print("11-20 aralığında")
# elif(21<=sayi<=30):
#     print("21-30 aralığında")


### ÖRNEK: Klavyeden girilen 4 sayıdan tekleri ayrı, çiftleri ayrı toplayarak ekrana toplamları yazdırınız
"""
cifttoplam=0
tektoplam=0

sayi1=int(input("1.sayı")) #4
if sayi1%2==0:
    # cifttoplam=cifttoplam+sayi1
    cifttoplam+=sayi1
else:
    tektoplam=tektoplam+sayi1

sayi2=int(input("2.sayı")) #6
if sayi2%2==0:
    cifttoplam=cifttoplam+sayi2
else:
    tektoplam=tektoplam+sayi2

sayi3=int(input("3.sayı"))
if sayi3%2==0:
    cifttoplam=cifttoplam+sayi3
else:
    tektoplam=tektoplam+sayi3

sayi4=int(input("4.sayı"))
if sayi4%2==0:
    cifttoplam=cifttoplam+sayi4
else:
    tektoplam=tektoplam+sayi4

print("tekler:",tektoplam)
print("çiftler:",cifttoplam)
"""
### Öğrencinin vize ve final notlarını alınız ve ortalamasına göre harf notu veriniz
# (vize+final)/2
# 0-24  : FF
# 25-44 : DD
# 45-54 : CC
# 55-69 : CB
# 70-84 : BB
# 85-100: AA
##*** Not aralığı kontrolü yapılacak vize ve final 0-100 aralığında olmalıdır.
"""
vize = int(input("Vize Notunu Giriniz"))
if 0<=vize<101:
    final = int(input("final notunu giriniz"))
    if 0<=final<101:
        ort = ((vize + final) / 2)
        if (0<=ort<=24):
            print("FF")
        elif (25<=ort<=44):
            print("DD")
        elif (45<=ort<=54):
            print("CC")
        elif (55<=ort<=69):
            print("CB")
        elif (70<=ort<=84):
            print("BB")
        else:
            print("AA")
    else:
        print("0-100 arasında giriniz")
else:
    print("0-100 arasında giriniz")
"""

### SORU: Kullancıdan isim,yaş,çocuksayisi ve maaş bilgilerini alalım.
"""
    Eğer kullanıcının yaşı 45'in altındaysa
        çocuksayısına bakılacak ve çocuk sayısı 3'den az ise çocuk başına 250 ₺,
                                                        değilse çocuk başına 200₺ maaşa eklenecek
    Eğer kullanıcının yaşı 45 ve üzerinde ise
        çocuk başına para verilmeyecek direk 500₺ maaşına eklenecek
        
    Ekrana "Altan Emre Maaş:5000₺" yazılacak 
"""
# isim=input("İsim:")
# cocuksayisi=int(input("Kaç çocuğunuz var?"))
# yas=int(input("Yaşınız kaç?"))
# maas=int(input("Maaşınız ne kadar?"))
#
# if yas<45:
#     if cocuksayisi<3:
#         maas+=cocuksayisi*250
#     else:
#         maas+=cocuksayisi*200
# else:
#     maas+=500
#
# print(f"{isim} Maas:{maas}")



### ÖDEV:
"""

## SORU:# // kullanıcıdan aylık gelirini isteyin.
#            // Aylık geliri 4000 üstünde 
                    ise %12 vergi kesilecek,
#            // 4000 ve altında 
                    ise %9 vergi kesimi yapılarak
#            // kullanıcıya yeni gelirini bu hesaplamalar sonucunda gösteriniz

"""

gelir=float(input("Aylık Geliriniz:"))
if gelir>4000:
    gelir= gelir-((gelir/100)*12)
    gelir=gelir*0.88

else:
    # gelir*=0.91
    gelir*=.91

print("Geliriniz:",gelir)
print(f"Geliriniz: {gelir}")
print("Geliriniz: {}".format(gelir))




"""
### SORU:
   kullanıcıdan alınan cinsiyet bilgisine göre
             ==>ERKEK ise
                yaşı 60 ve üstü ise maaşının 10 katı kadar ikramiye alaral emekli edilecek, 
                yaş 60'ın altında ise çalıştığı gün sayısına göre 
                    eğer 6000 ve üstü ise maaşının 11 katı kadar ikramiye alarak emekli edilecek,    
                    6000 altında ise emekli edilmeyecek bilgisi kullanıcıya gösterilecek
            ==> KADIN ise   
                 yaşı 58 ve üstü ise maaşının 10 katı kadar ikramiye alarak emekli edilecek, 
                 yaş 58'ın altında ise çalıştığı gün sayısına göre 
                    eğer 5600 ve üstü ise maaşının 11 katı kadar ikramiye alarak emekli edilecek, 
                    5600 altında ise emekli edilmeyecek bilgisi kullanıcıya gösterilecek
                 ==> cinsiyet bilgisi kontrol ile sorgulanacak
"""
"""
cinsiyet=input("Cinsiyetiniz:").upper() #alınan str değeri büyük harfe çevirir. #lower() alınan str değeri küçük harfe çevirir.

if cinsiyet=="ERKEK":
    yas=int(input("Yaş:"))
    maas=float(input("Maaş:"))
    if yas>=60:
        print("İkramiyeniz:",maas*10)
    else:
        primgunu=int(input("Prim Gün Sayısı:"))
        if primgunu>=6000:
            print("İkramiyeniz:",maas*11)
        else:
            print("Emeklilik Hayal... Çalışmaya Devam!!")

elif cinsiyet=="KADIN":
    yas=int(input("Yaş:"))
    maas=float(input("Maaş:"))
    if yas>57:
        print("İkramiyaniz:",maas*10)
    else:
        primgunu=int(input("Prim gun Sayısı:"))
        if primgunu>=5600:
            print("İkramiyeniz:",maas*11)
        else:
            print("Emeklilik Hayal.. Çalışmaya devam!!")

else:
    print("Hatalı Bilgi!!!")

"""

# try:
#     #Kontrol edilecek kod bloğu
#     yas=int(input("Yaş:"))
# except:
#     print("Yaşı rakam olarak giriniz!!")












