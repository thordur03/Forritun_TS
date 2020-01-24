on = True
while on == True:
    print("(1)")
    print("(2)")
    print("(3)")
    print("(4)")
    print("(5)")
    print("hætta við(4)")
    val=int(input("hvað viltu gera?"))
    if val==1:
        nafn_listi = [] # geri lista
        for x in range(1, 6): # nota for lykkju og bið um 5 nöfn  og bæti þeim í lista
            nafn = input("sláðu inn nafn")
            nafn_listi.append(nafn)
        on1 = True
        while on1 == True: # bý til valmynd
            print("(1)")
            print("(2)")
            print("(3)")
            print("(4)")
            print("hætta við(4)")
            val2 = int(input("hvað viltu gera?"))
            if val2 == 1:
                print("óraðaður listi: ", nafn_listi) # prenti óraðaðan lista
            elif val2 == 2:
                print("Listi í stafrófsröð: ", sorted(nafn_listi)) # prenti lista í stafrófsröð með sorted
            elif val2 == 3:
                listi = sorted(listi)
                print("Öfug stafrófsröð", nafn_listi[::-1]) # prenti sortaðan lista en öfugt
            elif val2 == 4:
                velja = int(input("Veldu tölu milli 1-5"))  # bið um tölu milli 1-5
                if velja >= 1 and velja <= 5:  # ef talan er á milli 1-5 prentir það út það nafn í lisstanum
                    print(nafn_listi[velja - 1])
                else:
                    print("tala þarf að vera milli 1-5")
            elif val2 == 0:
                on1 = False
    elif val== 2:
        import random # bæti við random
        listi = [] # geri lista
        tminni = 0 # tel  undir 250
        tmeiri = 0 # tel yfir 250
        for x in range(1,71): # geri for lykkju
            tala = random.randint(1,500) # bæti við random tölu frá 1 og 500 og bæti henni í lista
            listi.append(tala)
            if tala <251: # talan er minni en 251 bæti ég við tminni breytuna en ef ekki bæti ég í tmeyri
                tminni = tminni+1
            else:
                tmeiri = tmeiri + 1
        print(listi) # prenti listann
        for x in range(0,len(listi),4): # prenti listan í fjagra tala röðum
            print(listi[x],listi[x+1],listi[x+2],listi[x+3])
        print(listi[69],"stærsta Talan") # prenti stærstu töluna
        print(listi[0],"Minsta Talan") # prenti lægstu töluna
    elif val==3:
        listi = [] #geri lista
        fjoldi = int(input("sláðu inn fjölda í áfanganum FOR1TÖ05BU")) # bið um fjölda í hópnum
        for x in range(fjoldi): # nota for lykkju sem fer í gegnum fjölda í hopnum og biður um nöfn og bætir þeim í lista
            nafn = input("sláðu inn nafn í hópnum")
            listi.append(nafn)
        oradadur_listi = listi # geri breyti sem heldur orðuðum lista
        on = True # geri valmynd
        while on == True:
            print("(1)")
            print("(2)")
            print("(3)")
            print("(4)")
            print("(5)")
            print("hætta við(4)")
            val1 = int(input("hvað viltu gera?"))
            if val1 == 1:
                listi = sorted(listi) # sorta listan
                for x in listi: # nota for lykkju sem prentir öll nofnin í listanum
                    print(x)
            elif val1 == 2:
                nyr_listi = [] # by til nyjan lista
                print(listi) # prenti gamlal listann
                nafn_eyda = input("hvaða nafni viltu eyða? ") # bið um nafnið sem á að eyða
                for x in listi: # fer í gengum listan með for lykkju og bæti við öllum nöfnunum nema því sem notendi valdi
                    if nafn_eyda == x:
                        pass
                    else:
                        nyr_listi.append(x)
                    listi = nyr_listi
            elif val1 == 3:
                nytt_nafn = input("sláðu inn nafn: ") # bið notenda um nytt nafn nafn
                listi.append(nytt_nafn) # bæti nafninu í listann
                print(listi) # prenti listann
            elif val1 == 4:
                print(oradadur_listi) # prenti óraðaða listann
            elif val ==0:
                on = False

    elif val==4:
        talna_listi = [] # geri lista
        summa = 0 # geri breytuu fyrir summuna
        teljari = 0 # geri teljara
        for x in range(7): # geri for lykkju sem leyfir notenda ap bæti við 7 tölum í lista og tel hversu margar tölur eru jaft og eða undir 50.5
            tala = int(input("slaðu inn tölu"))
            talna_listi.append(tala)
            summa = summa+tala
            if tala <= 50.5:
                teljari=+1
        print(max(talna_listi),"stærsta talan") # prenti stærstu töluna
        print(min(talna_listi),"minnsta talan") # prenti minnstu töluna
        print(summa//7,"meðaltalið") # prenti meðaltalið
        print(sorted(talna_listi),"stærðar röð") # sorta listann
        for x in talna_listi: # nota for lykkju sem prentir út allar tölunar í röð me ; á milli og nota end fyrir það
            print(x,end=";")
        print(teljari,"þessar tölur eru undir 50,5") # prenti tölunar undir 50,5

    elif val==5:
        on1 = True

        import  random
        teningalisti = []
        teljari = 0

        while on1 == True:
            teljari = teljari + 1
            teningur_1 = random.randint(1,6)
            teningur_2 = random.randint(1,6)

            teningalisti.append(teningur_1)
            teningalisti.append(teningur_2)

            print("teningur 1:",teningur_1,"teningur 2:",teningur_2,"kast nmr: ",teljari)
            halda_afram = input("villtu halda áfram? j(já) n(nei)")
            if halda_afram == "n":
                on1 = False
        kast_listi = []
        for x in range(7):
            tal = 0
            tal = teningalisti.count(x)
            kast_listi.append(tal)
            



    elif val==0:
        on=False
