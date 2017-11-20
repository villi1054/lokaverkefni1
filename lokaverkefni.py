'''
20.11.17
Lokaverkefni
'''

#Daemi 1:
val = -1
while val !=0:
    print("1. Bílar")
    print("2. Samlagning")
    print("3. Skæri, blað, steinn")
    print("4. Strengur")
    print("5. Heilltölur")
    print("6. Teningaspilið craps")
    print("7. Teningakast")
    print("8. Byggingarupplýsingar úr Hópverkefni 1")
    print("9. Þyngdarstuðull")
    print("10. Hætta")

    val = int(input("Hvað má bjóða þér að gera? Veldu númer úr valmynd. "))
    #Þá get ég farið að vinna í hvaða lið fyrir sig með if, elif else,
    if val == 1:
        fjoldi = int(input("Hvað eru margir skráðir í ferðina?: "))
        if fjoldi > 4:
            bilar = fjoldi // 5
            sidasti_bill = fjoldi % 5
            if fjoldi % 5 != 0:
                bilar = bilar + 1
            print("Fjöldi bíla sem þarf: " + str(bilar))
            print("Fjöldi í síðasta bílnum: " + str(sidasti_bill))
        else:
            print("Því miður eru ekki nógu margir skráðir, hætt er við ferðina.")
    elif val == 2:
        print("Tölur sem að ganga upp í 7 en ekki 5 ▼▼▼▼")
        nl = []
        for x in range(1500, 2700):
            if (x % 7 == 0) and (x % 5 == 0):
                nl.append(str(x))
        print(','.join(nl))
    elif val == 3:
from random import randint
# Búa til lista af valmöguleikum
t = ["Steinn", "Blað", "Skæri"]
# assign a random play to the computer
computer = t[randint(0, 2)]
# set player to False
player = False

while player == False:
    # set player to True
    player = input("Steinn, Blað, Skæri, 'Hætta' til að hætta")
    if player == computer:
        print("Jafntefli!")
    elif player == "Steinn":
        teljari2 = 0
        teljari2 += 1
        if computer == "Blað":
            print("Þú tapar", computer, "vinnur", player)
        else:
            print("Þú vinnur", player, "vinnur", computer)
    elif player == "Blað":
        if computer == "Skæri":
            print("Þú tapar!", computer, "sker", player)
        else:
            print("Þú vinnur!", player, "vinnur", computer)
    elif player == "Skæri":
        if computer == "Steinn":
            print("Þú tapar....", computer, "vinnur", player)
        else:
            print("Þú vinnur!", player, "sker", computer)
    elif player == "Hætta":
        print("Þú vannst "+ teljari2 +"oft")
    else:
        print("Villa í innslátti! Sláðu inn annaðhvort Skæri, Blað eða Steinn")
    # player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0, 2)]
    elif val == 4:
        lengd1 = 7
        lengd2 = 6
        listi1 = []
        listi2 = []
        while len(listi1) < lengd1:
            inslattur = input("Sláðu inn 7 orð. ")
            listi1.append(inslattur)
            print(listi1)
        while len(listi2) < lengd2:
            inslattur1 = input("Sláðu inn 6 orð.")
            listi2.append(inslattur1)
            print(listi2)
        for item in listi1:
            if item in listi2:
                print("Þetta orð er í báðum listum "+item)
    
    elif val == 5:
        print("Takk fyrir að nota forritið mitt ")
        break
    else:
        break
        print("Takk fyrir að nota forritið mitt! ")
