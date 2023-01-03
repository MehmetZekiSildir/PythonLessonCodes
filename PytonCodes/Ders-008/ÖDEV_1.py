
print("""
         [DOLAR]  ALIŞ:15.10    SATIŞ:16.00
         [EURO]   ALIŞ:19.30    SATIŞ:20.05
         [YUAN]   ALIŞ:17.35    SATIŞ:18.15

    DOLAR (1)     EURO (2)     YUAN (3)     LİRA (4)
         """)
dolar_satıs=16.00
dolar_alıs=15.00
euro_satıs=20.00
euro_alıs=19.00
yuan_satıs=18.00
yuan_alıs=17.00

def giris():
    alınacak=input("Satmak istediginiz para birligi giriniz :")
    satılacak=input("Almak istediginiz para birligi giriniz  :")

    if alınacak == "1" and satılacak == "2":    # dolar ve euro
        euro =float(input("Kaç euro ister siniz? :"))
        if euro >= 100:
            kimlik =input("Kimliginiz var mı? (E/H) :").upper()
            if kimlik == "E":
                euro_lira = euro * float(euro_satıs)                 # alacağı euroyu liraya çevirdik
                dolar_lira = float(euro_lira) / float(dolar_alıs)    # sonucu alıs dolara böldük
                print(f" Vermeniz gereken : {dolar_lira}  dolar")
            elif kimlik == "H":
                print("Maalesef paranız 100(dolar,euro,yuan)'dan yüksek ise kimlik lazım olacak!")
            else:
                print("HATA!!!")
        elif euro < 100:
            euro_lira =euro *float(euro_satıs)
            dolar_lira =float(euro_lira ) /float(dolar_alıs)
            print(f" Vermeniz gereken : {dolar_lira}  dolar")

    elif alınacak == "1" and satılacak == "3":  # dolar ve yuan
        yuan =float(input("Kaç yuan ister siniz? :"))
        if yuan >= 100:
            kimlik =input("Kimliginiz var mı? (E/H) :").upper()
            if kimlik == "E":
                yuan_lira = yuan * float(yuan_satıs)
                dolar_lira = float(yuan_lira) / float(dolar_alıs)
                print(f" Vermeniz gereken : {dolar_lira}  dolar")
            elif kimlik == "H":
                print("Maalesef paranız 100(dolar,euro,yuan)'dan yüksek ise kimlik lazım olacak!")
            else:
                print("HATA!!!")
        elif yuan < 100:
            yuan_lira = yuan * float(yuan_satıs)
            dolar_lira = float(yuan_lira) / float(dolar_alıs)
            print(f" Vermeniz gereken : {dolar_lira}  dolar")
    elif alınacak == "1" and satılacak == "4":  # dolar ve lira
        dolar = float(input("Kaç dolar satacaksınız ? :"))
        if dolar >= 100:
            kimlik = input("Kimliginiz var mı? (E/H) :").upper()
            if kimlik == "E":
                lira = dolar_alıs * dolar
                print(f" Vermeniz gereken : {lira}  lira")
            elif kimlik == "H":
                print("Maalesef paranız 100(dolar,euro,yuan)'dan yüksek ise kimlik lazım olacak!")
            else:
                print("HATA!!!")
        elif dolar < 100:
            lira=dolar_alıs*dolar
            print(f" Vermeniz gereken : {lira}  lira")
        else:
            print("HATA!!")

    elif alınacak == "2" and satılacak == "1":  # euro ve dolar
        dolar =float(input("Kaç dolar ister siniz? :"))
        if dolar >= 100:
            kimlik =input("Kimliginiz var mı? (E/H) :").upper()
            if kimlik == "E":
                dolar_lira = dolar * float(dolar_satıs)
                euro_lira = float(dolar_lira) / float(euro_alıs)
                print(f" Vermeniz gereken : {euro_lira}  euro")
            elif kimlik == "H":
                print("Maalesef paranız 100(dolar,euro,yuan)'dan yüksek ise kimlik lazım olacak!")
            else:
                print("HATA!!!")
        elif dolar < 100:
            dolar_lira = dolar * float(dolar_satıs)
            euro_lira = float(dolar_lira) / float(euro_alıs)
            print(f" Vermeniz gereken : {euro_lira}  euro")

    elif alınacak == "2" and satılacak == "3":  # euro ve yuan
        yuan =float(input("Kaç yuan ister siniz? :"))
        if yuan >= 100:
            kimlik =input("Kimliginiz var mı? (E/H) :").upper()
            if kimlik == "E":
                yuan_lira = yuan * float(yuan_satıs)
                euro_lira = float(yuan_lira) / float(euro_alıs)
                print(f" Vermeniz gereken : {euro_lira}  euro")
            elif kimlik == "H":
                print("Maalesef paranız 100(dolar,euro,yuan)'dan yüksek ise kimlik lazım olacak!")
            else:
                print("HATA!!!")
        elif yuan < 100:
            yuan_lira = yuan * float(yuan_satıs)
            euro_lira = float(yuan_lira) / float(euro_alıs)
            print(f" Vermeniz gereken : {euro_lira}  euro")
    elif alınacak == "2" and satılacak == "4":
        euro = float(input("Kaç euro satacaksınız ? :"))
        if euro >= 100:
            kimlik = input("Kimliginiz var mı? (E/H) :").upper()
            if kimlik == "E":
                lira = euro_alıs * euro
                print(f" Vermeniz gereken : {lira}  lira")
            elif kimlik == "H":
                print("Maalesef paranız 100(dolar,euro,yuan)'dan yüksek ise kimlik lazım olacak!")
            else:
                print("HATA!!!")
        elif euro < 100:
            lira = euro_alıs * euro
            print(f" Vermeniz gereken : {lira}  lira")
        else:
            print("HATA!!")

    elif alınacak == "3" and satılacak == "1":  # yuan ve dolar
        dolar =float(input("Kaç dolar ister siniz? :"))
        if dolar >= 100:
            kimlik =input("Kimliginiz var mı? (E/H) :").upper()
            if kimlik == "E":
                dolar_lira = dolar * float(dolar_satıs)
                yuan_lira = float(dolar_lira) / float(yuan_alıs)
                print(f" Vermeniz gereken : {yuan_lira}  yuan")
            elif kimlik == "H":
                print("Maalesef paranız 100(dolar,euro,yuan)'dan yüksek ise kimlik lazım olacak!")
            else:
                print("HATA!!!")
        elif dolar < 100:
            dolar_lira = dolar * float(dolar_satıs)
            yuan_lira = float(dolar_lira) / float(yuan_alıs)
            print(f" Vermeniz gereken : {yuan_lira}  yuan")

    elif alınacak == "3" and satılacak == "2":  # yuan ve euro
        euro =float(input("Kaç euro ister siniz? :"))
        if euro >= 100:
            kimlik =input("Kimliginiz var mı? (E/H) :").upper()
            if kimlik == "E":
                euro_lira = euro * float(euro_satıs)
                yuan_lira = float(euro_lira) / float(yuan_alıs)
                print(f" Vermeniz gereken : {yuan_lira}  yuan")
            elif kimlik == "H":
                print("Maalesef paranız 100(dolar,euro,yuan)'dan yüksek ise kimlik lazım olacak!")
            else:
                print("HATA!!!")
        elif euro < 100:
            euro_lira = euro * float(euro_satıs)
            yuan_lira = float(euro_lira) / float(yuan_alıs)
            print(f" Vermeniz gereken : {yuan_lira}  yuan")
    elif alınacak == "3" and satılacak == "4":
        yuan = float(input("Kaç yuan satacaksınız ? :"))
        if yuan >= 100:
            kimlik = input("Kimliginiz var mı? (E/H) :").upper()
            if kimlik == "E":
                lira = yuan_alıs * yuan
                print(f" Vermeniz gereken : {lira}  lira")
            elif kimlik == "H":
                print("Maalesef paranız 100(dolar,euro,yuan)'dan yüksek ise kimlik lazım olacak!")
            else:
                print("HATA!!!")
        elif yuan < 100:
            lira = yuan_alıs * yuan
            print(f" Vermeniz gereken : {lira}  lira")
        else:
            print("HATA!!")
    elif alınacak == "4" and satılacak == "1":  # lira ve dolar
        dolar =float(input("Kaç dolar ister siniz? :"))
        if dolar >= 100:
            kimlik =input("Kimliginiz var mı? (E/H) :").upper()
            if kimlik == "E":
                dolar_lira = dolar * float(dolar_satıs)
                print(f" Vermeniz gereken : {dolar_lira}  lira")
            elif kimlik == "H":
                print("Maalesef paranız 100(dolar,euro,yuan)'dan yüksek ise kimlik lazım olacak!")
            else:
                print("HATA!!!")
        elif dolar < 100:
            dolar_lira = dolar * float(dolar_satıs)
            print(f" Vermeniz gereken : {dolar_lira}  lira")

    elif alınacak == "4" and satılacak == "2":  # lira ve euro
        euro =float(input("Kaç euro ister siniz? :"))
        if euro >= 100:
            kimlik = input("Kimliginiz var mı? (E/H) :").upper()
            if kimlik == "E":
                euro_lira = euro * float(euro_satıs)
                print(f" Vermeniz gereken : {euro_lira}  lira")
            elif kimlik == "H":
                print("Maalesef paranız 100(dolar,euro,yuan)'dan yüksek ise kimlik lazım olacak!")
            else:
                print("HATA!!!")
        elif euro < 100:
            euro_lira = euro * float(euro_satıs)
            print(f" Vermeniz gereken : {euro_lira}  lira")

    elif alınacak == "4" and satılacak == "3":  # lira ve yuan
        yuan =float(input("Kaç yuan ister siniz? :"))
        yuan = float(input("Kaç euro ister siniz? :"))
        if yuan >= 100:
            kimlik = input("Kimliginiz var mı? (E/H) :").upper()
            if kimlik == "E":
                yuan_lira = yuan * float(yuan_satıs)
                print(f" Vermeniz gereken : {yuan_lira}  lira")
            elif kimlik == "H":
                print("Maalesef paranız 100(dolar,euro,yuan)'dan yüksek ise kimlik lazım olacak!")
            else:
                print("HATA!!!")
        elif yuan < 100:
            yuan_lira = yuan * float(yuan_satıs)
            print(f" Vermeniz gereken : {yuan_lira}  lira")
    else:
        print("HATA!!!")

giris()























