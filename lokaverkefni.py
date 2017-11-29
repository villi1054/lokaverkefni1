import random

'''
20.11.17
Lokaverkefni
'''

# Valmynd
val = -1
while val != 0:
    print("1. Bílar")
    print("2. Samlagning")
    print("3. Skæri, blað, steinn")
    print("4. Strengur")
    print("5. Heiltölur")
    print("6. Teningaspilið Craps")
    print("7. Teningakast")
    print("8. Byggingarupplýsingar úr Hópverkefni 1")
    print("9. Þyngdarstuðull")
    print("10. Hætta")

    val = int(input("Hvað má bjóða þér að gera? Veldu númer úr valmynd. "))
    # Þá get ég farið að vinna í hvaða lið fyrir sig með if, elif else,

    if val == 1:
        # Fá inntak um fjölda manneskja
        fjoldi = int(input("Hvað eru margir skráðir í ferðina?: "))
        # Forritið keyrir ekki nema innsláttur sé meira en 4
        if fjoldi > 4:
            bilar = fjoldi // 5
            sidasti_bill = fjoldi % 5
            # Ef það eru einhverjir í siðasta bíl þá bæta +1 við fjölda bíla
            if fjoldi % 5 != 0:
                bilar = bilar + 1
            print("Fjöldi bíla sem þarf: " + str(bilar))
            print("Fjöldi í síðasta bílnum: " + str(sidasti_bill))
            print()
        else:
            print("Því miður eru ekki nógu margir skráðir, hætt er við ferðina.")
            print()

    elif val == 2:
        # búa til variable
        heiltala = 1
        # while lykkja svo að forritið keyrir þangað til að innsláttur sé 0
        while heiltala != 0:
            heiltala = int(input("Sláðu inn heiltölu: "))
            if heiltala != 0:
                summa = 0
                if heiltala > 0:
                    # ef talan er ekki mínustala þá fer það upp
                    for x in range(1, heiltala + 1):
                        summa += x
                        if x == heiltala:
                            print(x, end="")
                        else:
                            print(str(x) + " + ", end="")
                    print(" = " + str(summa))
                # ef tala er mínustala þá fer það niður
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
        print()

    elif val == 3:
        from random import randint

        # create a list of play options
        t = ["Steinn", "Blað", "Skæri"]
        # assign a random play to the computer
        computer = t[randint(0, 2)]
        # set player to False
        notandi_vann = 0

        talva_vann = 0

        jafntefli = 0

        spilanir = 0

        player = False
        print("Reglurnar:")
        print("Skæri vinnur blað")
        print("Steinn vinnur skæri")
        print("Blað vinnur steinn")
        print("'Hætta' til að hætta")
        nafn = input("Hvað heitir þú ?. ")
        aldur = int(input("Sláðu inn aldur þinn? "))
        while player == False:
            # búa til while lykkju fyrir spilið svo að það haldi áfram þangað til að hætt er.
            spilanir += 1
            # set player to True
            player = input("Skæri, Blað, Steinn eða Hætta: ").capitalize()
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
                if computer == "Steinn":
                    print("Þú tapar!", computer, "vinnur", player)
                    talva_vann += 1
                else:
                    print("Þú vinnur!", player, "sker", computer)
                    notandi_vann += 1
            # end of while þegar hætt er
            elif player == "Hætta":
                print("Þú vannst " + str(notandi_vann) + " sinnum.")
                print("Talvan vann þig ", str(talva_vann), " sinnum.")
                print("Það kom upp jafntefli", str(jafntefli), " sinnum.")
                print("Leikurinn var spilaður", str(spilanir - 1), " sinnum.")
                print(str(nafn) + ", aldur", str(aldur))
                print()
                break
            else:
                print("Villa í innslátti! Sláðu inn annaðhvort Skæri, Blað eða Steinn")
            # player was set to True, but we want it to be False so the loop continues
            player = False
            computer = t[randint(0, 2)]
            print()

    elif val == 4:
        # fá inntak frá notanda
        texti = input("Sláðu inn texta: ")
        for i in texti:
            # breyta g k n og r í textanum með "<"
            if i in {"g","k","n","r"} or i in {"G","K","N","R"}:
                print("<", end="")
            else:
                print(i, end="")
        print()
        # finna út miðjuna í textanum, skera textann í gegnum miðjuna og prenta i nýrri línu með capitalize
        mid = (len(texti)) // 2
        print(texti[:mid].capitalize())
        print(texti[mid:].capitalize())
        print()

    elif val == 5:
        # búa til lista
        listi = []
        for x in range(7):
            # fá inntak frá notanda og bæta því i lista
            tolur = int(input("Sláðu inn tölu númer " + str(x + 1) + ": "))
            listi.append(tolur)
        # búa til variable fyrir það sem verkefnið spyr um
        minnstaTala = min(listi)
        haestaTala = max(listi)
        summaTalna = sum(listi)
        medalTal = format(sum(listi) / len(listi), ".2f")
        print("Minnsta talan er: " + str(minnstaTala))
        print("Hæsta talan er: " + str(haestaTala))
        print("Summa talnanna er: " + str(summaTalna))
        print("Meðaltal talnanna er: " + str(medalTal))
        print()

    elif val == 6:
        teningur = 1
        kast = 1
        # búa til while lykkju fyrir fyrsta kast
        while teningur == 1:
            # nota random til að kasta tening
            t1 = random.randint(1, 6)
            t2 = random.randint(1, 6)
            summa = (t1 + t2)
            # prenta útkomur
            print("Kast númer " + str(kast))
            print("-------------")
            print("Fyrsti teningur er: " + str(t1))
            print("Annar teningur er: " + str(t2))
            print("Summan er: " + str(summa))
            # ef summan er 7 eða 11 þá vinnur leikmaður og spilið endar
            if summa in {7, 11}:
                print("----------------------")
                print("Leikmaður vinnur")
                teningur = teningur + 2
            # ef summan er 2, 3 eða 12 þá vinnur talvan og spilið endar
            elif summa in {2, 3, 12}:
                print("----------------------")
                print("Leikmaður tapar")
                teningur = teningur + 2
            # ef summan er eitthvað annað þá er kastað aftur
            elif summa in {4, 5, 6, 8, 9, 10}:
                teningur = teningur + 1
            if teningur == 3:
                print("Takk fyrir að spila")
            print()
            # while lykkja fyrir fleiri köst
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
                # ef leikmaður fær summu fyrsta kasts, þá vinnur hann spilið
                if summa2 == stig:
                    print("----------------------")
                    print("Leikmaður vinnur")
                    teningur = teningur + 1
                # ef leikmaður fær 7, þá vinnur talvan spilið.
                elif summa2 == 7:
                    print("----------------------")
                    print("Leikmaður tapar")
                    teningur = teningur + 1
                # exit message
                if teningur == 3:
                    print("Takk fyrir að spila")
                print()

    elif val == 7:
        listi = []
        numer = 0
        numer += 1
        kast = 0
        # kasta tening 100 sinnum
        for x in range(99):
            roll1 = random.randint(1, 6)
            roll2 = random.randint(1, 6)
            print("Kast teningur 1: ", roll1)
            print("Kast teningur 2: ", roll2)
            samtal = roll1 + roll2
            print("Samtals ", str(samtal))
            numer += 1
            print("Þetta verður sett í listann sem kast: ", numer)
            # setja summu kasts í lista
            listi.append(samtal)
        # prenta listann á mismunandi vegu
        print("Hérna er listinn þinn óraðaður.")
        print(listi)
        print("Hérna er listinn þinn raðaður.")
        print(sorted(listi))
        print("Summa listans")
        summa = sum(listi)
        print(sum(listi))
        print("Meðaltal listans er.")
        print(summa / numer)
        # prenta út hversu oft 7, 3 og 12 kemur fyrir
        print("7 kemur fyrir: " + str(listi.count(7)) + " sinnum")
        print("3 kemur fyrir: " + str(listi.count(3)) + " sinnum")
        print("12 kemur fyrir: " + str(listi.count(12)) + " sinnum")
        print()

    elif val == 8:
        # búa til lista fyrir allar byggingar
        allar_b = []
        svar = "j"
        print("Sláðu inn upplýsingar um byggingar í Reykjavík.")
        while svar != "n":
            # búa til lista fyrir hverja byggingu
            bygginga_listi = []
            bygging = input("Sláðu inn nafn á byggingu: ")
            print("Sláðu inn upplýsingar um", bygging)
            staðsetning = input("Staðsetning: ")
            arkitekt = input("Arkitekt: ")
            ar = int(input("Byggingarár: "))
            bygginga_listi.append(bygging)
            bygginga_listi.append(staðsetning)
            bygginga_listi.append(arkitekt)
            bygginga_listi.append(ar)
            # bæta byggingu í lista
            allar_b.append((bygginga_listi))
            svar = input("Villtu skrá fleyri bygginar? (j/n): ").lower()
        print()

        for i in range(len(allar_b)):
            print("Bygging: ", allar_b[i][0])
            print("Staðsetning: ", allar_b[i][1])
            print("Arkítekt: ", allar_b[i][2])
            print("Ár: ", allar_b[i][3])
        print()

    elif val == 9:
        # fá inntak notanda um upplýsingar
        nafn = input("Hvað heitir notandinn? ")
        kyn = input("Hvaða kyn ertu (KK/KVK)? ")
        kg = int(input("Sláðu inn þyngd þína í kílóum: "))
        haed = float(input("Sláðu inn hæð þína í metrum: "))
        # formúlan bmi
        bmi = kg / (haed * haed)
        # búa til if setningar fyrir mismunandi bmi niðurstöður, farið eftir töflunni
        if bmi <= 18.5:
            print("BMI stuðull þinn er: " + format(bmi, ".2f"))
            print("Þú ert í vannæringu " + nafn.capitalize())
            print()
        if bmi > 18.5 and bmi < 25:
            print("BMI stuðull þinn er: " + format(bmi, ".2f"))
            print("Þú ert í kjörþyngd " + nafn.capitalize())
            print()
        if bmi > 25 and bmi < 30:
            print("BMI stuðull þinn er: " + format(bmi, ".2f"))
            print("Þú ert í ofþyngd " + nafn.capitalize())
            print()
        if bmi > 30:
            print("BMI stuðull þinn er: " + format(bmi, ".2f"))
            print("Þú ert í offitu " + nafn.capitalize())
            print()

    else:
        break
print("Takk fyrir að nota forritið mitt! ")





