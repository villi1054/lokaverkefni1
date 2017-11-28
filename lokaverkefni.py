import random
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
        texti = input("Sláðu inn texta: ")
        for i in texti:
            if i == "g" or i == "G" or i == "k" or i == "K" or i == "n" or i == "N" or i == "r" or i == "R":
                print("<", end="")
            else:
                print(i, end="")
        print()
        mid = (len(texti)) // 2
        print(texti[:mid].capitalize())
        print(texti[mid:].capitalize())
    
    elif val == 5:
        listi = []
        for x in range(7):
           tolur = int(input("Sláðu inn tölu númer " + str(x+1) + ": "))
           listi.append(tolur)
        minnstaTala = min(listi)
        haestaTala = max(listi)
        summaTalna = sum(listi)
        medalTal = format(sum(listi)/len(listi),".2f")
        print("Minnsta talan er: " + str(minnstaTala))
        print("Hæsta talan er: " + str(haestaTala))
        print("Summa talnanna er: " + str(summaTalna))
        print("Meðaltal talnanna er: " + str(medalTal))
        
    elif val == 6:
        teningur = 1
        kast = 1
        while teningur == 1:
            t1 = random.randint(1,6)
            t2 = random.randint(1,6)
            summa = (t1 + t2)
            print("Kast númer " + str(kast))
            print("-------------")
            print("Fyrsti teningur er: " + str(t1))
            print("Annar teningur er: " + str(t2))
            print("Summan er: " + str(summa))
            if summa in {7,11}:
                print("----------------------")
                print("Leikmaður vinnur")
                teningur = teningur + 2
            elif summa in {2,3,12}:
                print("----------------------")
                print("Leikmaður tapar")
                teningur = teningur + 2
            elif summa in {4,5,6,8,9,10}:
                teningur = teningur + 1
            if teningur == 3:
                print("Takk fyrir að spila")
            print()
            while teningur == 2:
                stig = summa
                t3 = random.randint(1, 6)
                t4 = random.randint(1, 6)
                summa2 = (t3 + t4)
                kast = kast + 1
                print("Kast númer " + str(kast))
                print("-------------")
                print("Fyrsti teningur er: " + str(t3))
                print("Annar teningur er: " + str(t4))
                print("Summan er: " + str(summa2))
                if summa2 == stig:
                    print("----------------------")
                    print("Leikmaður vinnur")
                    teningur = teningur + 1
                elif summa2 == 7:
                    print("----------------------")
                    print("Leikmaður tapar")
                    teningur = teningur + 1
                if teningur == 3:
                    print("Takk fyrir að spila")
                print()
                
    elif val == 7:
        listi = []
        numer = 0
        numer += 1
        kast = 0
        for x in range(99):
            roll1 = random.randint(1, 6)
            roll2 = random.randint(1, 6)
            print("Kast teningur 1: ", roll1)
            print("Kast teningur 2: ", roll2)
            samtal = roll1+roll2
            print("Samtals ", str(samtal))
            numer += 1
            print("Þetta verður sett í listann sem kast: ", numer)

            listi.append(samtal)
            print(listi)
        print("Hérna er listinn þinn óraðaður.")
        print(listi)
        print("Hérna er listinn þinn raðaður.")
        print(sorted(listi))
        print("Summa listans")
        summa = sum(listi)
        print(sum(listi))
        print("Meðaltal listans er.")
        print( summa / numer)
        print("Hversu oft 7 kom fyrir í listanum.")
        print(listi.count(7))
        print("Hversu oft 3 kom fyrir í listanum.")
        print(listi.count(3))
        print("Hversu oft 12 kom fyrir í listanum.")
        print(listi.count(12))
        
    elif val == 9
        nafn = input("Hvað heitir notandinn? ")
        kyn = input("Hvaða kyn ertu (KK/KVK)? ")
        kg = int(input("Sláðu inn þyngd þína í kílóum: "))
        haed = float(input("Sláðu inn hæð þína í metrum: "))
        bmi = kg / (haed*haed)
        if bmi <= 18.5:
            print("BMI stuðull þinn er: " + format(bmi, ".2f"))
            print("Þú ert í vannæringu " + nafn.capitalize())
        if bmi > 18.5 and bmi < 25:
            print("BMI stuðull þinn er: " + format(bmi, ".2f"))
            print("Þú ert í kjörþyngd " + nafn.capitalize())
        if bmi > 25 and bmi < 30:
            print("BMI stuðull þinn er: " + format(bmi, ".2f"))
            print("Þú ert í ofþyngd " + nafn.capitalize())
        if bmi > 30:
            print("BMI stuðull þinn er: " + format(bmi, ".2f"))
            print("Þú ert í offitu " + nafn.capitalize())

    else:
        break
        print("Takk fyrir að nota forritið mitt! ")
