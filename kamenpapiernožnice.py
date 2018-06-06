"""
Simuluje hru kamen papier nožnice a jej rozšírenú verziu.
Obe hry ananlizuje a porovnáva ktorá z nich je lepšia z hladiska remíz (čím menej remíz tým lepšia)
"""

from random import randint
def playerRegular():
    a=randint(1,3)
    return a
def RegularGame():
    a=playerRegular()
    if a==1:
        return "K"
    elif a==2:
        return "P"
    else:
        return "N"
def checkRegularGame(rounds, turns):
    remizy=0
    for i in range (rounds):
        x=0
        for i in range (turns):
            player1=RegularGame()
            player2=RegularGame()
            if player1==player2:
                x=x+0
            elif (player1=="K" and player2=="N") or(player1=="P" and player2=="K") or (player1=="N" and player2=="P"):
                x=x+1
            else:
                x=x-1
        if x==0:
            remizy=remizy+1
    podiel=remizy*100.0/rounds
    return podiel

def playerExtended():
    a=randint(1,5)
    return a
    
def ExtendedGame():
    a=playerExtended()
    if a==1:
        return "K"
    elif a==2:
        return "P"
    elif a==3:
        return "N"
    elif a==4:
        return "T"
    else:
        return "S"
    
def checkExtendedGame(rounds, turns):
    remizy=0
    for i in range (rounds):
        x=0
        for i in range (turns):
            player1=ExtendedGame()
            player2=ExtendedGame()
            if player1==player2:
                x=x+0
            elif (player1=="K" and (player2=="N" or player2=="T")) or(player1=="P" and (player2=="K"or player2=="S")) or(player1=="N" and (player2=="P" or player2=="T")) or(player1=="T" and (player2=="S" or player2=="P")) or(player1=="S" and (player2=="N" or player2=="K")):
                x=x+1
            else:
                x=x-1
        if x==0:  
            remizy=remizy+1
    podiel=remizy*100.0/rounds
    return podiel

def compareGames (rounds, turns, tolerance):
    normal=checkRegularGame(rounds, turns)
    extended=checkExtendedGame(rounds, turns)
    print normal, extended
    if normal-extended<(0-tolerance):
        return "Regulerni je lepsi"
    elif normal-extended>(0+tolerance):
        return "Rozsirena je lepsi"
    else:
        return "Obe hry jsou podobne"

for i in range (10):
    print compareGames(10000,50,0.5)
