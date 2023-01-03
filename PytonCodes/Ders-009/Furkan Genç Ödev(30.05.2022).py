"""******************* Furkan Genç Ödev *******************"""

import os
import random
import datetime

if not os.path.exists("C:\TEST"): #Dosyayı oluşturdum.
    os.mkdir("C:\TEST")

today = datetime.datetime.now()
d3 = today.strftime("%d.%m.%Y %H:%M:%S") #Zamanı belirledim.

dosya=open("C:\TEST\Rastgele.txt",mode="w") #Dosyayı açtım.
dosya.write(f"ZAMAN {' ' * 23}OLAY SIRASI {' ' * 10}RASTGELE SAYI\n")# Başlıkları ekledim.
dosya.write(f"{'-' * 5}{' ' * 24}{'-' * 11}{' ' * 11}{'-' * 13}\n\n")#Başlıklar daha belirgin olsun fiye altına çizgi ekledim.

#
for i in range(1,11): #Başlıkların altını doldurdum.
    sayi = random.randint(0, 100)
    if i == 10:
        dosya.write(f"{d3} {' ' * 13}{i} {' ' * 19} {sayi}\n")
    else:
        dosya.write(f"{d3} {' ' * 13}{i} {' ' * 20} {sayi}\n")





