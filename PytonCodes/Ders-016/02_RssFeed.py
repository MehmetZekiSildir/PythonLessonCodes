manavMeyveler = []
manavSebzeler = []
Müşteri = []
while True:
    print("sönmez HAL'e hoş geldniz.  Ne lazım abi?")
    cevap = input()
    if cevap == "meyve":
        while True:
            print("hangi meyveden istiyorsunuz abi")
            istek = input()
            if istek == "elma":
                print("kaç kilo abi")
                kilo = int(input("kaç kilo:"))
                manavMeyveler.append((kilo, "kg elma"))
                print("başka isteğiniz varmı abi")
                istek1 = input()
                if istek1 == "evet":
                    print("tabi abi")
                else:
                    print("tamam abi")
                    break
            if istek == "armut":
                print("kaç kilo abi")
                kilo = int(input("kaç kilo:"))
                manavMeyveler.append((kilo, "kg armut"))
                print("başka isteğiniz varmı abi")
                istek1 = input()
                if istek1 == "evet":
                    print("tabi abi")
                else:
                    print("tamam abi")
                    break
            if istek == "kiraz":
                print("kaç kilo abi")
                kilo = int(input("kaç kilo:"))
                manavMeyveler.append((kilo, "kg kiraz"))
                print("başka isteğiniz varmı abi")
                istek1 = input()
                if istek1 == "evet":
                    print("tabi abi")
                else:
                    print("tamam abi")
                    break
            if istek == "çilek":
                print("kaç kilo abi")
                kilo = int(input("kaç kilo:"))
                manavMeyveler.append((kilo, "kg çilek"))
                print("başka isteğiniz varmı abi")
                istek1 = input()
                if istek1 == "evet":
                    print("tabi abi")
                else:
                    print("tamam abi")
                    break
            if istek == "muz":
                print("kaç kilo abi")
                kilo = int(input("kaç kilo:"))
                manavMeyveler.append((kilo, "mus"))
                print("başka isteğiniz varmı abi")
                istek1 = input()
                if istek1 == "evet":
                    print("tabi abi")
                else:
                    print("tamam abi")
                    break
            else:
                print("malesef elimizde yok")

    elif cevap == "sebze":
        while True:
            print("hangi sebzeden istiyorsunuz abi")
            istek1 = input()
            if istek1 == "patlıcan":
                print("kaç kilo abi")
                kilo = int(input("kaç kilo:"))
                manavSebzeler.append((kilo, "kg patlıcan"))
                print("başka isteğiniz varmı abi")
                istek1 = input()
                if istek1 == "evet":
                    print("tabi abi")
                else:
                    print("tamam abi")
                    break
            if istek1 == "domates":
                print("kaç kilo abi")
                kilo = int(input("kaç kilo:"))
                manavSebzeler.append((kilo, "kg domates"))
                print("başka isteğiniz varmı abi")
                istek1 = input()
                if istek1 == "evet":
                    print("tabi abi")
                else:
                    print("tamam abi")
                    break
            if istek1 == "biber":
                print("kaç kilo abi")
                kilo = int(input("kaç kilo:"))
                manavSebzeler.append((kilo, "kg biber"))
                print("başka isteğiniz varmı abi")
                istek1 = input()
                if istek1 == "evet":
                    print("tabi abi")
                else:
                    print("tamam abi")
                    break
            if istek1 == "patates":
                print("kaç kilo abi")
                kilo = int(input("kaç kilo:"))
                manavSebzeler.append((kilo, "kg patates"))
                print("başka isteğiniz varmı abi")
                istek1 = input()
                if istek1 == "evet":
                    print("tabi abi")
                else:
                    print("tamam abi")
                    break
            if istek1 == "soğan":
                print("kaç kilo abi")
                kilo = int(input("kaç kilo:"))
                manavSebzeler.append((kilo, "kg soğan"))
                print("başka isteğiniz varmı abi")
                istek1 = input()
                if istek1 == "evet":
                    print("tabi abi")
                else:
                    print("tamam abi")
                    break
            else:
                print("malesef elimizde yok")

    elif cevap == "çıkış":
        print("yine bekleriz")
        break
    else:
        print("malesef elimizde yok")
print("meyve listesi", manavMeyveler)
print("sebze listesi", manavSebzeler)