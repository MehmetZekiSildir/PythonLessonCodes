##### Zip() #####
'''
Kelimenin çevirsine baktığımızdaki anlamı yansıtır.zip fermuar anlamına gelir ve bu mantıkla kullanılır.
2 Listeyi birbiri indisleri üzerine birleştiriyor. Bunu yaparken eleman sayısı az olan listeyi baz alır.

zip(list1,list2)

zip çalıştığında list, tuple veya dict döndürür.
'''

# list1=["Ali","Veli","Deli","Furkan"]
# list2=[23,34,45]
# print(list(zip(list1,list2)))
# sonuc=zip(list1,list2)
# for i,j in sonuc:
#     print("{} -> {}".format(i,j))


##### FILTER #####
'''
sayılabilen (iterable) tipindeki değerlerin içindeki , item'ları süzme işlemi yapar ve sadece True deger donduren sonuçları verir.
Verdiği sonucun tipi filter tipindedir. Bunu list veya tuple çevirmemiz gereklidir. Döngülere göre hız olarak daha başarılıdır.
'''

# liste=[1,2,3,4,5,6,7,8,9,10]
#
# sonuc=list(filter(lambda i: i%2==0,liste))
# print(sonuc)


## int veya float tipleri filtreleyin
# karisikListe=[12,23.5,45,"56",98,56.34]
#
# print(tuple(filter(lambda s: type(s)==int or type(s)==float,karisikListe)))


### ÖRNEK :
# filter(func,iter)

# def baslik(header):
#     return header.istitle()
#
# liste=["Python Dersleri","django","Gazi üniversitesi","Python","JAVA"]
#
# print(tuple(filter(baslik,liste)))



## Tek Satır FOR
# liste=[1,2,3,4,5,6,7,8,9,10]
#
# print(list(filter(lambda s: s<9 and s>3,liste)))
# print([s for s in liste if s<9 and s>3])
# print([s for s in [1,2,3,4,5,6,7,8,9,10] if s<9 and s>3])


### FILTER,ZIP BİRLİKTE KULLANIMI ###
# kisiler=["Semih","Adnan","Bihter","Behlül"]
# dogumyillari=[1990,1963,1992,1989]
#
# ## Doğum yılı 1989 dan büyük olanlar.
# zipped=zip(kisiler,dogumyillari)
# # print(list(zipped))
# print(list(filter(lambda z: z[1]>1989, zipped)))
#
# print(list(filter(lambda z: z[1]>1989, zip(kisiler,dogumyillari))))

### ÖRNEK
liste=[6,1,8,7,3,9,2,4]

print([x**2 if x%2==0 else x**3 for x in liste])