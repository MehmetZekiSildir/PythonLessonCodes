#### TRY-EXCEPT  OR  TRY-CATCH ####
"""
try:
    kontrol edilecek kod bloğu
except:
    hata olması durumunda yapılacak işlemler

"""

# sayi=int(input("Sayı:"))
# print("Devamke")
# try:
#     sayi = int(input("Sayı:"))
# except:
#     print("Lütfen sayı değerini RAKAM ile giriniz ULAN!!")

# while True:
#     try:
#         sayi = int(input("Sayı:"))
#         print(sayi)
#         break
#     except:
#         print("Lütfen sayı değerini RAKAM ile giriniz ULAN!!")

## finally: try veya except bloklarından hangisi çalıştığı fark etmeksizin mutlaka çalışır.

# try:
#     sayi = int(input("Sayı:"))
#     print(sayi)
# except:
#     print("Lütfen sayı değerini RAKAM ile giriniz ULAN!!")
# finally:
#     print("Her türlü çalışır")

# dosya=open("sayi.txt","w")
# try:
#     sayi=input("Sayı:")
#     dosya.write(sayi)
#     dosya.close()
# except:
#     print("HATA!!")
#
# finally:
#     dosya.close()



# with open("my_file.txt") as file:
#     content = file.read()
#     print(content)

##### HATAYA GÖRE MESAJ #####
# try:
#     sayi = int(input("Sayı:"))
#     print(12/ sayi)
#     liste=[sayi]
#     print(liste[1])
# except ValueError:
#     print("Giriş Değeri Hatası!")
# except ZeroDivisionError:
#     print("Sıfıra Bölme Hatası!!")
# except IndexError:
#     print("Listenin Uzunluğu Dışında Hatası!!")
# except:
#     print("Bilinmeyen Hata!!")


# try:
#     sayi = int(input("Sayı:"))
#     print(12/sayi)
#     liste = [sayi]
#     print(liste[1])
# except Exception as e:
#     print(e.__class__.__name__+":"+str(e))


#### HATA FIRLATMA : TANIMLAMA raise() ####
###########################################
# not1=float(input("Vize notu giriniz:"))
#
# if not1<0 or not1>100:
#     # raise Exception("Not Aralığı Hatası!!!")
#     raise OverflowError("Not Aralığı Hatası!!!")


# try:
#     not1 = float(input("Vize notu giriniz:"))
#
#     if not1 < 0 or not1 > 100:
#         # raise Exception("Not Aralığı Hatası!!!")
#         raise OverflowError()
#
# except OverflowError:
#     print("Not Aralığı Hatası!!!")
#
# print("Bug olmaz devamke")

### ASSERT => iddaa edilen ###
# email="sexi_velet_17@hotmail.com"
#
# eposta=input("Email Adresi:")
# assert eposta==email ## aynı değilde iddaa edilen yanlış olduğundan hata fırlatır.

###### ALIŞTIRMALAR #######
# Kullanıcıdan 2 sayı 1 işlem alıp önceden tanımladığmız methodlara alınan değerleri göndereceğiz.
    # işlem topla,cikar,carp veya bol'den biri değilse ASSERT fırlatın.
    # Kullancııdan veri alınırken VALUEERROR verdiğidne bir defa daha isteyiniz.
    # ZERODIVISIONERROR hatası alırsanız veri istenmesin.


# def DORTISLEM():
#     s1 = int(input("Sayı1:"))
#     s2 = int(input("Sayı2:"))
#     islem = input("İşlem:")
#     assert islem=="+" or islem=="-" or islem=="*" or islem=="/"
#     if islem=="+":
#         print(s1+s2)
#     elif islem=="-":
#         print(s1-s2)
#     elif islem=="*":
#         print(s1*s2)
#     elif islem=="/":
#         print(s1/s2)
#
# try:
#     DORTISLEM()
# except ValueError:
#     DORTISLEM()
# except ZeroDivisionError:
#     print("Sıfıra Bölme Hatası!!")

#
# islems=["+","-","*","/"]
# def DortIslem(s1,s2,islem):
#     assert islem in islems
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


### LOGLAMA ###
"""
import datetime

dd=open("log.txt","a",encoding="utf8")

while True:
    try:
        sayi=int(input("Sayı:"))
        print(sayi*2)
        print(sayi/0)
    # except ValueError:
    #     print("{} -> ValueError Hatası".format(datetime.datetime.now().strftime("%d.%m.%Y %H:%M")),file=dd)
    #     break
    # except ZeroDivisionError:
    #     print("{} -> ZeroDivision Hatası".format(datetime.datetime.now().strftime("%d.%m.%Y %H:%M")),file=dd)
    #     break
    except Exception as e:
        print("{} -> {} Hatası".format(datetime.datetime.now().strftime("%d.%m.%Y %H:%M"),e.__class__.__name__), file=dd)
        break
"""
# import  traceback
# try:
#     s=int(input("sdad"))
#
# except Exception as e:
#     print(traceback._format_final_exc_line(type(e)))
















