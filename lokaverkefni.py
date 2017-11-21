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
        heiltala = 1
        while heiltala != 0:
            heiltala = int(input("Sláðu inn heiltölu: "))
            if heiltala != 0:
                summa = 0
                if heiltala > 0:
                    for x in range(1, heiltala + 1):
                        summa += x
                        if x == heiltala:
                            print(x, end="")
                        else:
                            print(str(x) + " + ", end="")
                    print(" = " + str(summa))
        
                if heiltala < 0:
                    for x in range(heiltala, 0, 1):
                        summa += x
                        if x == -1:
                            print("(" + str(x) + ")", end="")
                        else:
                            print("(" + str(x) + ") + ", end="")
                    print(" = " + str(summa))
        # end of while
        print()
        print("Takk fyrir að nota forritið mitt")
    elif val == 3:
        from random import randint
# create a list of play options
t = ["Steinn", "Blað", "Skæri"]
# assign a random play to the computer
computer = t[randint(0, 2)]
# set player to False
notandi_vann = 0
notandi_vann += 1

talva_vann = 0
talva_vann += 1

jafntefli = 0
jafntefli += 1

spilanir = 0
spilanir += 1

player = False
print("Reglurnar:")
print("Skæri vinnur blað")
print("Steinn vinnur skæri")
print("Blað vinnur steinn")
print("'Hætta' til að hætta")
print("Sláðu inn 'Skæri', 'Blað', eða 'Steinn' til að byrja ")
nafn = input("Hvað heitir þú ?. ")
aldur = int(input("Sláðu inn aldur þinn? "))
while player == False:
    # set player to True
    spilanir += 1
    player = input("Skæri, Blað, Steinn")
    if player == computer:
        print("Jafntefli!")
        jafntefli += 1
    elif player == "Steinn":
        teljari2 = 0
        teljari2 += 1
        if computer == "Blað":
            print("Þú tapar!", computer, "vinnur", player)
            talva_vann += 1
        else:
            print("Þú vinnur!", player, "vinnur", computer)
            notandi_vann += 1
    elif player == "Blað":
        if computer == "Skæri":
            print("Þú tapar!", computer, "sker", player)
            talva_vann += 1
        else:
            print("Þú vinnur!", player, "vinnur", computer)
            notandi_vann += 1
    elif player == "Skæri":
        if computer == "Steinn!":
            print("Þú tapar....", computer, "vinnur", player)
            talva_vann += 1
        else:
            print("Þú vinnur!", player, "sker", computer)
            notandi_vann += 1
    elif player == "Hætta":
        print("Þú vannst "+ str(notandi_vann) +" Sinnum.")
        print("Talvan vann þig ", str(talva_vann), " sinni.")
        print("Þið kom upp jafntefli", str(jafntefli), " sinnum.")
        print("Leikurinn var spilaður", str(spilanir), " sinnum.")
        print(str(nafn),",aldur", str(aldur))
        break
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
