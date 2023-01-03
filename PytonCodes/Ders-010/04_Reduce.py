##### REDUCE() #####

## Kullanmak için import edilmesi gereklidir.

# from functools import reduce
"""
Reduce fonksiyonu,döngüye sokabileceğiniz herhangi bir veri tipi içinde, veri tipinin içindeki bütün elemanları azaltarak dolaşan ve karşılaştırma yapmaya imkan tanıyan bir yapıdır.
"""



##ÖRNEK:
numbers=[11,3,9,12,2,15,66,19]
# bu listenin içindeki değerleri sırayla karşılaştırarak en büyük değeri bulan function yazınız.

def findMax(a,b):
    if a>b:
        return a
    return b

# for i in range(len(numbers)):
#     print(findMax(numbers[i],numbers[i+1]))

from functools import reduce

# print(reduce(findMax,numbers))

# findMax(11,3) #11
# findMax(11,9) #11
# findMax(11,12) #12
# findMax(12,2) #12
# .....

# print(reduce(lambda x,y: (x,y),range(1,6)))


def faktoriyel(s1,s2):
    return s1*s2

print(reduce(faktoriyel,range(1,6)))
















