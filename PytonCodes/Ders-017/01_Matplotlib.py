import matplotlib.pyplot as plt

# plt.xkcd()

print(plt.style.available)

### Hazır stil kullanımı
# plt.style.use('bmh')
# plt.style.use('classic')
plt.style.use('dark_background')

x_ekseni=[1,2,3,4,5]
y_AliReza=[45,55,65,63,120]
y_Gulu=[10,25,35,40,45]
y_Altan=[65,85,95,105,145]

plt.title("Yas-Boy Tablosu")
plt.xlabel("Yaşlar")
plt.ylabel("Boylar")



## El ile stil verme
# plt.plot(x_ekseni,y_AliReza,color="b",linestyle="--",marker="x",label="AliReza")
# plt.plot(x_ekseni,y_Gulu,"ko-",label="Gulu")
# plt.plot(x_ekseni,y_Altan,color="#f54245",linestyle="-.",marker=".",label="ALTAN")


# otomatik stil kullanımı
plt.plot(x_ekseni,y_AliReza,label="Ali")
plt.plot(x_ekseni,y_Gulu,label="Gulu")
plt.plot(x_ekseni,y_Altan,label="ALTAN")


# plt.bar(x_ekseni,y_Altan,label="ALTAN")
# plt.bar(x_ekseni,y_AliReza,label="Ali")
# plt.bar(x_ekseni,y_Gulu,label="Gulu")



plt.legend()
plt.tight_layout()
plt.grid(True)
plt.show()