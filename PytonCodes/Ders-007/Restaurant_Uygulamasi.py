masalar={"Masa-1":False,"Masa-2":False,"Masa-3":False,"Masa-4":False,"Masa-5":False}
corbalar={"1-Mercimek Çorbası":"7.00","2-Ezogelin Çorbası":"7.00","3-Yayla Çorbası   ":"6.00"}
baliklar={"1-Mezgit":"27.00","2-Palamut":"32.00","3-Çupra":"40.00"}
etler={"1-Pirzola":"56.00","2-Biftek":"65.00","3-Lokum":"45.00"}
makarnalar={"1-Bolanezli":"35.00","2-Körili":"35.00","3-Spagetti":"30.00"}
salatalar={"1-Çoban":"25.00","2-Sezar":"25.00","3-Mevsim":"25.00"}
icecekler={"1-Kola":"7.00","2-Şalgam":"7.00","3-Ayran":"7.00"}

# siparisler=dict()#{masa1:{Kola:7.00,Çoban:25.00}}
siparisler={"Masa-1":{'Ezogelin Çorbası': 7.0, 'Biftek': '65.00', 'Şalgam': '7.00', 'Çoban': '25.00', 'Çupra': '40.00'},
"Masa-2": {'Spagetti': '30.00', 'Ayran': '7.00'}}
while True:
    islem=int(input("""
    Sipariş      - 1
    Hesap        - 2
    Çıkış        - 3
    MasaTransfer - 4
    İşlem Seçiniz: """))

    if islem==1:
        print("""
        **************************************************
        ****** KARDEŞLER ET LOKANTASINA HOŞGELDİNİZ ******
        **************************************************
        """)
        kisiSayisi = int(input("Kaç Kişiyiz?"))
        musteriMasasi = str()
        for masa in masalar:  # masa: Key değerleri döner.
            if masalar[masa] == False:
                musteriMasasi = masa
                masalar[masa] = True
                break

        siparis={} # Gelen müşteri masasının siparişi
        for i in range(kisiSayisi):
            print(f"{i+1}. müşterinin siparişi")

            while True:
                print("""
                1-Çorba Çeşitleri
                2-Balık Çeşitleri
                3-Et Çeşitleri
                4-Makarna Çeşitleri
                5-Salata Çeşitleri
                6-İçecek Çeşitleri""")

                secim=int(input("Seçiminiz:"))
                if secim == 1:
                    for i in corbalar:
                        print(i, ":", corbalar[i])
                    secim1 = int(input("Seçiminiz:"))
                    if secim1 == 1:
                        if "Mercimek Çorbası" not in siparis:
                            siparis["Mercimek Çorbası"] = 7.00
                        else:
                            siparis["Mercimek Çorbası"] = siparis["Mercimek Çorbası"] + 7.00
                    elif secim1 == 2:
                        if "Ezogelin Çorbası" not in siparis:
                            siparis["Ezogelin Çorbası"] = 7.00
                        else:
                            siparis["Ezogelin Çorbası"] = siparis["Ezogelin Çorbası"] + 7.00
                    elif secim1 == 3:
                        if "Yayla Çorbası" not in siparis:
                            siparis["Yayla Çorbası"] = 6.00
                        else:
                            siparis["Yayla Çorbası"] = siparis["Yayla Çorbası"] + 6.00
                    else:
                        print("Hatalı Çorba Seçimi!!")
                elif secim == 2:
                    for i in baliklar:
                        print(i, ":", baliklar[i])
                    secim1 = int(input("Seçiminiz:"))
                    if secim1 == 1:
                        siparis["Mezgit"] = "27.00"
                    elif secim1 == 2:
                        siparis["Palamut"] = "32.00"
                    elif secim1 == 3:
                        siparis["Çupra"] = "40.00"
                    else:
                        print("Hatalı Balık Seçimi!!")
                elif secim == 3:
                    for i in etler:
                        print(i, ":", etler[i])
                    secim1 = int(input("Seçiminiz:"))
                    if secim1 == 1:
                        siparis["Pirzola"] = "56.00"
                    elif secim1 == 2:
                        siparis["Biftek"] = "65.00"
                    elif secim1 == 3:
                        siparis["Lokum"] = "45.00"
                    else:
                        print("Hatalı Et Seçimi!!")
                elif secim == 4:
                    for i in makarnalar:
                        print(i, ":", makarnalar[i])
                    secim1 = int(input("Seçiminiz:"))
                    if secim1 == 1:
                        siparis["Bolanezli"] = "35.00"
                    elif secim1 == 2:
                        siparis["Körili"] = "35.00"
                    elif secim1 == 3:
                        siparis["Spagetti"] = "30.00"
                    else:
                        print("Hatalı Makarna Seçimi!!")
                elif secim == 5:
                    for i in salatalar:
                        print(i, ":", salatalar[i])
                    secim1 = int(input("Seçiminiz:"))
                    if secim1 == 1:
                        siparis["Çoban"] = "25.00"
                    elif secim1 == 2:
                        siparis["Sezar"] = "25.00"
                    elif secim1 == 3:
                        siparis["Mevsim"] = "25.00"
                    else:
                        print("Hatalı Salata Seçimi!!")
                elif secim == 6:
                    for i in icecekler:
                        print(i, ":", icecekler[i])
                    secim1 = int(input("Seçiminiz:"))
                    if secim1 == 1:
                        siparis["Kola"] = "7.00"
                    elif secim1 == 2:
                        siparis["Şalgam"] = "7.00"
                    elif secim1 == 3:
                        siparis["Ayran"] = "7.00"
                    else:
                        print("Hatalı İçecek Seçimi!!")
                else:
                    print("Hatalı Menü Seçimi!")

                siparisler[musteriMasasi]=siparis
                print(siparisler)

                cevap=input("Başka bir arzunuz var mı? (E/H)").upper()
                if cevap=="E":
                    continue
                else:
                    break


    elif islem==2:
        for i in siparisler:
            print(i, "=>",siparisler[i])

        hesap=0
        masahesabi=input("Masa nuamarası:")
        for fiyat in siparisler["Masa-"+masahesabi].values():
            hesap+=float(fiyat)
        print(hesap)
        odeme=input("Ödeme yapıldı mı?(E/H)").upper()

        if odeme=="E":
            masalar["Masa-"+masahesabi]=False



    elif islem==3:
        print("Çıkış Yapıldı.")
        break

    elif islem==4:
        ilkmasa=input("Taşınacak Masa Numarası:")
        sonmasa=input("Nereye Taşınacak:")

        siparisler["Masa-"+sonmasa]=siparisler["Masa-"+ilkmasa].copy()
        siparisler["Masa-"+ilkmasa].clear()
        print(siparisler)
    else:
        print("Hatalı işlem!!")


