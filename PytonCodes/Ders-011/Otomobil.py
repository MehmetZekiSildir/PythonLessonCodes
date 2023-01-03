class Otomobil:
    def __init__(self):
        self.Marka = input("Marka giriniz: ")
        self.Model = input("Model giriniz: ")
        self.Renk = input("Rengini giriniz: ")
        self.MotorHacmi = input("Motor Hacmini giriniz: ")
        self.UretimYili = input("Üretim Yılını giriniz: ")
        self.Kaydet()

    def Kaydet(self):
        from datetime import datetime
        tarih = datetime.now().date()
        tarih = tarih.strftime("%d_%m_%Y")
        dosya = open("OTO_"+str(tarih)+".txt", "w",encoding="utf8")
        dosya.write("MARKA\t\tMODEL\t\tRENK\t\tMOTOR HACMİ\t\tÜRETİM YILI\n")
        dosya.write(f"{self.Marka}\t\t{self.Model}\t\t{self.Renk}\t\t{self.MotorHacmi}\t\t{self.UretimYili}\n\t")
