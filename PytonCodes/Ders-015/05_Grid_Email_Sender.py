### SMTP (Simple Mail Transfer Protocol) ###
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def Postala():
    eposta=MIMEMultipart() # class örnek alma işlemi - instance
    eposta["From"]="test_altan_emre_1989@hotmail.com"
    eposta["To"]=str(txt_alici.get())
    eposta["Subject"]=str(txt_konu.get())
    body=txt_email.get("1.0",END)
    body_text=MIMEText(body,"plain")
    eposta.attach(body_text)

    try:
        hotmail=smtplib.SMTP("smtp-mail.outlook.com",587) #Gmail SMTP bilgileri
        hotmail.ehlo()
        hotmail.starttls()
        hotmail.login("test_altan_emre_1989@hotmail.com","UBY12345") #gönderici maili
        hotmail.sendmail(eposta["From"],eposta["To"],eposta.as_string())
        messagebox.showinfo("Bilgi","Email Gönderildi.")
        hotmail.close()
    except:
        messagebox.showerror("HATA","EMail Gönderilemedi.")

from tkinter import *
from tkinter import messagebox


pencere=Tk()
pencere.title("EMail")
pencere.geometry("1024x768+415+100")

lbl_alici=Label(pencere,text="Alıcı Email Adresi:",font=("Consolas",16))
txt_alici=Entry(pencere,text="",font=("Consolas",16),width=60)

lbl_alici.grid(row=0,column=0,padx=10,pady=10)
txt_alici.grid(row=0,column=1,padx=10,pady=10)

lbl_konu=Label(pencere,text="Konu:",font=("Consolas",16))
txt_konu=Entry(pencere,text="",font=("Consolas",16),width=60)

lbl_konu.grid(row=1,column=0,padx=10,pady=10)
txt_konu.grid(row=1,column=1,padx=10,pady=10)


lbl_email=Label(pencere,text="EMail:",font=("Consolas",16))
txt_email=Text(pencere,font=("Consolas",16),width=60)

lbl_email.grid(row=2,column=0,padx=10,pady=10)
txt_email.grid(row=2,column=1,padx=10,pady=10)

btn_gonder=Button(pencere,text="Gönder",font=("Consolas",16),command=Postala)
btn_gonder.grid(row=3,column=1,padx=10,pady=10,sticky=W+E+N+S)

pencere.mainloop()
