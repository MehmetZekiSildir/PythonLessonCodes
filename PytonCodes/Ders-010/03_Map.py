##### Map() ######
'''
iterable(sayılabilen) tipteki değişkenin içindeki elemanlara matematiksel işlem yapmaya yarar. Sorgu işlemi yapılamaz, yapılırsa True-False değer döner.

map(func,iter)
'''
liste=[2,3,4]
def karesi(sayi):
    return sayi*sayi

# kareler=list()
# for i in liste:
#     kareler.append(karesi(i))
# print(kareler)

# print(list(map(karesi,liste)))
#
# kareler=list(map(karesi,liste))
# print(kareler)

###ÖRNEK:
# dd=[1,2,3,4,5,6,7,8,9]
# print(tuple(map(lambda s: s*s,dd)))
#
# print(list(map(lambda s: s*s,filter(lambda c: c%2==0,dd))))


## SORU: Aşağıdaki liste elemanlarının integer tipde olanları 2'ye bölüp ekrana yazdırınız.
# liste=[1,32,True,234,213,"1234",34.567,6,74,12]
#
# ints=list(filter(lambda i: type(i)==int or type(i)==float,liste))
# print(ints)
#
# print(list(map(lambda s: s/2,ints)))
#
# print(list(map(lambda s: s/2,filter(lambda i: type(i)==int or type(i)==float,liste))))




