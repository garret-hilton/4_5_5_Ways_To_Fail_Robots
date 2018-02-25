# 4_5_5_Ways_To_Fail_Robots

# Labs for CSCI - 455 Robotics - Embedded Systems
# Assignment 2
# The work is this repository belongs to Garret Hilton and Meshal Albaiz. Any
# use of this work without citation for academic purposes at Montana State
# University will be considered academic misconduct and plagiarism. The authors
# claim no liability for improper use of work contained in this repository.
# Use at your own risk.

import time
import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter import messagebox
import _thread

class GuiTest():
    def __init__(self, r, c=None):
        self.client = c
        self.root = r
        #self.flag = True
        self.speed = .8
        self.timeToWait = 5
        self.flag1 = False
        self.dropBoxFlag = False
        self.x = 10
        self.y = 50
        self.deltaX1 = 0
        self.deltaX2 = 0
        self.deltaY1 = 0
        self.deltaY2 = 0
        self.buttonID = 0
        self.font1 = font.Font(family="Times",size=30, weight="bold", slant="italic")
        self.font2 = font.Font(family="Times",size=15, weight="bold", slant="italic")
        self.color = "#FFFFFF"
        self.img = PhotoImage(file="ForBack.gif")
        #self.listbox = Listbox(r, yscrollcommand=self.scrollbar.set, height=5)
        #self.listbox.pack(side=RIGHT, fill=BOTH)
        self.scrollbar = Scrollbar(r)
        self.scrollbar.grid(row=1,column=7, sticky=N+S)
        #self.scrollbar.pack(side=RIGHT, fill=Y)
        self.listbox = Listbox(r, bg="#999999")
        self.listbox.grid(row=1, column=6, sticky=N+S)
        #self.listbox.pack(side=RIGHT, fill=Y)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        self.canvasW = 650
        self.canvasH = 400
        self.c = tk.Canvas(self.root, bg="#333333", width = self.canvasW, height=self.canvasH)
        #self.c2 = tk.Canvas( self.root, bg="#333333", width = 150, height=50)
        #self.c2.pack(side=RIGHT)
        self.c.bind('<B1-Motion>', self.mouseDragged)
        self.c.bind('<ButtonPress-1>', self.mousePressed)
        self.c.bind('<ButtonRelease-1>', self.mouseRelease)
        #self.c.create_oval(5, 5, 45, 45, fill="#FFFF00")
        self.drawStuff()
        self.c.bind('<Motion>', self.motion)
        r.title("TangoBot")
        r.bind('<Up>', self.arrow)
        r.bind('<Left>', self.arrow)
        r.bind('<Down>', self.arrow)
        r.bind('<Right>', self.arrow)
        self.c.grid(row=1, column=1, rowspan=3, columnspan=5)
        button = tk.Button(self.root, width="15", text="Put in Queue", font=self.font2, bg="blue", fg="yellow", command=self.addToQueue)
        button.grid(row=4, column=5)
        button2 = tk.Button(self.root, width="15", text="Move Down",font=self.font2, bg="blue", fg="yellow", command=self.fun)
        button2.grid(row=2, column=6)
        button3 = tk.Button(self.root, width="15", text="Move Down",font=self.font2, bg="blue", fg="yellow", command=self.fun)
        button3.grid(row=3, column=6)
        button4 = tk.Button(self.root, width="15", text="Run",font=self.font2, bg="blue", fg="yellow", command=self.fun)
        button4.grid(row=4, column=6)
        button5 = tk.Button(self.root, width="15", text="Remove Action\nFrom Drop Box",font=self.font2, bg="blue", fg="yellow", command=self.removeAction)
        button5.grid(row=5, column=5)
        self.s1 = Scale(self.root, from_=0, to=10, orient=HORIZONTAL, resolution=0.1)
        self.s2 = Scale(self.root, from_=4000, to=8000, orient=HORIZONTAL)
        self.s1.grid(row=4, column=2, columnspan=3, sticky=N+S+W+E)
        self.s1.set(1.0)
        self.s2.grid(row=5, column=2, columnspan=3, sticky=N+S+W+E)
        self.s2.set(6000)
        label1=tk.Label(self.root, text="Set Time", font=self.font2)
        label1.grid(row=4, column=1, )
        label2=tk.Label(self.root, text="Set Speed", font=self.font2)
        label2.grid(row=5, column=1)






    def drawStuff(self):
        self.c.delete("all")

        #self.c.create_rectangle(10, 50, 145, 95,   fill="#FFFF00", width=5)
        self.c.create_image(10,50,anchor=NW, image=self.img)
        self.c.create_rectangle(10, 105, 145, 150, fill="#3377AA", width=5)
        self.c.create_rectangle(10, 160, 145, 205, fill="#00FF00", width=5)
        self.c.create_rectangle(10, 215, 145, 260, fill="#FF0F00", width=5)
        self.c.create_rectangle(10, 270, 145, 315, fill="#111FFF", width=5)
        self.c.create_text(380, 30,font=self.font1, text="Drop Box", fill="#777777")
        self.c.create_text(80, 30,font=self.font1, text="Actions:", fill="#777777")
        self.c.create_rectangle(160, 50, 600, 300, width=5, fill="#444444")
        #self.c.pack()
    def drawButton1(self):
        self.c.create_rectangle(10, 50, 145, 95, fill="#FFFF00", width=5)

    def timer(self):
        temp = self.timeToWait
        time.sleep(self.timeToWait)
        print("Timer for %f seconds has ended" % temp)

    def mousePressed(self, event):
        self.deltaX1 = event.x - 10
        self.deltaX2 = 145 - event.x
        if (event.x > self.x and event.x < self.x + 145) and (event.y > self.y and event.y < self.y + 45):
            self.buttonID = 1
            self.flag1 = True
            self.deltaY1 = event.y - 50
            self.deltaY2 = 95 - event.y
            self.color = "#FFFF00"
        elif (event.x > self.x and event.x < self.x + 145) and (event.y > 105 and event.y < 150):
            self.buttonID = 2
            self.flag1 = True
            self.deltaY1 = event.y - 105
            self.deltaY2 = 150 - event.y
            self.color = "#3377AA"
        elif (event.x > self.x and event.x < self.x + 145) and (event.y > 160 and event.y < 205):
            self.buttonID = 3
            self.flag1 = True
            self.deltaY1 = event.y - 160
            self.deltaY2 = 205 - event.y
            self.color = "#00FF00"
        elif (event.x > self.x and event.x < self.x + 145) and (event.y > 215 and event.y < 260):
            self.buttonID = 4
            self.flag1 = True
            self.deltaY1 = event.y - 215
            self.deltaY2 = 260 - event.y
            self.color = "#FF0F00"
        elif (event.x > self.x and event.x < self.x + 145) and (event.y > 270 and event.y < 305):
            self.buttonID = 5
            self.flag1 = True
            self.deltaY1 = event.y - 270
            self.deltaY2 = 315 - event.y
            self.color = "#111555"
    def mouseDragged(self, event):
        if self.flag1 == True:
            self.drawStuff()
            if self.buttonID == 1:
                self.c.create_image(event.x-self.deltaX1,event.y-self.deltaY1,anchor=NW, image=self.img)
            else:
                self.c.create_rectangle(event.x-self.deltaX1, event.y-self.deltaY1,event.x+self.deltaX2, event.y+self.deltaY2,width=5, fill=self.color)

    def mouseRelease(self, event):
        if self.flag1 == True:
            self.flag1 = False
            self.drawStuff()
            if (event.x > 160 and event.x < 600) and (event.y > 50 and event.y < 300):
                self.dropBoxFlag = True
                self.x = event.x - 22
                self.y = event.y -23
                if self.buttonID == 1:
                    self.c.create_image(event.x-self.deltaX1,event.y-self.deltaY1,anchor=NW, image=self.img)
                else:
                    self.c.create_rectangle(event.x-self.deltaX1, event.y-self.deltaY1,event.x+self.deltaX2, event.y+self.deltaY2, fill=self.color)
            print("Released at:\n    x: %f" % self.x)
            print("\n    y: %f" %  self.y)

    def arrow(self, key):
        if key.keycode==114:
            self.timeToWait = 5
            print("Right\nWating for %f" % self.timeToWait)
            try:
                _thread.start_new_thread(self.timer, ())
            except:
               print ("Error: unable to start thread")
        elif key.keycode==111:
            self.timeToWait = 1
            try:
                _thread.start_new_thread(self.timer, ())
            except:
               print ("Error: unable to start thread")
            print("Up\nWating for %f" % self.timeToWait)
        elif key.keycode==116:
            print("Down")
        elif key.keycode==113:
            print("Left")

    def removeAction(self):
        self.dropBoxFlag = False
        self.drawStuff()
        self.x = 10
        self.y = 50
        self.s1.set(1.0)
        self.s2.set(6000)
        print("Action removed from Drop Box")
    def mouseClick(self, event):
        print(event)

    def addToQueue(self):
        if self.dropBoxFlag == True:
            string = ("A: "+str(self.buttonID) +" T = " + str(self.s1.get())  + " S = " + str(self.s2.get()))
            self.listbox.insert(END, string)
            self.drawStuff()
            self.dropBoxFlag = False
            self.x = 10
            self.y = 50
            self.s1.set(1.0)
            self.s2.set(6000)
            print("Function Added to Queue")
        else:
            messagebox.showerror("Error", "No Action Selected\nPlease Place an Action\nin the Drop Box")

    def fun(self):
        self.drawStuff()
        self.x = 10
        self.y = 10
        print("Button is pushed")

    def motion(self, event):
      print("Mouse position: (%s %s)" % (event.x, event.y))
      return

def __main__():
    print("Hello\n")

    root = tk.Tk()
    gui = GuiTest(root)
    #root.bind('<Up>', gui.arrow)
    #root.bind('<Left>', gui.arrow)
    #root.bind('<Down>', gui.arrow)
    #root.bind('<Right>', gui.arrow)
    #root.bind('<Button>', gui.mouseClick)
    root.mainloop()



__main__()
