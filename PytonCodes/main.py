
vize=0


while True:
    while True:
        try:
            vize = int(input("Vize Notunu Giriniz"))
            break
        except:
            print("Lütfen bir sayi giriniz:")
    if 0<=vize<=100:
        while True:
            try:
                final=int(input("Final Notunu Giriniz:"))
                break
            except:
                print("Lütfen sayi giriniz")
        break

    else:  
        print("0-100 aralıgında sayi giriniz:")
        continue

ort=(vize+final)/2

if (0<=ort<=24):
            print("FF")
            print(f"Notunuz:{ort}")
elif (25<=ort<=44):
            print(f"Notunuz:{ort}")
            print("DD")
            
elif (45<=ort<=54):
            print(f"Notunuz:{ort}")
            print("CC")
elif (55<=ort<=69):
            print(f"Notunuz:{ort}")
            print("CB")
elif (70<=ort<=84):
            print(f"Notunuz:{ort}")
    
            print("BB")
else:
            print(f"Notunuz:{ort}")
            print("AA")