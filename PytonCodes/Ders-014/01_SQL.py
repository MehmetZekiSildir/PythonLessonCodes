### SQL ###
"""
SQL Yazılımları: MSSQL, MySQL, PL-SQL, SQLite, PostgreSQL, MongoDB, NOSQL

#### VERİ TİPLERİ ####
int => int
float => decimal(18,2): Ondalıklı kısım 2 basamak, toplam sayı 18 basamak
bool => bit

string => varchar(30): Latin alfabesini destekler. her karakter 1 bit yer tutar.
          nvarchar(30): Arapça,kiril alfabesi,çin alfabesi,vb ve latin alfabesini destekler. Her karakter 2 bit yer tutar.



"""

### MSSQL KULLANIMI
# import pypyodbc
# connection = pypyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-9IJKPL9\SQLDERS;DATABASE=Northwind;UID=sa;PWD=1')
# cursor = connection.cursor()

# cursor.execute("Create database okul")


# cursor.execute("SELECT * FROM Products")
# sonuc = cursor.fetchall()
# print(type(sonuc))
# for i in sonuc:
#     print(i)


# import sqlite3
# vt=sqlite3.connect("okul.db") # database varsa bağlanır yoksa oluşturup bağlanır.
#
# ## TABLO OLUŞTURMA ##
# cursor = vt.cursor()

# cursor.execute("Create table Ogrenci (Numara INTEGER,Ad varchar(20), Soyad varchar(20))")
# cursor.execute("Create table Ogrenci (Numara INTEGER PRIMARY KEY,Ad varchar(20), Soyad varchar(20))")
# cursor.execute("Create table if not exists Ogrenci (Numara INTEGER PRIMARY KEY AUTOINCREMENT,Ad varchar(20), Soyad varchar(20))")



## TABLOYA VERİ EKLEME ##
#*** Data Manipüle(Insert,Update,Delete) işlemi yapıldığında mutlaka commit() komutu ile değişiklikler aktarılmalıdır.
# cursor.execute("Insert into Ogrenci (Numara,Ad,Soyad) values (1,'Altan','Emre')")
# cursor.execute("Insert into Ogrenci  values (2,'Kübra','Kösmene')")
# vt.commit()


# cursor.execute("Insert into Ogrenci (Ad,Soyad)  values ('Altan','Emre')")
# cursor.execute("Insert into Ogrenci (Ad,Soyad)  values ('Kıvanç','Demirci')")



## TABLOYA VERİ GÜNCELLEME ##
# komut="Update Ogrenci set Ad='Yiğit' where Ad='Kübra'"

## TABLODAN VERİ SİLME ##
# komut="Delete from Ogrenci where Ad='Yiğit'"
# cursor.execute(komut)
# vt.commit()

### Kullanıcıdan 3 Ogrenci kaydı alınız.
"""
import sqlite3
vt=sqlite3.connect("okul.db")
cur=vt.cursor()
for i in range(3):
    ad = input("Ad:")
    soyad = input("Soyad:")
    try:
        # komut="Insert into Ogrenci (Ad,Soyad) values ('"+ad+"','"+soyad+"')"
        # cur.execute(komut)
        komut = "Insert into Ogrenci (Ad,Soyad) values (?,?)"
        cur.execute(komut,(ad,soyad))
        vt.commit()
    except:
        print("Veritabanı bağlantı hatası!!!")

vt.close()
"""

######### TABLODAN VERİ OKUMA (SELECT) ###########
# fetchall() : Tablodan okuma sonucunu liste olarak döndürür.
# fetchone() : Her çalışmadan bir satır döndürür.

# SELECT kolonad,kolonadı FROM TABLENAME WHERE filter
# SELECT * FROM TABLENAME ...=> * tabloda tanımlı sırayla bütün kolonları getirir.
"""
import sqlite3
vt=sqlite3.connect("okul.db")
cur=vt.cursor()
try:
    komut="Select * from Ogrenci"
    # komut="Select Ad,Soyad from Ogrenci"
    # komut="Select Soyad,Ad from Ogrenci"

    # komut="Select * from Ogrenci where Soyad='Demirci'"

    cur.execute(komut)
    ogrenciler=cur.fetchall()
    print(ogrenciler)
except:
    print("Veritabanı Bağlantı Hatası!!")

"""

"""
import sqlite3
vt=sqlite3.connect("okul.db")
cur=vt.cursor()
try:
    komut="Select * from Ogrenci "
    cur.execute(komut)
    while True:
        record=cur.fetchone()
        if record==None:
            break
        else:
            print(record)
except:
    print("Veritabanı Bağlantı Hatası!!")
"""

### TABLOYA ÇOKLU VERİ EKLEME ###
# ogrenciler=[(11, 'AliReza', 'Kutlu'), (12, 'Mahmut', 'Tuncer'), (13, 'Fatih', 'Erbakan')]
ogrenciler=[('Aydın', 'Kuş'), ('Yusuf', 'Tunay')]
import sqlite3
vt=sqlite3.connect("okul.db")
cur=vt.cursor()

# komut="Insert into Ogrenci values (?,?,?)"
komut="Insert into Ogrenci (Ad,Soyad) values (?,?)"
cur.executemany(komut,ogrenciler)
vt.commit()
vt.close()







