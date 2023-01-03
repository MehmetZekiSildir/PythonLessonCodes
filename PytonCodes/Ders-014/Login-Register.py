class User:
    def __init__(self):
        self.Id=0
        self.Name=""
        self.Surname=""
        self.__Email=""
        self.__Username=""
        self.__Password=""
        User.DBCreate()

    @staticmethod
    def DBCreate():
        import sqlite3
        vt = sqlite3.connect("projects.db")
        cur = vt.cursor()
        cur.execute("""Create table if not exists Users 
        (Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Name varchar(30),
        Surname varchar(30),
        Email varchar(200),
        Username varchar(20),
        Password varchar(6)
        )""")
        vt.close()

    def Save(self):
        self.Name=input("Name:")
        self.Surname=input("Surname:")
        email=self.setEmailControl()
        while email==False:
            email=self.setEmailControl()
        self.__Email=email
        username = self.setUsernameControl()
        while username == False:
            username=self.setUsernameControl()
        self.__Username=username
        self.setPasswordControl()
        import sqlite3
        vt = sqlite3.connect("projects.db")
        cur = vt.cursor()
        komut="Insert into Users (Name,Surname,Email,Username,Password) values(?,?,?,?,?)"
        cur.execute(komut,(self.Name,self.Surname,self.__Email,self.__Username,self.__Password))
        vt.commit()
        vt.close()
    #region Controls
    def setPasswordControl(self):
        password=input("Password:")
        if len(password)==6 and password.isalnum():
            self.__Password=password
        else:
            print("Password uzunluğu 6 olmalıdır ve özel karakter barındıramaz.")
            self.setPasswordControl() #recursive Method

    def getPassword(self):
        return self.__Password

    @staticmethod
    def setEmailControl():
        email=input("Email:")
        import sqlite3
        vt=sqlite3.connect("projects.db")
        cur=vt.cursor()
        cur.execute("Select Email from Users where Email='"+email+"'")

        if cur.fetchone()!=None:
            print("Kayıtlı Email Adresi!!")
            return False
        else:
            return email

    @staticmethod
    def setUsernameControl():
        Username = input("Username:")
        import sqlite3
        vt = sqlite3.connect("projects.db")
        cur = vt.cursor()
        cur.execute("Select Username from Users where Username='" + Username + "'")
        if cur.fetchone()!=None:
            print("Kayıtlı Username!!")
            return False
        else:
            return Username
    #endregion
    @classmethod
    def Login(cls):
        username=input("Username:")
        password=input("Password:")

        import sqlite3
        vt=sqlite3.connect("projects.db")
        cur=vt.cursor()
        cur.execute("Select * from Users where Username='"+username+"' and Password='"+password+"'") # checker => Username and password
        userList=cur.fetchall()
        if len(userList)==1:
            u=User()
            u.Id=userList[0][0]
            u.Name=userList[0][1]
            u.Surname=userList[0][2]
            u.__Email=userList[0][3]
            u.__Username=userList[0][4]
            u.__Password=userList[0][5]
            return u
        else:
            print("Giriş Başarısız!!")
            return False


user=User()
# user.Save()
user=User.Login()
print(user.Name)