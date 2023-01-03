# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# driver_path="chromedriver.exe"
#
# opsiyonlar=Options()
# opsiyonlar.add_argument("--headless") # Veri çekme işlemini arkaplanda yapar.
#
# ## tarayı tanımlama
# browser = webdriver.Chrome(executable_path=driver_path,options=opsiyonlar)
# browser.get("https://www.haberturk.com/")
#
# icerik = browser.find_element_by_id("dolar").text
# print(icerik)
# parcalar=icerik.split("\n")
# print(parcalar[0],"=>",parcalar[1])


### DOLAR => EURO

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def KurGetir(doviz):
    opsiyonlar = Options()
    opsiyonlar.add_argument("--headless") # Veri çekme işlemini arkaplanda yapar.

    ## tarayı tanımlama
    browser = webdriver.Chrome(executable_path="chromedriver.exe",options=opsiyonlar)
    browser.get("https://www.haberturk.com/")

    icerik = browser.find_element_by_id(doviz).text
    parcalar=icerik.split("\n")
    return float(parcalar[1].replace(",","."))


miktar=int(input("Kaç dolar euro ya döndürülecek? "))

lira=KurGetir("dolar")*miktar

euro=lira/KurGetir("euro")
print(euro)