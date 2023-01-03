######## DICTIONARY (SOZLUK) ##########
"""
sozluk={}
sozluk=dict()
print(type(sozluk))

# Sozluk={key:value,key:value,...}

sozluk={"renk1":"Siyah","renk2":"Kırmızı","renk3":"Turuncu"}

print(sozluk)
# print(sozluk.keys())
# print(sozluk.values())
# print(sozluk.items())

# print(sozluk["renk2"])
# print(sozluk["Kırmızı"]) # value üzerinde erişim imkansızdır. KeyError hatası verir.

# print(sozluk.get("renk4")) # Olmayan Key değerine ulaşılamadığında None döndürür.

# print(len(sozluk))

sozluk["renk4"]="Beyaz"
sozluk["renk3"]="Mavi"

print(sozluk)
"""

# sozluk={1:"Ali","Metin":2.5,"Elran":True}
# # sozluk.clear()
# del sozluk["Metin"]
# print(sozluk)

# sozluk={"renk1":"Siyah","renk2":"Kırmızı","renk3":"Turuncu"}
# print("Siyah" in sozluk)
# print("Siyah" in sozluk.values())
#
# print("renk3" in sozluk)
# print("renk3" not in sozluk)

"""
s1={"ad":"Selim","soyad":"Kaçar"}
s2={"soyad":"Kaçar","ad":"Selim"}
s3={"soyad":"Varan","ad":"Selim"}

print("s1 s2 ye eşit mi?",s1==s2)
print("s2 s3 ye eşit mi?",s3==s2)
"""

# s1={"ad":"Selim","soyad":"Kaçar"}
# s2={"soyad":"Kaçar","ad":"Selim"}
# s3={"soyad":"Varan","ad":"Selim"}
# s4={"soyad":"Varan","ad":"Selim","yas":32}

# s2.update(s4)
# print(s2)


# s5=s2 # ramde aynı adreste tutuldukları için her işlem ikisinide etkiler.
# print(s2)
# print(s5)
#
# s2["Yas"]=45
# print(s2)
# print(s5)


# s5=s2.copy() # ramde farklı adreslerde tutuldukları için birine uygulanan işlem diğerini ilgilendirmez.
# print(s2)
# print(s5)
#
# s2["Yas"]=45
# print(s2)
# print(s5)

# sozluk={"renk1":"Siyah","renk2":"Kırmızı","renk3":"Turuncu"}
#
# kelime = sozluk.pop("renk1")
# print(sozluk)
# print(kelime)

# s3lu={}
# list1=[1,2,3,4,5]
# list2=[6,7,8,9,0]
# list3=[11,22,33]
#
# s3lu["x"]=list1
# s3lu["y"]=list2
# s3lu["z"]=list3
# print(s3lu)


## SORU: Kullanıcıdan alınan ad,soyad,yas,cinsiyet bilgilerini Personel isimli bir dict ekleyin ve ad soyad bilgilerini ekrana yazdırınız

# ad = input("ad")
# soyad = input("soyad")
# yas = input("yas")
# cinsiyet = input("cinsiyet")

# Personel=dict()
# Personel["ad"]=ad
# Personel["soyad"]=soyad
# Personel["yas"]=yas
# Personel["cinsiyet"]=cinsiyet
#
# Personel = {"ad": ad, "soyad": soyad, "yas": yas, "cinsiyet": cinsiyet}
#
# print(Personel["ad"] + Personel["soyad"])


# ÖDEV: Bir firmanın IK, IT, MUH departmanlarının çalışan listelerini yöneticiden isteyerek bir dict atınız
# ve ekrana istenilen bölümdeki çalışanları listeyiniz.

# sirket=dict()
# IK=[]
# IT=[]
# MUH=[]
#
# while True:
#     secim=int(input("1-Personel Ekle\n2-Personel Listele\n3-Çıkış\n\tNe yapmak istersiniz?"))
#     if secim==1:
#         isim = input("Ad:")
#         bolum=int(input("1-IK\n2-IT\n3-MUH\n\tSeçiminiz:"))
#         if bolum==1:
#             IK.append(isim)
#             sirket["IK"]=IK
#         elif bolum==2:
#             IT.append(isim)
#             sirket["IT"] = IT
#         elif bolum==3:
#             MUH.append(isim)
#             sirket["MUH"] = MUH
#         else:
#             print("Hatalı Seçim!!")
#     elif secim==2:
#         bolum=int(input("1-IK\n2-IT\n3-MUH\n\tSeçiminiz:"))
#         if bolum==1:
#             print(sirket["IK"])
#         elif bolum==2:
#             print(sirket["IT"])
#         elif bolum==3:
#             print(sirket["MUH"])
#     elif secim == 3:
#         break
#     else:
#         print("Hatalı Seçim")

## ÖDEV:
'''
# SORU: sözlük uygulaması olsun Tr-Eng
#       sözlük={"siyah":"black"...}
#       kullanıcı 4 seçenekli bir menü verelim
#          1-Arama
           2-Çıkarma
           3-Listeleme
           4-Çıkış

        Kullanıcı 1'e basarsa ->
            - Aranacak kelimeyi giriniz:
            - Bu kelime dict varsa english karşılığını yazılır.
            - Yoksa uygulamayı geliştirmek istermisiniz?
                - E ise bu kelimenin ingilizce karşılığını alırız ve sözlüğe eklenir.
                - H ise Peki.. 
        Kullanıcı 2'e basarsa -> 
            - Çıkarılmak istenen kelime:
            - Kelime sözlükte varsa çıkartılır.
            - Yoksa uyarı verilir.
        Kullanıcı 3'e basarsa ->
            - Tum key value lar listenilir.
            - KEY -> VALUE
        Kullanıcı 4'e basarsa ->
            - Döngü sonlanır..
'''
"""
sozluk={"kırmızı":"red","kalem":"pen"}
while True:
    soru = int(input("1-Arama\n2-Çıkarma\n3-Listeleme\n4-Çıkış\nYapmak istediğiniz işlemin numarasını giriniz:"))
    if soru==4:
        print("İyi Günler Dileriz")
        break
    elif soru==1:
        arama=input("Aramak istediğiniz kelimeyi giriniz:")
        if arama in sozluk:
            print(sozluk[arama])
        else:
            arama2=input("Kelime Sözlüğümüzde mevcut değil.Sözlüğe eklemek ister misiniz?\nEVET\nHAYIR").upper()
            if arama2=="EVET":
                arama3=input("Aradığınız kelimenin anlamını yazınız:")
                sozluk[arama]=arama3
                print(sozluk)
                print("Katkınız için teşekür ederiz")
            else:
                print(""
                      "Giriş ekranına yönlendiriliyorsunuz...")

    elif soru==2:
        cıkarma=input("Çıkarmak istediğiniz kelimeyi giriniz:")
        if cıkarma in sozluk:
            del sozluk[cıkarma]
            print(sozluk)
        else:
            print(cıkarma,"Bu kelime sözlüğümüzde mevcut değil")

    elif soru==3:
        for i in sozluk:
            print(i,"=>",sozluk[i])
    else:
        print("Hatalı Giriş!")
"""







