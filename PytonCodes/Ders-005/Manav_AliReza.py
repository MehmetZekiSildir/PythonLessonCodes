print("""....Welcome o he the GREENGROCER....
#**************
 #(1) Fruit
 #(2)Vegtable
 #(3)exit fruit 
 #(4)exit vegtable
 #(5)exit
    """)
fruit = []
vegtable = []
total = 0
totalV = 0

i = 0
while i < 6:
    select = int(input("Please chose one of the option please:"))
    if (select == 1):
        chooseFruit = input("enter the fruit that you wnat:")
        if chooseFruit in fruit:
            print("choosen product is already in the list.")
        else:
            kg = int(input("enter the amount that you need: "))
            total += kg
            if total > 10 or kg > 10:
                print("the amount is not available.")
                continue
    elif (select == 2):
        chooseVegtable = input("enter the vegtable that you wnat:")
        if chooseVegtable in fruit:
            print("choosen product is already in the list.")
        else:
            kgV = int(input("enter the amount that you need: "))
            totalV += kgV
            if totalV > 10 or kgV > 10:
                print("the amount is not available.")
                continue
    elif (select == 3):
        print(f"the products has bought: \n {total} kg {chooseFruit}")
    elif (select == 4):
        print(f"the products has bought: \n  {totalV}kg {chooseVegtable}")
    elif (select == 5):
        print(f"the products has bought: \n {total}kg {chooseFruit} , {totalV} kg {chooseVegtable} ")
        break
    else:
        print("wrong selection, please try again")