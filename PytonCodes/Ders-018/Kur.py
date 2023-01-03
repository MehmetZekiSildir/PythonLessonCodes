from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from Veritabani import VeriTabani

class Kur:
    @staticmethod
    def Getir(doviztipi):
        opsiyonlar=Options()
        opsiyonlar.add_argument("--headless")
        browser=webdriver.Chrome(executable_path="chromedriver.exe", options=opsiyonlar)
        browser.get("https://www.haberturk.com/")
        if(doviztipi=="altin"):
            icerik=browser.find_element_by_css_selector("#gram-altin span:nth-child(2)").text
        elif(doviztipi=="dolar"):
            icerik=browser.find_element_by_css_selector("#dolar span:nth-child(2)").text
        elif (doviztipi == "euro"):
            icerik=browser.find_element_by_css_selector("#euro span:nth-child(2)").text

        deger=float(icerik.replace(",","."))
        tablo="tb_"+doviztipi
        zaman=datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        print(zaman)
        komut=f"Insert into {tablo} (zaman,kur) values ('{zaman}','{deger}')"
        VeriTabani.Kaydet(komut)









