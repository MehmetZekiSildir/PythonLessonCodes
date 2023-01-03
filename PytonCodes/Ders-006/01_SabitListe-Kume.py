#### TUPLE - Sabit Liste ###
# Listeden farklı olarak eleman ekleme silme yoktur.

# sabitListe=()
# sabitListe=tuple()
# print(type(sabitListe))

# sabitListe=(1,2,3)
# print(sabitListe)

## Eleman Ekleme YOK
# sabitListe+=[4]
# sabitListe.append(5)

## Eleman Silme YOK
# sabitListe.remove(2)

# numbers=(11,22,33,44,33,55,33)
# print(numbers.count(33))
# print(len(numbers))

### SET : KUME ###
# kume=set()

# kume={1,2,3,4}

## Eleman Ekleme
# kume.add(5)
# kume.add(5)
# kume.add(5)
# kume.add(5)

## Eleman Silme
# kume.remove(4)
# kume.remove(4) # Olmayan değer silme hatası

# kume.discard(4)
# kume.discard(4)
# kume.discard(4)
# kume.discard(4)
# print(kume)
# print(len(kume))


## Kume İşlemleri
kume={11,22,33,44}
kume2={33,44,55,66,77}

# print(kume2)

# İki küme farkı
# kumeFark=kume-kume2
# kumeFark=kume2.difference(kume)
# print(kumeFark)

# Küme Kesişim
# kumeKesisim=kume & kume2
# kumeKesisim=kume.intersection(kume2)
# print(kumeKesisim)

# Küme Birleşim
# kumeBirlesim=kume.union(kume2)
# print(kumeBirlesim)

# print(f"kume kumeBirlesim'in alt kumesi mi {kume.issubset(kumeBirlesim)}")
# print(f"kume kume2 farklı kumeler mi {kume.isdisjoint(kume2)}")
# print(f"kumeBirlesim kume2'nin üst küme mi {kumeBirlesim.issuperset(kume2)}")

### ALIŞTIRMALAR ###
#SORU: 1 - 15 arasında 5'er adet sayı üretip 2 farklı kümeye kaydediniz
#** Daha sonra iki kümeyi ekrana yazdırınız.
"""
import random
kumes=set()
kumes2=set()

i=0
while i<5:
    sayi=random.randint(1,15)
    # print(sayi)
    if sayi not in kumes2:
        kumes2.add(sayi)
        i+=1

while len(kumes)<5:
    sayi = random.randint(1, 15)
    kumes.add(sayi)

print(kumes)
print(kumes2)
"""



#PROJE:
"""
OTOMAT MAKİNESİ

1-Ürün al
2-Admin Giriş

# 1 Seçilirse
    Ekrana ürünler ve fiyatları yazılacak. 
    Müşteriden ürün kodu veya adı istenilecek para yatırması istenilecek  
        yeterli miktar yatırıldıysa para üstü verilerek Afiyet olsun. 
        Yeterli miktar yatırılmazsa ekleme yapılaması veya başka ürün seçmesi istenilecek.
# 2 Seçilirse
    Tanımlı bir admin adı ve şifresi 3 defa girilmesi istenilecek.
        Giriş başarılı ise
         1-Ürün ekle
         2-Ürün Güncelle
         3-Ürün Sil
        Giriş başarısız ise tekrarlanacak 3 hak bittiğinde 5 saniye program kitlenecek.Sonra tekrar 3 giriş hakkı verilecek.
"""









