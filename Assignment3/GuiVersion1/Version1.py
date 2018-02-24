# 4_5_5_Ways_To_Fail_Robots

# Labs for CSCI - 455 Robotics - Embedded Systems

# The work is this repository belongs to Garret Hilton and Meshal Albaiz. Any
# use of this work without citation for academic purposes at Montana State
# University will be considered academic misconduct or plagiarism. The authors
# claim no liability for improper use of work contained in this repository.
# Use at your own risk.

import time
import tkinter as tk
from tkinter import *
from tkinter import font
import _thread

class GuiTest():
    def __init__(self, r, c=None):
        self.client = c
        self.root = r
        #self.flag = True
        self.speed = .8
        self.timeToWait = 5
        self.flag1 = False
        self.x = 10
        self.y = 10
        self.font1 = font.Font(family="Times",size=30, weight="bold", slant="italic")
        self.font2 = font.Font(family="Times",size=15, weight="bold", slant="italic")
        #self.listbox = Listbox(r, yscrollcommand=self.scrollbar.set, height=5)
        #self.listbox.pack(side=RIGHT, fill=BOTH)
        self.scrollbar = Scrollbar(r)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.listbox = Listbox(r, yscrollcommand=self.scrollbar.set, bg="#999999")
        self.listbox.pack(side=RIGHT, fill=Y)
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
        self.c.pack()
        button = tk.Button(self.root, width="15", text="Clear Drop Box", font=self.font2, bg="blue", fg="yellow", command=self.fun)
        button.pack(side = tk.RIGHT)
        button2 = tk.Button(self.root, width="15", text="Second",font=self.font2, bg="blue", fg="yellow", command=self.fun)
        button2.pack(side = tk.BOTTOM)






    def drawStuff(self):
        self.c.delete("all")
        self.c.create_oval(10, 10, 45, 45, fill="#FFFF00")
        self.c.create_text(375, 30,font=self.font1, text="Drop Box", fill="#777777", )
        self.c.create_rectangle(150, 50, 600, 300, width=5, fill="#444444")
        self.c.pack()


    def timer(self):
        temp = self.timeToWait
        time.sleep(self.timeToWait)
        print("Timer for %f seconds has ended" % temp)

    def mousePressed(self, event):
        if (event.x > self.x and event.x < self.x + 45) and (event.y > self.y and event.y < self.y + 45):
            self.flag1 = True

    def mouseDragged(self, event):
        if self.flag1 == True:
            self.drawStuff()
            self.c.create_oval(event.x - 22, event.y-22, event.x+23, event.y+23, fill="#FFFF00")
            self.c.pack()

    def mouseRelease(self, event):
        if self.flag1 == True:
            self.flag1 = False
            #string = ("X = " + str(self.x)  + " Y = " + str(self.y))
            self.drawStuff()
            if (event.x > 150 and event.x < 600) and (event.y > 50 and event.y < 300):
                self.x = event.x - 22
                self.y = event.y -23
                self.c.create_oval(event.x - 22, event.y-22, event.x+23, event.y+23, fill="#FFFF00")
                string = ("X = " + str(self.x)  + " Y = " + str(self.y))
                self.listbox.insert(END, string)
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


    def mouseClick(self, event):
        print(event)


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
