class Matematik:
    @classmethod
    def Topla(cls,*numbers):
        sum=0
        for n in numbers:
            sum+=n
        print(sum)

    @classmethod
    def Cikar(cls, s1,s2):
        print(s1-s2)

    @classmethod
    def Carp(cls, *numbers):
        crp = 1
        for n in numbers:
            crp *= n
        print(crp)

    @classmethod
    def Bol(cls, s1, s2):
        try:
            print(s1/s2)
        except ZeroDivisionError:
            print("Sıfıra Bölme Hatası")