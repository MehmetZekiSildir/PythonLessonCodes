########## DİZİN İŞLEMLERİ ##########

# dizin=r"C:\Users\altan\PycharmProjects\PYTHONSALI\Ders-008"
# dizin="C:\\Users\\altan\\PycharmProjects\\PYTHONSALI\\Ders-008"
# dizin2="C:\\\\Users\\\\altan\\\\PycharmProjects\\\\PYTHONSALI\\\\Ders-008"
# print(dizin2)

"""
open()      => dosya açma komutu
system()    => system32 komutları yazılır.
getcwd()    => Sistemin şuan işlem yaptığı dizin döndürülür.
chdir()     => Farklı bir dizine geçmemizi sağlar.
listdir()   => Bulunduğumuz dizinde mevcut dosyaları getirir.
mkdir()     => Bulunduğumuz dizinde yeni klasör açar.
rmdir()     => İçi boş olan bir klasörü siler.
rename()    => İsim değiştirir
path()      => Bir dosya veya klasörün var olup olmadığını kontrol etmek istediğimizde path.exists() komutu kullanırız.
"""

# import os
# os.system("calc")
# os.system("ipconfig")
# os.system("hostname")

# print(os.getcwd())
# os.chdir("C:\\")
# print(os.getcwd())
# print(os.listdir())

# import os
# if not os.path.exists("C:\\TEST"):
#     os.mkdir("C:\\TEST")

###SORU: C:\TEST\YIL-AY-GUN isminde bir klasör oluşturunuz
# import os, datetime
# datestring = datetime.datetime.now().strftime("%Y-%m-%d")
# # print(datestring)
# if not os.path.exists("C:\\TEST"):
#     os.mkdir("C:\\TEST")
#     if not os.path.exists(f"C:\\TEST\\{datestring}"):
#         os.mkdir(f"C:\\TEST\\{datestring}")


#### DOSYA İŞLEMLERİ ####
"""
Yetki Modları
w  : sadece yazma yetkisi verir.(dosya yoksa oluşturur.Eğer varsa dosyayı siler yeniden oluşturur.)
a  : sona ekleme yetkisi verir.(dosya yoksa oluşturur. Varsa sonuna ekleme yapar.)
r  : sadece okuma yetkisi verir.
x  : sadece yazma yetkisi verir.(dosya yoksa oluşturur.Varsa hata verir.)

w+ : yazma + okuma yetkisi verir.(dosya yoksa oluşturur. Varsa siler yeniden oluşturur.)
r+ : okuma + yazma yetkisi verir.
a+ : ekleme + okuma yetkisi verir. (dosya yoksa oluşturur.)
"""

# dosya=open("C:\\TEST\\ask.txt",mode="w")
# dosya.write("Herşeye rağmen adamsın.")


# dosya=open("C:\\TEST\\ask.txt",mode="a")
# dosya.write("Herşeye rağmen adamsın.\n")


### SORU: 1 - 10 sayıların karelerini kare.txt isimli bir dosyaya aşağıdaki formatla yazdırınız.
"""
    1 sayısının karesi: 1
    2 sayısının karesi: 2
    3 sayısının karesi: 3
    4 sayısının karesi: 4
    ......
    
"""

# dosya=open("C:\\TEST\\kare.txt","w")
# for i in range(1,11):
#     dosya.write(f"{i} sayısının karesi:{i*i}\n")
#
# dosya.close()


