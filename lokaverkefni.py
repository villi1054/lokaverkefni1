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
        listi = []
        for x in range(50):
            listi.append(randint(5, 70))
        teljari = 1
        for i in listi:
            teljari *= i
        print("Margfeldi talnanna er "+ str(teljari))
        print(max(listi))
        print(min(listi))
        print(listi)
        print(sorted(listi))
    elif val == 2:
        print("Tölur sem að ganga upp í 7 en ekki 5 ▼▼▼▼")
        nl = []
        for x in range(1500, 2700):
            if (x % 7 == 0) and (x % 5 == 0):
                nl.append(str(x))
        print(','.join(nl))
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
    elif val == 6:
    elif val == 7:
    elif val == 8:
    elif val == 9:
    elif val == 10:
        print("Takk fyrir að nota forritið mitt ")
        break
    else:
        break
        print("Takk fyrir að nota forritið mitt! ")
