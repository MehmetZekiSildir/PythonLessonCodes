sinf1=[78,65,57,93,54]
sinf2=[59,85,72,67,56]
sinf3=[49,93,86,51,66]
sinf4=[62,61,74,85,70]

toplam1 = 0
for i in sinf1:
    toplam1+=i
    ogrenci_sayi=len(sinf1)
ortalama1=toplam1/ogrenci_sayi

toplam2 = 0
for i in sinf2:
    toplam2+=i
    ogrenci_sayi=len(sinf2)
ortalama2=toplam2/ogrenci_sayi

toplam3 = 0
for i in sinf3:
    toplam3+=i
    ogrenci_sayi=len(sinf3)
ortalama3=toplam3/ogrenci_sayi

toplam4 = 0
for i in sinf4:
    toplam4+=i
    ogrenci_sayi=len(sinf4)
ortalama4=toplam4/ogrenci_sayi

print("        **SINF PUAN ORTALAMASI**")
print(f"""-----------------------------------------   
    11'A sınf puanı ortalaması : {ortalama1}
    11'B sınf puanı ortalaması : {ortalama2}
    11'C sınf puanı ortalaması : {ortalama3}
    11'D sınf puanı ortalaması : {ortalama4}
          """)
print("        **SINF PUAN SIRALAMASI**")
print("-----------------------------------------")
if ortalama4 > ortalama1 and ortalama2 and ortalama3:
    print(f"     1'yeri {ortalama4} puanla 11'D kazandı") # 4 çıktı
    if ortalama1 > ortalama2 and ortalama3:
        print(f"     2'yeri {ortalama1} puanla 11'A kazandı")
        if ortalama2 > ortalama3:
            print(f"     3'yeri {ortalama2} puanla 11'B kazandı")
            print(f"     4'yeri {ortalama3} puanla 11'C kazandı")
        elif ortalama3 > ortalama2:
            print(f"     3'yeri {ortalama3} puanla 11'C kazandı")
            print(f"     4'yeri {ortalama2} puanla 11'B kazandı")
    elif ortalama2 > ortalama1 and ortalama3:
        print(f"     2'yeri {ortalama2} puanla 11'B kazandı")
        if ortalama1 > ortalama3:
            print(f"     3'yeri {ortalama1} puanla 11'A kazandı")
            print(f"     4'yeri {ortalama3} puanla 11'C kazandı")
        elif ortalama3 > ortalama1:
            print(f"     3'yeri {ortalama3} puanla 11'C kazandı")
            print(f"     4'yeri {ortalama1} puanla 11'A kazandı")
    elif ortalama3 > ortalama1 and ortalama2:
        print(f"     2'yeri {ortalama3} puanla 11'C kazandı")
        if ortalama1 > ortalama2:
            print(f"     3'yeri {ortalama1} puanla 11'A kazandı")
            print(f"     4'yeri {ortalama2} puanla 11'B kazandı")
        elif ortalama2 > ortalama1:
            print(f"     3'yeri {ortalama2} puanla 11'B kazandı")
            print(f"     4'yeri {ortalama1} puanla 11'A kazandı")

elif ortalama1 > ortalama2 and ortalama3 and ortalama4:
    print(f"     1'yeri {ortalama1} puanla 11'A kazandı")  # 1 çıktı
    if ortalama2 > ortalama3 and ortalama4:
        print(f"     2'yeri {ortalama2} puanla 11'B kazandı") # 2 çıktı
        if ortalama3 > ortalama4:
            print(f"     3'yeri {ortalama3} puanla 11'C kazandı")
            print(f"     4'yeri {ortalama4} puanla 11'D kazandı")
        elif ortalama4 > ortalama3:
            print(f"     3'yeri {ortalama4} puanla 11'D kazandı")
            print(f"     4'yeri {ortalama3} puanla 11'C kazandı")
    elif ortalama3 > ortalama2 and ortalama4:
        print(f"     2'yeri {ortalama3} puanla 11'C kazandı")
        if ortalama2 > ortalama4:
            print(f"     3'yeri {ortalama2} puanla 11'B kazandı")
            print(f"     4'yeri {ortalama4} puanla 11'D kazandı")
        elif ortalama4 > ortalama2:
            print(f"     3'yeri {ortalama4} puanla 11'D kazandı")
            print(f"     4'yeri {ortalama2} puanla 11'B kazandı")
    elif ortalama4 > ortalama2 and ortalama3:
        print(f"     2'yeri {ortalama4} puanla 11'D kazandı")
        if ortalama2 > ortalama3:
            print(f"     3'yeri {ortalama2} puanla 11'B kazandı")
            print(f"     4'yeri {ortalama3} puanla 11'C kazandı")
        elif ortalama3 > ortalama2:
            print(f"     3'yeri {ortalama3} puanla 11'C kazandı")
            print(f"     4'yeri {ortalama2} puanla 11'B kazandı")
