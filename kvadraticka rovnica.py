from Tkinter import *

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self,master)
        self.grid()
        self.widgets()

    def widgets(self):
        self.a=Entry(self, width=10)
        self.a.insert(0, "0")
        self.a.grid(row =1, column=0, columnspan=1, sticky=W)
        self.x2= Label(self, text= "x^2  +  ")
        self.x2.grid(row=1, column=1, sticky=W)

        self.b=Entry(self, width=10)
        self.b.insert(0, "0")
        self.b.grid(row =1, column=2, columnspan=1, sticky=W)
        self.x1= Label(self, text= "x  +  ")
        self.x1.grid(row=1, column=3, sticky=W)

        self.c=Entry(self, width=10)
        self.c.insert(0, "0")
        self.c.grid(row =1, column=4, columnspan=1, sticky=W)
        self.x0= Label(self, text= "  =  0")
        self.x0.grid(row=1, column=5, sticky=W)

        self.solve=Button(self, width= 10, text= " Vyriesit ", command= self.solve)
        self.solve.grid(row=2, column=0, sticky=W)

        self.clear= Button(self, width=10, text=" Zmazat ", command= self.clear)
        self.clear.grid(row=2, column=2, sticky=W)

        self.R1= Label(self, text= "x1     = ")
        self.R1.grid(row=3, column=0, sticky=W)
        self.res1=Text(self, width= 30, height=1, wrap= WORD)
        self.res1.grid(row=3, column= 1, columnspan=4, sticky=W)

        self.R2= Label(self, text= "x2     = ")
        self.R2.grid(row=4, column=0, sticky=W)
        self.res2=Text(self, width= 30, height=1, wrap= WORD)
        self.res2.grid(row=4, column= 1, columnspan=4, sticky=W)

        
        
    def solve(self):
        A=float(self.a.get())
        B=float(self.b.get())
        C=float(self.c.get())
        if A==0:
            X1=C/B
            X2=" - "
        elif C==0:
            X1=0.0
            X2=B/A
        elif B==0:
            if C>0:
                X1=str(C**0.5)+"i"
                X2=str(-1*(C**0.5))+"i"
            else:
                X1= str((-C)**0.5)
                X2= str(-(-C)**0.5)
        else:
            D= B**2-4*A*C
            if D<0:
                X1=str(-B/2*A) +" + "+ str((-D)**0.5/2*A)+ "i"
                X2=str(-B/2*A) +" - "+ str((-D)**0.5/2*A)+ "i"
            else:
                X1= (-B + D**0.5)/2*A
                X2=(-B - D**0.5)/2*A
        self.res1.delete(0.0, END)
        self.res1.insert(0.0, X1)
        self.res2.delete(0.0, END)
        self.res2.insert(0.0,X2)
        
    def clear(self):
        self.a.delete(0, END)
        self.b.delete(0, END)
        self.c.delete(0, END)
        self.res1.delete(0.0, END)
        self.res2.delete(0.0, END)

        self.a.insert(0, "0")
        self.b.insert(0, "0")
        self.c.insert(0, "0")

        
root= Tk()
root.title("GUI")
root.geometry("500x100")

app= Application(root)

root.mainloop()
