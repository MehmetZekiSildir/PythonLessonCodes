from datetime import datetime
import random
today = datetime.now()

date = today.strftime("%d-%m-%Y--%H:%M:%S--%A")

try:
    dosya = open("file.txt", "w")
    dosya.write(f"ZAMAN {' ' * 23}OLAY SIRASI {' ' * 10}RASTGELE SAYI\n")
    for i in range(1, 11):
        randomke = random.randint(1, 101)
        dosya.write(f"{date}    |      {i}        |        {randomke}    \n")
    dosya.close()
except:
    print("calismadi yigidim")




