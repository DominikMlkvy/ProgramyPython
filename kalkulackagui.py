# coding: utf8
from Tkinter import *
from PIL import Image,ImageTk
from kalkulacka import *

c1=Simple("2 * 2 - 585 / 12")
root=Tk()
root.title("Kalkulačka")
# root.geometry("500x500")
root.configure(background="#777777")

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self,master)
        self.grid()
        self.widgets()

    def widgets(self):

        self.display=Entry(self, width=25, font=("Courier", 25), justify=RIGHT, bg="#505050", fg="white")
        self.display.grid(row=1, column=0, columnspan=8, sticky=W)
        self.display.insert(0,"0")

        for i in range(10):
            self.newbutton = Button(self, text=i, font=("Courier", 20), command=lambda i=i: self.display.insert(END, i))
            self.newbutton.grid(row=2 + (9- i) / 3, column=(9 - i) % 3, sticky=W)
        self.plus=Button(self, text="+", font=("Courier", 20), command=lambda: self.display.insert(END, " + "))
        self.plus.grid(row=2, column=3, sticky=W)
        self.minus = Button(self, text="-", font=("Courier", 20), command=lambda: self.display.insert(END, " - "))
        self.minus.grid(row=3, column=3, sticky=W)
        self.times = Button(self, text="*", font=("Courier", 20), command=lambda: self.display.insert(END, " * "))
        self.times.grid(row=4, column=3, sticky=W)
        self.divided = Button(self, text="/", font=("Courier", 20), command=lambda: self.display.insert(END, " / "))
        self.divided.grid(row=5, column=3, sticky=W)
        self.decimal = Button(self, text=".", font=("Courier", 20), command=lambda: self.display.insert(END, "."))
        self.decimal.grid(row=5, column=1, sticky=W)
        self.power = Button(self, text = "^", font= ("Courier", 20), command= lambda: self.display.insert(END, " ^ "))
        self.power.grid(row= 2, column=4, sticky=W)

        self.cl = Button(self, text="C", font=("Courier", 20), command=self.clear)
        self.cl.grid(row=5, column=2, sticky=W)
        self.eq= Button(self, text="=", font=("Courier", 20), height=3, command=self.equals)
        self.eq.grid(row=4, column=4, rowspan=2, sticky=W)

        self.img=Image.open("logo.jpg")
        self.photo=ImageTk.PhotoImage(self.img)
        self.picture=Button(self,image=self.photo, command=self.clear)
        self.picture.grid(row=2, rowspan=4, column=5)

    def clear(self):
        self.display.delete(0,END)
        self.display.insert(0,"0")
    def equals(self):
        problem=Simple(self.display.get())
        self.display.delete(0,END)
        self.display.insert(0,round(problem.result,10))






App=Application(root)
root.mainloop()