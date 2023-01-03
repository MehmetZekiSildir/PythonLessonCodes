####################  HAZIR STRING FONKSİYONLAR  ########################
"""
capitalize() İlk karakteri büyük harfe çevirir.
count()      Bir dizide belirtilen değerin kaç defa gerçekleştiğini döndürür.
endswith()   Dize belirtilen değer ile bitmiş ise true döndürür.
find()       Dizede belirli bir değeri arar ve bulunduğu yeri döndürür.
format()     Bir dizede belirtilen değerleri formatlar.
index()
isalpha()    Dizedeki bütün karakterleri alfabede ise True döndürür.
isdecimal()  Dizedeki bütün karakterler ondalıksa True döndürür.
isdigit()    Dizedeki bütün karakterler sayısal ise True döndürür.
islower()
isupper()
isnumeric()  Dizedeki bütün karakterler numeric ise True döndürür.
isspace()    Dizede boşluk varsa True döndürür.
ljust()      Dizeyi sola dayalı bir sürüm döndürür.
rjust()
lstrip()     Dizenin sol trim versiyonunu döndürür.
rstrip()
strip()
replace()
split()      Dizeyi belirtilen ayrıcıya böler.
isalnum()    Dizedeki değerler Alfabe ve numara olması durumunda True döner
"""

# metin="aliReza"
# print(metin.capitalize())

# metin="Altan"
# print(metin.isalpha())
# if metin.isalnum():
#     print("Evet hepsi harftir.")


# metin="Altan12"
# if metin.isalnum():
#     print("Harf ve Rakam var")


# metin="Altan.Emre.Demirci"
# print(metin.split('.'))
# print(metin.split('.',1))

# metin="     Yiğit&Kübra      "
# print(metin)
# print(metin.rstrip())
# print(metin.lstrip())
# print(metin.strip())


############ DATETIME KUTUPHANE #############
# import datetime
from datetime import datetime

zaman=datetime.now()
print(zaman)
# print(zaman.year)
# print(zaman.month)
# print(zaman.day)
# print(zaman.hour)
# print(zaman.minute)
# print(zaman.second)
# print(zaman.date())
# print(zaman.time())

# zmn=datetime(2022,5,24)
# print(zmn)

## Zaman Formatlama ##
print("Zaman değişkenin formatlı hali: ",zaman.strftime("%d-%m-%Y"))

"""
%d  : rakam ile gün
%m  : rakam ile ay
%Y  : rakam ile 4 haneli yıl
%y  : rakam ile 2 haneli yıl
%b  : yazı ile 3 haneli ay
%H  : rakam ile saat 
%M  : rakam ile dakika 
%S  : rakam ile saniye 
%a  : yazı ile 3 haneli gün
%A  : yazı ile tam gün adı
%D  : AY/GUN/YIL
"""
"""
print(zaman.strftime("Bugün Günlerden: %A"))

import locale

locale.setlocale(locale.LC_ALL,"tr")

print(zaman)
print(zaman.strftime("Bugün Günlerden: %A"))
print(zaman.strftime("Bugün Günlerden: %B"))
"""

### Şimdi zamanı ekrana GUN-AY-YIL--Saat:Dakika:Saniye--GünAdı
from datetime import datetime
today = datetime.now()

d3 = today.strftime("%d-%m-%Y--%H:%M:%S--%A")
print("d3 =", d3)













