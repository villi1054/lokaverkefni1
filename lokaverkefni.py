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
        print("Sláðu inn 10 orð og forritið finnur út allskonar um þau")
        listi = []
        lengd = 10
        while len(listi) < lengd:
            ord = input("Sláðu inn orð í listann þinn")
            listi.append(ord)
            listi4 = []
            if len(ord) == 4:
                listi4.insert(i, char)
                print(listi4)
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
