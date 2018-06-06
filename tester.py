"""
Program na pomáhanie k učeniu
Užívateľ si vytvorí "databázu" do ktorej zadá otázky a správne odpovede
Potom program beží v nekonečnom cikle a píta sa náhodne vybraté otázky
Užívateľ odpovedá, a program vyhodnotí či odpoveď svrávna

poznamka: program nepracuje s reálnymi databázami ale s textovými súbormi
"""
from random import randint
def normal(file1, file2):
    block1=[]
    block2=[]
    output=""
    correct=0
    wrong=0
    with open(file1, "r") as input1:
        with open (file2, "r") as input2:
            for i in input1:
                block1.append(i[:-1])
            for j in input2:
                block2.append(j[:-1])
    while True:
        random=randint(0,(len(block1)-1))
        output= "%s: " %(block1[random])
        answer=raw_input(output)
        if answer.lower()==block2[random].lower():
            output= "OK"
            correct+=1
        else:
            output="NOK  %s - %s your answer %s"%(block1[random], block2[random], answer)
            wrong+=1
        raw_input (output)



def files(file1, file2, write):
    inputword1=""
    inputword2=""
    with open (file1, write)as words1:
        with open (file2, write) as words2:
            while True:
                inputword1=raw_input("zadaj otazku, x pre koniec: ")
                if inputword1=="x":
                    return 1
                else:
                    inputword1+="\n"
                    words1.write(inputword1)
                inputword2=raw_input("zadaj odpoveď: ")
                inputword2+="\n"
                words2.write(inputword2)

    

def choice(file1, file2):
    write= raw_input("vytvorit novu databazu?(y pre ano, n pre nie, p pre pridanie slov do existujucej databazy)" )
    if write=="y":
        files(file1, file2, "w")
    elif write=="p":
        files(file1,file2, "a")
    normal(file1,file2)
    #mode= raw_input ("zvol sposob(n pre normal)")
    #if mode == "n":
choice("guestions.txt","answers.txt" ) 
    
