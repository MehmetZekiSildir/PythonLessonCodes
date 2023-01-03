import time

musteri=list()
manavmeyve=list()
manavsebze=list()
ELMA=ARMUT=KIRAZ=MUZ=CILEK=0
DOMATES=PATLICAN=BIBER=SOGAN=MANTAR=0
while True:
    print("********* HALE HOŞGELDİNİZ **********")
    secim=input("Meyve Mi? Sebze Mi?(M/S) Çıkmak İçin Q\n\tSeçiminiz:").upper()
    if secim=="M":
        while True:
            meyve=int(input("1-ELMA\n2-ARMUT\n3-MUZ\n4-KIRAZ\n5-CILEK\n6-ANA MENÜ\n\tMeyve Seçiminiz:"))
            if meyve==1:
                if "ELMA" not in manavmeyve:
                    manavmeyve.append("ELMA")
                ELMA+=float(input("Kaç Kilo İstersiniz?"))
            elif meyve==2:
                if "ARMUT" not in manavmeyve:
                    manavmeyve.append("ARMUT")
                ARMUT += float(input("Kaç Kilo İstersiniz?"))
            elif meyve==3:
                if "MUZ" not in manavmeyve:
                    manavmeyve.append("MUZ")
                MUZ += float(input("Kaç Kilo İstersiniz?"))
            elif meyve==4:
                if "KIRAZ" not in manavmeyve:
                    manavmeyve.append("KIRAZ")
                KIRAZ += float(input("Kaç Kilo İstersiniz?"))
            elif meyve==5:
                if "CILEK" not in manavmeyve:
                    manavmeyve.append("CILEK")
                CILEK += float(input("Kaç Kilo İstersiniz?"))
            elif meyve==6:
                print("Ana Menüye Yönlendiliyor...")
                time.sleep(3)
                break
            else:
                print("HATA!!")
            cevap = input("Başka arzunuz var mı?(E/H)").upper()
            if cevap!="E":
                break


    elif secim=="S":
        while True:
            sebze = int(input("1-DOMATES\n2-PATLICAN\n3-BIBER\n4-SOGAN\n5-MANTAR\n6-ANA MENÜ\n\tSebze Seçiminiz:"))
            if sebze == 1:
                if "DOMATES" not in manavsebze:
                    manavsebze.append("DOMATES")
                DOMATES += float(input("Kaç Kilo İstersiniz?"))
            elif sebze == 2:
                if "PATLICAN" not in manavsebze:
                    manavsebze.append("PATLICAN")
                PATLICAN += float(input("Kaç Kilo İstersiniz?"))
            elif sebze == 3:
                if "BIBER" not in manavsebze:
                    manavsebze.append("BIBER")
                BIBER += float(input("Kaç Kilo İstersiniz?"))
            elif sebze == 4:
                if "SOGAN" not in manavsebze:
                    manavsebze.append("SOGAN")
                SOGAN += float(input("Kaç Kilo İstersiniz?"))
            elif sebze == 5:
                if "MANTAR" not in manavsebze:
                    manavsebze.append("MANTAR")
                MANTAR += float(input("Kaç Kilo İstersiniz?"))
            elif sebze == 6:
                print("Ana Menüye Yönlendiliyor...")
                time.sleep(3)
                break
            else:
                print("HATA!!")
            cevap = input("Başka arzunuz var mı?(E/H)").upper()
            if cevap != "E":
                break
    elif secim=="Q":
        print("Yine Bekleriz...")
        time.sleep(3)
        break
    else:
        print("HATA!!")


