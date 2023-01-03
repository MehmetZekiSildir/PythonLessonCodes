### ACCESS MODIFIER ###
# public,private
#region public: Genel erişime açık anlamına gelir. Her dosyadan her classtan erişilebilir.
"""
class Muhendis:
    ad="Yiğit"
    soyad="Kumbasar"

    def EkranYaz(self):
        print(self.ad)
        print(self.soyad)



muh=Muhendis()
print(muh.ad)
print(muh.soyad)
muh.EkranYaz()
"""
#endregion

#private: Sadece kendi tanımlı olduğu class içinde erişime açık anlamına gelir. Class dışından erişime kapalıdır. '__' iki alt çizgi ile tanımlanır.
"""
class Muhendis:
    ad="Yiğit"
    __soyad="Kumbasar"

    def EkranYaz(self):
        print(self.ad)
        print(self.__soyad)




muh=Muhendis()
# print(muh.ad)
# print(muh.__soyad)
muh.EkranYaz()

"""

# class Muhendis:
#     def __init__(self):
#         self.__ad=""
#         self.__soyad=""
#         self.__Kayit()
#
#     def __Kayit(self):
#         ad=input("Adınız:")
#         soyad=input("Soyadınız:")
#         if ad.isalpha() and soyad.isalpha():
#             self.__ad=ad
#             self.__soyad=soyad
#
#     def Yazdir(self):
#         print(self.__ad+" "+self.__soyad)
#
# muh=Muhendis()
# muh.Yazdir()
"""
class Musteri:
    ad=""
    soyad=""
    __tc=""

    def Kayit(self):
        self.ad=input("Ad:")
        self.soyad=input("Soyad:")
        while True:
            tc=input("TC:")
            if len(tc)==11 and tc.isdigit():
                self.__tc=tc
                break
            else:
                print("TC bilgisi hatalı!!")

    def Yaz(self):
        print(self.ad+" "+self.soyad+" "+self.__tc)

m=Musteri()
m.Kayit()
m.Yaz()
"""


############ KAPSULLEME (Encapsulation) #############

# getter methodlar private özellikleri okumayı sağlar. readonly
# setter methodlar private özelliklere değer atamayı sağlar.
"""
class Musteri:
    ad=""
    soyad=""
    __tc="11111"

    def Kayit(self):
        self.ad=input("Ad:")
        self.soyad=input("Soyad:")

    def getTC(self):
        return self.__tc

    def setTC(self,value):
        if len(value)==11 and value.isdigit():
            self.__tc=value
        else:
            self.__tc="0000"


    def Yaz(self):
        print(self.ad+" "+self.soyad+" "+self.__tc)

m=Musteri()
m.setTC("1234567890")
print(m.getTC())
"""