### ÖDEV: 1-100 arası üretilen 10 adet rastgele sayıyı Rastgele.txt isimli dosyaya aşağıdaki formatla yazdırınız.
"""
    ZAMAN                       OLAYSIRASI          RASTGELESAYI
    25.05.2020 21:38:35.213         1                    23
    25.05.2020 21:38:35.213         2                    34
    25.05.2020 21:38:35.213         3                    2
    25.05.2020 21:38:35.213         4                    65
    25.05.2020 21:38:35.213         5                    87
    ...........
    ...........
    ...........
"""
"""
import os
import random
import datetime

if not os.path.exists("C:\TEST"): #Dosyayı oluşturdum.
    os.mkdir("C:\TEST")

today = datetime.datetime.now()
d3 = today.strftime("%d.%m.%Y %H:%M:%S") #Zamanı belirledim.

dosya=open("C:\TEST\Rastgele.txt",mode="w") #Dosyayı açtım.
dosya.write(f"ZAMAN {' ' * 23}OLAY SIRASI {' ' * 10}RASTGELE SAYI\n")# Başlıkları ekledim.
dosya.write(f"{'-' * 5}{' ' * 24}{'-' * 11}{' ' * 11}{'-' * 13}\n\n")#Başlıklar daha belirgin olsun fiye altına çizgi ekledim.

#
for i in range(1,11): #Başlıkların altını doldurdum.
    sayi = random.randint(0, 100)
    if i == 10:
        dosya.write(f"{d3} {' ' * 13}{i} {' ' * 19} {sayi}\n")
    else:
        dosya.write(f"{d3} {' ' * 13}{i} {' ' * 20} {sayi}\n")
"""

### DOSYA OKUMA İŞLEMLERİ ###
# dizin="C:\\TEST\\"
# dosya=open(dizin+"personeller.txt","r",encoding="utf8")

##### readline() : Satır satır okuma #####

# print(dosya.readline(),end="")
# print(dosya.readline(),end="")
# print(dosya.readline(),end="")
# print(dosya.readline(),end="")
# print(dosya.readline(),end="") # okunacak satır kalmadığında boş satır getirir.


### Dosyayı 2 tur okuma  seek() ##

# print(dosya.readline(),end="")
# print(dosya.readline(),end="")
# print(dosya.readline(),end="")
# print(dosya.readline(),end="")
# print(dosya.readline(),end="")
# dosya.seek(0)
# print(dosya.readline())
# print(dosya.readline())
# print(dosya.readline())

# OKUYACAĞI SATIRDAN kaç karakter okunmasını istediğimizi belirtiyoruz.
# print(dosya.readline(80))


##### readlines(): Dosyayı bir liste halinde döndürür. #####
# dokuman=dosya.readlines()
# print(dokuman)
# for i in dokuman:
#     print(i,end="")
# yeniDokuman=[]
# for satir in dokuman:
#     # yeniDokuman.append(satir.replace("\n",""))
#     # yeniDokuman.append(satir.strip("\n"))
#     yeniDokuman.append(satir.rstrip("\n"))
#
# print(yeniDokuman)


##### read(): verilen karakter sayısı kadar okuma yapar. #####

# print(dosya.read())
# print(dosya.read(34))

# print(type(dosya.read()))

#SORU: Bir sayiListe.txt isimli dosyadan sayıları okuyarak teklerin 3. kuvvetini, çiftlerin karesini kareListe.txt isimli dosyaya yazdırınız.
"""
sayilar=open("C:\\TEST\\sayiListesi.txt","r").readlines()
sayilar=[int(i.strip("\n")) for i in sayilar]
print(sayilar)
dosya=open("C:\\TEST\\sayiListesi.txt","a")
#
print([i*i if i%2==0 else i**3 for i in sayilar],file=dosya)
"""
#
# for i in sayilar:
#     if i % 2 == 0:
#         dosya.write(f"\n{i ** 2}")
#     elif i % 2 != 0:
#         dosya.write(f"\n{i ** 3}")

### ÖDEV: Bir Şirket Otomasyonu tasarlayınız. İnsan Kaynakları, Muhasebe ve Bilgi İşlem birimleri olsun.
# Her personeli kendi birim adıyla oluşturulan txt dosyasına isim soyisim doğumyılı başlıkları altında personel bilgileri tutulsun.
# Personel ekleme, Güncelleme, Silme, Birime göre personel listeleme işlemlerini yapan bir menü tasarlayarak işlemler bu  menü üzerinden ilerlesin.

























