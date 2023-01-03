### ÖDEV: 1-100 arası üretilen 10 adet rastgele sayıyı Rastgele.txt isimli dosyaya aşağıdaki formatla yazdırınız.
"""
    ZAMAN                       OLAYSIRASI          RASTGELESAYI
    25.05.2020 21:38:35.213         1                    23
    25.05.2020 21:38:35.213         2                    34
    25.05.2020 21:38:35.213         3                    2
    25.05.2020 21:38:35.213         4                    65
    25.05.2020 21:38:35.213         5                    87
    ...........
    ...........
    ...........

"""
from datetime import datetime
import os, random
date = datetime.now().strftime("%d.%m.%Y  %H:%M:%S.")

if not os.path.exists("C:\\TEST"):
    os.mkdir("C:\\TEST")
dosya = open(f"C:\\TEST\\Rastgele.txt","w")
for i in range(1, 11):
    rastgele = random.randint(1, 100)
    dosya.write(f"{date}\t\t{i}\t\t{rastgele}.\n")
dosya.close()

