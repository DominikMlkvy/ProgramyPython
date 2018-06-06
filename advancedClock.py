#Program čo do konzoly vykresluje aktuálny čas

from datetime import datetime
from time import*
class Number:
    def __init__(self, digit, code):
        self.digit=digit
        self.code=code
    def picture (self):
        j=1
        for i in self.code:
            if i==1:
                print "##",
            else:
                print "  ",
            if j%3==0:
                print""
            j+=1


class Clock:
    def __init__(self, time, numbers,seconds=False):
        self.time=time
        self.numbers=numbers
        self.seconds=seconds
    def minute(self,seconds):
        array=[]
        for i in self.time:
            array.append (self.numbers[i].code)
        display=[]
        if seconds==True:
            dig=6
        else:
            dig=4
        for n in range(5):
            for i in range (dig):
                for j in range (3):
                    display.append(array[i][(n*3)+j])
                if i==1 or (i==3 and seconds==True):
                    display.append(0)
                    if n%2==1:
                        display.append(1)
                    else:
                        display.append(0)
                display.append(0)
            display.append(2)
        return display
    
    def displayshow(self):
        display=self.minute(self.seconds)
        for i in display:
            if i==1:
                print "##",
            elif i==0:
                print "  ",
            else:
                print""


"""class Run:
    def __init__(self,seconds=False):
        self.seconds=seconds
        self.time(seconds)
    def time(seconds=False):
        zer=Number(0, [1,1,1,1,0,1,1,0,1,1,0,1,1,1,1])
        one=Number(1, [0,0,1,0,0,1,0,0,1,0,0,1,0,0,1])
        two=Number(2, [1,1,1,0,0,1,1,1,1,1,0,0,1,1,1])
        thr=Number(3, [1,1,1,0,0,1,1,1,1,0,0,1,1,1,1])
        fou=Number(4, [1,0,1,1,0,1,1,1,1,0,0,1,0,0,1])
        fiv=Number(5, [1,1,1,1,0,0,1,1,1,0,0,1,1,1,1])
        six=Number(6, [1,1,1,1,0,0,1,1,1,1,0,1,1,1,1])
        sev=Number(7, [1,1,1,0,0,1,0,0,1,0,0,1,0,0,1])
        eig=Number(8, [1,1,1,1,0,1,1,1,1,1,0,1,1,1,1])
        nin=Number(9, [1,1,1,1,0,1,1,1,1,0,0,1,1,1,1])
        numbers=[zer,one,two,thr,fou,fiv,six,sev,eig,nin]
        while 1:
            outputTime=[]
            inputTime=strftime('%H%M%S')
            for i in inputTime:
                outputTime.append(int(i))

            clock=Clock(outputTime, numbers, seconds)
            clock.displayshow()
            print""
            if seconds==True:
                sleep(1)
            else:
                sleep(60)"""
    
def time(seconds=False):
        zer=Number(0, [1,1,1,1,0,1,1,0,1,1,0,1,1,1,1])
        one=Number(1, [0,0,1,0,0,1,0,0,1,0,0,1,0,0,1])
        two=Number(2, [1,1,1,0,0,1,1,1,1,1,0,0,1,1,1])
        thr=Number(3, [1,1,1,0,0,1,1,1,1,0,0,1,1,1,1])
        fou=Number(4, [1,0,1,1,0,1,1,1,1,0,0,1,0,0,1])
        fiv=Number(5, [1,1,1,1,0,0,1,1,1,0,0,1,1,1,1])
        six=Number(6, [1,1,1,1,0,0,1,1,1,1,0,1,1,1,1])
        sev=Number(7, [1,1,1,0,0,1,0,0,1,0,0,1,0,0,1])
        eig=Number(8, [1,1,1,1,0,1,1,1,1,1,0,1,1,1,1])
        nin=Number(9, [1,1,1,1,0,1,1,1,1,0,0,1,1,1,1])
        numbers=[zer,one,two,thr,fou,fiv,six,sev,eig,nin]
        while 1:
            outputTime=[]
            inputTime=strftime('%H%M%S')
            for i in inputTime:
                outputTime.append(int(i))

            clock=Clock(outputTime, numbers, seconds)
            clock.displayshow()
            print""
            if seconds==True:
                sleep(1)
            else:
                sleep(60)
                
time(True)
