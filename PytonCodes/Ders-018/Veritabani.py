import sqlite3
# vt=sqlite3.connect("PyPara.db")
# cursor=vt.cursor()

# komut="""Create table tb_altin(
# id INTEGER NOT NULL UNIQUE,
# zaman NVARCHAR(100) NOT NULL,
# kur REAL NOT NULL,
# PRIMARY KEY(id AUTOINCREMENT)
# )"""

# komut="""Create table tb_dolar(
# id INTEGER NOT NULL UNIQUE,
# zaman NVARCHAR(100) NOT NULL,
# kur REAL NOT NULL,
# PRIMARY KEY(id AUTOINCREMENT)
# )"""

# komut="""Create table tb_euro(
# id INTEGER NOT NULL UNIQUE,
# zaman NVARCHAR(100) NOT NULL,
# kur REAL NOT NULL,
# PRIMARY KEY(id AUTOINCREMENT)
# )"""

# cursor.execute(komut)
#
# vt.close()


class VeriTabani:
    @staticmethod
    def Kaydet(komut):
        vt=sqlite3.connect("PyPara.db")
        try:
            cur=vt.cursor()
            cur.execute(komut)
            vt.commit()
            print("KAYIT BAŞARILI")
        except:
            print("KAYIT BAŞARISIZ!!!")

        finally:
            vt.close()
    @staticmethod
    def KurGetir(komut):
        vt=sqlite3.connect("PyPara.db")
        try:
            cur=vt.cursor()
            cur.execute(komut)
            kurListe=cur.fetchall()
            # kurListe.reverse()
        except:
            print("KUR GETİRME HATASI!!!")
        finally:
            vt.close()
        return kurListe