while True:
    print("********* MANAV HOŞGELDİNİZ *********")
    secim=input("Meyve Mi? Sebze Mi?(M/S) Çıkmak İçin Q\n\tSeçiminiz:").upper()
    if secim=="M":
        if len(manavmeyve)==0:
            print("Meyveler tükenmiştir. :(")
            continue
        i=1
        for m in manavmeyve:
            print(f"{i}-{m}")
            i+=1
        meyve=input("Seçiminiz:").upper()
        if meyve in manavmeyve:
            if meyve=="ELMA":
                kilo=int(input("Kaç Kilo İstersiniz?"))
                if kilo<=ELMA:
                    musteri.append(meyve)
                    ELMA-=kilo
                    if ELMA==0:
                        manavmeyve.remove(meyve)
                else:
                    print(f"Elimizde {ELMA} kilo {meyve} verdır.")
            elif meyve == "ARMUT":
                kilo = int(input("Kaç Kilo İstersiniz?"))
                if kilo <= ARMUT:
                    musteri.append(meyve)
                    ARMUT -= kilo
                    if ARMUT == 0:
                        manavmeyve.remove(meyve)
                else:
                    print(f"Elimizde {ARMUT} kilo {meyve} verdır.")
            elif meyve == "MUZ":
                kilo = int(input("Kaç Kilo İstersiniz?"))
                if kilo <= MUZ:
                    musteri.append(meyve)
                    MUZ -= kilo
                    if MUZ == 0:
                        manavmeyve.remove(meyve)
                else:
                    print(f"Elimizde {MUZ} kilo {meyve} verdır.")
            elif meyve == "KIRAZ":
                kilo = int(input("Kaç Kilo İstersiniz?"))
                if kilo <= KIRAZ:
                    musteri.append(meyve)
                    KIRAZ -= kilo
                    if KIRAZ == 0:
                        manavmeyve.remove(meyve)
                else:
                    print(f"Elimizde {KIRAZ} kilo {meyve} verdır.")
            elif meyve == "CILEK":
                kilo = int(input("Kaç Kilo İstersiniz?"))
                if kilo <= CILEK:
                    musteri.append(meyve)
                    CILEK -= kilo
                    if CILEK == 0:
                        manavmeyve.remove(meyve)
                else:
                    print(f"Elimizde {CILEK} kilo {meyve} verdır.")

        else:
            print("Mevcut Olmayan Meyve !!")


    elif secim=="S":
        if len(manavsebze) == 0:
            print("Sebzeler tükenmiştir. :(")
            continue
        i = 1
        for m in manavsebze:
            print(f"{i}-{m}")
            i += 1
        sebze = input("Seçiminiz:").upper()
        if sebze in manavsebze:
            if sebze == "DOMATES":
                kilo = int(input("Kaç Kilo İstersiniz?"))
                if kilo <= DOMATES:
                    musteri.append(sebze)
                    DOMATES -= kilo
                    if DOMATES == 0:
                        manavsebze.remove(sebze)
                else:
                    print(f"Elimizde {DOMATES} kilo {sebze} verdır.")

            elif sebze == "PATLICAN":
                kilo = int(input("Kaç Kilo İstersiniz?"))
                if kilo <= PATLICAN:
                    musteri.append(sebze)
                    PATLICAN -= kilo
                    if PATLICAN == 0:
                        manavsebze.remove(sebze)
                else:
                    print(f"Elimizde {PATLICAN} kilo {sebze} verdır.")

            elif sebze == "BIBER":
                kilo = int(input("Kaç Kilo İstersiniz?"))
                if kilo <= BIBER:
                    musteri.append(sebze)
                    BIBER -= kilo
                    if BIBER == 0:
                        manavsebze.remove(sebze)
                else:
                    print(f"Elimizde {BIBER} kilo {sebze} verdır.")

            elif sebze == "SOGAN":
                kilo = int(input("Kaç Kilo İstersiniz?"))
                if kilo <= SOGAN:
                    musteri.append(sebze)
                    SOGAN -= kilo
                    if SOGAN == 0:
                        manavsebze.remove(sebze)
                else:
                    print(f"Elimizde {SOGAN} kilo {sebze} verdır.")

            elif sebze == "MANTAR":
                kilo = int(input("Kaç Kilo İstersiniz?"))
                if kilo <= MANTAR:
                    musteri.append(sebze)
                    MANTAR -= kilo
                    if MANTAR == 0:
                        manavsebze.remove(sebze)
                else:
                    print(f"Elimizde {MANTAR} kilo {sebze} verdır.")

        else:
            print("Mevcut Olmayan Sebze !!")
    elif secim=="Q":
        break
    else:
        print("HATA!!")

print("***** MÜŞTERİ BÖLÜMÜ *****")
for i in musteri:
    print(i)