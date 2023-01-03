import os,random,datetime

bugun = datetime.datetime.now()
gunler = bugun.strftime("%d.%m.%Y %H:%M:%S")

rastgele = open("C:\\TEST\\rastgele2.txt",mode="w")
rastgele.write(f"Zaman {' ' * 18}OLAY SIRASI {' ' * 10}RASTGELE SAYI\n")


for i in range(1, 11):
        randomsayi = random.randint(1,101)
        rastgele.write(f"{gunler} {' ' * 10}{i} {' ' * 20} {randomsayi}\n")