elif ortalama2 > ortalama1 and ortalama3 and ortalama4:
    print(f"    1'yeri {ortalama2} puanla 11'B kazandı")
    if ortalama1 > ortalama3 and ortalama4:
        print(f"    2'yeri {ortalama1} puanla 11'A kazandı")
        if ortalama3 > ortalama4:
            print(f"    3'yeri {ortalama3} puanla 11'C kazandı")
            print(f"    4'yeri {ortalama4} puanla 11'D kazandı")
        elif ortalama4 > ortalama3:
            print(f"    3'yeri {ortalama4} puanla 11'D kazandı")
            print(f"    4'yeri {ortalama3} puanla 11'C kazandı")
    elif ortalama3 > ortalama1 and ortalama4:
        print(f"    2'yeri {ortalama3} puanla 11'C kazandı")
        if ortalama1 > ortalama4:
            print(f"    3'yeri {ortalama1} puanla 11'A kazandı")
            print(f"    4'yeri {ortalama4} puanla 11'D kazandı")
        elif ortalama4 > ortalama1:
            print(f"     3'yeri {ortalama4} puanla 11'D kazandı")
            print(f"     4'yeri {ortalama1} puanla 11'A kazandı")
    elif ortalama4 > ortalama1 and ortalama3:
        print(f"    2'yeri {ortalama4} puanla 11'D kazandı")
        if ortalama3 > ortalama1:
            print(f"    3'yeri {ortalama3} puanla 11'C kazandı")
            print(f"    4'yeri {ortalama1} puanla 11'A kazandı")
        elif ortalama1 > ortalama3:
            print(f"    3'yeri {ortalama1} puanla 11'A kazandı")
            print(f"    4'yeri {ortalama3} puanla 11'C kazandı")
elif ortalama3 > ortalama1 and ortalama2 and ortalama4:
    print(f"    1'yeri {ortalama3} puanla 11'C kazandı")
    if ortalama1 > ortalama2 and ortalama4:
        print(f"    2'yeri {ortalama1} puanla 11'A kazandı")
        if ortalama3 > ortalama1:
            print(f"     3'yeri {ortalama3} puanla 11'C kazandı")
            print(f"     4'yeri {ortalama1} puanla 11'A kazandı")
        elif ortalama1 > ortalama3:
            print(f"     3'yeri {ortalama1} puanla 11'A kazandı")
            print(f"     4'yeri {ortalama3} puanla 11'C kazandı")
    elif ortalama2 > ortalama1 and ortalama4:
        print(f"    2'yeri {ortalama2} puanla 11'B kazandı")
        if ortalama1 > ortalama4:
            print(f"    3'yeri {ortalama1} puanla 11'A kazandı")
            print(f"    4'yeri {ortalama4} puanla 11'D kazandı")
        elif ortalama4 > ortalama1:
            print(f"     3'yeri {ortalama4} puanla 11'D kazandı")
            print(f"     4'yeri {ortalama1} puanla 11'A kazandı")
    elif ortalama4 > ortalama1 and ortalama2:
        print(f"    2'yeri {ortalama4} puanla 11'D kazandı")
        if ortalama1 > ortalama2:
            print(f"     3'yeri {ortalama1} puanla 11'A kazandı")
            print(f"    4'yeri {ortalama2} puanla 11'B kazandı")
        elif ortalama2 > ortalama1:
            print(f"     3'yeri {ortalama2} puanla 11'B kazandı")
            print(f"     4'yeri {ortalama1} puanla 11'A kazandı")
# elif ortalama4 > ortalama1 and ortalama2 and ortalama3:
#     print(f" 1'yeri {ortalama4} puanla 11'D kazandı") # 4 çıktı
#     if ortalama1 > ortalama2 and ortalama3:
#         print(f" 2'yeri {ortalama1} puanla 11'A kazandı")
#         if ortalama2 > ortalama3:
#             print(f" 3'yeri {ortalama2} puanla 11'B kazandı")
#             print(f" 4'yeri {ortalama3} puanla 11'C kazandı")
#         elif ortalama3 > ortalama2:
#             print(f" 3'yeri {ortalama3} puanla 11'C kazandı")
#             print(f" 4'yeri {ortalama2} puanla 11'B kazandı")
#     elif ortalama2 > ortalama1 and ortalama3:
#         print(f" 2'yeri {ortalama2} puanla 11'B kazandı")
#         if ortalama1 > ortalama3:
#             print(f" 3'yeri {ortalama1} puanla 11'A kazandı")
#             print(f" 4'yeri {ortalama3} puanla 11'C kazandı")
#         elif ortalama3 > ortalama1:
#             print(f" 3'yeri {ortalama3} puanla 11'C kazandı")
#             print(f" 4'yeri {ortalama1} puanla 11'A kazandı")
#     elif ortalama3 > ortalama1 and ortalama2:
#         print(f" 2'yeri {ortalama3} puanla 11'C kazandı")
#         if ortalama1 > ortalama2:
#             print(f" 3'yeri {ortalama1} puanla 11'A kazandı")
#             print(f" 4'yeri {ortalama2} puanla 11'B kazandı")
#         elif ortalama2 > ortalama1:
#             print(f" 3'yeri {ortalama2} puanla 11'B kazandı")
#             print(f" 4'yeri {ortalama1} puanla 11'A kazandı")





