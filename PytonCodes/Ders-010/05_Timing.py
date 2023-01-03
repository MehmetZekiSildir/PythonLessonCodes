import time
import random

baslangic=time.time() # baslangıç zamanından programın run ettiğimizde zamana kadar geçen saniye bilgisine verecek
# print(baslangic)

dd1=random.sample(range(0,5000000),5000000)
cifts=list()
for item in dd1:
    if item%2==0:
        cifts.append(item)

# print(cifts)
# print(len(cifts))
bitis=time.time()
print("For : {}".format(bitis-baslangic))
# print(f"For : {bitis-baslangic}")
# print("For : ",bitis-baslangic)

###############################################

baslangic1=time.time() # baslangıç zamanından programın run ettiğimizde zamana kadar geçen saniye bilgisine verecek
# print(baslangic)

dd2=random.sample(range(0,5000000),5000000)
ciftler=list(filter(lambda x: x%2==0,dd2))

bitis1=time.time()
print("Filter : {}".format(bitis1-baslangic1))

###############################################

baslangic2=time.time() # baslangıç zamanından programın run ettiğimizde zamana kadar geçen saniye bilgisine verecek
# print(baslangic)

dd3=random.sample(range(0,5000000),5000000)
sonCift=[x for x in dd3 if x%2==0]

bitis2=time.time()
print("For-OneLine : {}".format(bitis2-baslangic2))






