# ## ÖDEV: 1-100 arası üretilen 10 adet rastgele sayıyı Rastgele.txt isimli dosyaya aşağıdaki formatla yazdırınız.
import os
import random
import datetime
if not os.path.exists("C:\\TEST"):
    os.mkdir("C:\\TEST")
olay=datetime.datetime.now()
d3=olay.strftime("%d.%m.%Y %H:%M:%S")
dosya=open("C:\\TEST\\ask.txt",mode="w")
dosya.write(f"ZAMAN{' '*20} OLAY SIRASI{' '*10} RANDOM SAYI\n")
for i in range(1,10):
    sayi = random.randint(1, 100)
    if i<11:
        dosya.write(f"{d3} {' ' * 10}{i} {' ' * 20} {sayi}\n")
    else:
        dosya.write(f"{d3} {' ' * 10}{i} {' ' * 20} {sayi}\n")
