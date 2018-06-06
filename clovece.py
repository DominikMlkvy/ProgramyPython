# Program ktor� analizuje modifikovan� hru clovece

from random import randint
def kocka(output=True): #tahy s� in� ako v be�nej hre, t�to funkcia ich rie�i
    hod=randint(1,6)
    cislo=[hod]
    sucet=hod
    pocet_1=0
    while (hod==1):
        pocet_1+=1
        hod=randint(1,6)
        sucet=sucet+hod
        cislo.append(hod)
    if output==True:
        print cislo,
    if pocet_1%2!=0 or pocet_1==0 :
        return sucet
    else:
        return 0

def game (length, output = True): #simuluje jednu hru d�ky length
    pozice=0
    hod=0
    while (pozice<length):
        koc=kocka(False)
        pozice+=koc
        hod+=1
        if output==True:
            print hod,"kolo:",
            kocka(True),
            print "->", pozice

        if pozice==(length-1):
            pozice=pozice-koc
        elif pozice>length:
            pozice=pozice-koc
    if output==True:
        print "ukonceno v", hod, " kolach:"
    return hod
game(20, True)

def game_analysis(length, count): #zahr� count-po�et hier a vr�ti po ko�k�ch �ahoch sa priemerne skon�ili
    soucet=0
    priem=0
    for i in range (count):
        hra=game(length, output = False)
        soucet+=hra
    priem=(soucet*1.0)/count
    return priem

for i in range(3):
    print game_analysis(20, 1000)

def game_average_length(count):  # vyp�e po ko�k�ch kol�ch sa priemerne skon�� hra d�ky 3-50
    for i in range (3,51):
       b=game_analysis (i,count)
       print "plan ma",i,"pol�",
       print "hra skon�� priemerne po", b, "kolach"
game_average_length (1000) 
    
        
    
        
        
