products=["Çikolata","Bisküvi","Kola"]
prices=[7,9,5.5]

username="admin"
password="123"

while True:
    secim=int(input("""
    Admin Girişi   - 1
    Müşteri Girişi - 2
    Çıkış          - 3
        Seçiminiz:"""))

    if secim==1:
        hak=1
        login=False
        while hak<4:
            kullaniciadi=input("Username:")
            sifre=input("Password:")
            if kullaniciadi==username and sifre==password:
                login=True
                break
            else:
                hak+=1
        if hak==4:
            print("Hakkınız Bitti.")
        elif login:
            while True:
                islem=int(input("""
1-Ürün Ekle
2-Ürün Güncelle
3-Ürün Sil
4-Ürün Listele
5-Çıkış
    Seçiminiz:"""))
                if islem==1:
                    productname=input("Ürün Adı:")
                    price=float(input("Ürün Fiyatı:"))
                    products.append(productname)
                    prices.append(price)
                elif islem==2:
                    for i in range(len(products)):
                        print(f"{i}-{products[i]}:{prices[i]}")
                    updatedproduct=int(input("Güncellenecek Ürün Numarası:"))
                    if -1<updatedproduct<len(products):
                        del products[updatedproduct]
                        del prices[updatedproduct]
                        productname = input("Ürün Adı:")
                        price = float(input("Ürün Fiyatı:"))
                        products.insert(updatedproduct,productname)
                        prices.insert(updatedproduct,price)
                    else:
                        print("Var olmayan ürün girişi!!")
                elif islem==3:
                    for i in range(len(products)):
                        print(f"{i}-{products[i]}:{prices[i]}")
                    deletedproduct=int(input("Silinecek Ürün Numarası:"))
                    if -1<deletedproduct<len(products):
                        del products[deletedproduct]
                        del prices[deletedproduct]
                    else:
                        print("Var olmayan ürün girişi!!")
                elif islem==4:
                    for i in range(len(products)):
                        print(f"{i}-{products[i]}:{prices[i]}")
                elif islem==5:
                    break
                else:
                    print("Hatalı Seçim!!")





    elif secim==2:
        for i in range(len(products)):
            print(f"{i}-{products[i]}:{prices[i]}")
        urun = int(input("Seçiminiz:"))
        if urun<len(products):
            miktar=0
            while True:
                miktar+=float(input("Para Yatırınız:"))
                if miktar>=prices[urun]:
                    print(f"Afiyet Olsun. Para Üstü:{miktar-prices[urun]}")
                    break
                else:
                    print("Yetersiz Bakiye!!")
                    cevap=input("Para Eklemek İster Misiniz?(E/H)").upper()
                    if cevap=="E":
                        continue
                    else:
                        print("Paranı Al:",miktar)
                        break
        else:
            print("Hatalı Ürün Seçimi!!")

    elif secim==3:
        print("Yine Bekleriz :*")
        break
    else:
        print("Hatalı Seçim!!!")