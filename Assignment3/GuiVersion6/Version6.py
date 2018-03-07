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
import Run
import Menu

class GuiTest():
    def __init__(self, r, c=None):
        self.client = c
        self.root = r
        self.root.attributes('-fullscreen', True)
        self.speed = .8
        self.timeToWait = 5
        self.flag1 = False
        self.dropBoxFlag = False
        self.x = 10
        self.y = 50
        self.deltaX1 = 0
        self.deltaY1 = 0
        self.buttonID = 0
        self.font1 = font.Font(family="Times",size=30, weight="bold", slant="italic")
        self.font2 = font.Font(family="Times",size=12, weight="bold", slant="italic")
        self.font3 = font.Font(family="Times",size=20, weight="bold", slant="italic")
        self.font4 = font.Font(family="Courier",size=11, weight="bold")
        self.color = "#FFFFFF"
        self.imgForBack = PhotoImage(file="ForBack.gif")
        self.imgTurnB = PhotoImage(file="TurnBody.gif")
        self.imgTurnR = PhotoImage(file="Turn.gif")
        self.imgTiltH = PhotoImage(file="TiltHead.gif")
        self.imgTurnH = PhotoImage(file="TurnHead.gif")
        self.actionString = " "
        self.scrollbar = Scrollbar(r)
        self.scrollbar.grid(row=2,column=8, sticky=N+S)
        self.listbox = Listbox(r, bg="#999999", width= 30, font=self.font4 )
        self.listbox.grid(row=2, column=6, columnspan=2, sticky=N+S+E+W)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        fileMenu = Menu.FileMenu(self.root, self.listbox)
        self.canvasW = 510
        self.canvasH = 330
        self.c = tk.Canvas(self.root, bg="#333333", width = self.canvasW, height=self.canvasH)
        self.c.bind('<B1-Motion>', self.mouseDragged)
        self.c.bind('<ButtonPress-1>', self.mousePressed)
        self.c.bind('<ButtonRelease-1>', self.mouseRelease)
        self.drawStuff()
        r.title("TangoBot")
        self.c.grid(row=1, column=1, rowspan=5, columnspan=5)
        button = tk.Button(self.root, width="15", text="Put in Queue", font=self.font2, bg="blue", fg="yellow", command=self.addToQueue)
        button.grid(row=6, column=5)
        button2 = tk.Button(self.root, width="10", text="Move Up",font=self.font2, bg="blue", fg="yellow", command=self.moveUp)
        button2.grid(row=3, column=6, sticky=E+W)
        button3 = tk.Button(self.root, width="10", text="Move Down",font=self.font2, bg="blue", fg="yellow", command=self.moveDown)
        button3.grid(row=3, column=7, sticky=E+W)
        button4 = tk.Button(self.root, width="10", text="Run",font=self.font2, bg="green3", fg="yellow", command=self.runQueue)
        button4.grid(row=6, column=6, rowspan=2,columnspan=2, sticky=N+S+W+E)
        button5 = tk.Button(self.root, width="15", text="Remove Action\nFrom Drop Box",font=self.font2, bg="blue", fg="yellow", command=self.removeAction)
        button5.grid(row=7, column=5)
        button6 = tk.Button(self.root, width="10", text="Remove",font=self.font2, bg="blue", fg="yellow", command=self.removeQueue)
        button6.grid(row=4, column=6, sticky=E+W)
        button7 = tk.Button(self.root, width="10", text="Delete All",font=self.font2, bg="blue", fg="yellow", command=self.deleteQueue)
        button7.grid(row=4, column=7, sticky=E+W)
        button8 = tk.Button(self.root, width="10", text="Edit",font=self.font2, bg="blue", fg="yellow", command=self.editQueue)
        button8.grid(row=5, column=6, sticky=E+W, columnspan=2)
        self.s1 = Scale(self.root, from_=0, to=10, orient=HORIZONTAL, resolution=0.1, width=30)
        self.s2 = Scale(self.root, from_=4000, to=8000, orient=HORIZONTAL, resolution=250, width=30)
        self.label1=tk.Label(self.root, text="Set Time", font=self.font2)
        self.label2=tk.Label(self.root, text="Set PWM", font=self.font2)
        self.label3=tk.Label(self.root, text="Action Queue", font=self.font3)
        self.label3.grid(row = 1, column = 6, columnspan=2)

    def editQueue(self):
        try:
            self.pos = self.listbox.curselection()
            string = self.listbox.get(self.listbox.curselection())
            #print(self.pos)

        except:
            messagebox.showerror("Error", "No Action Selected\nPlease Select an Item In \n the Queue to Edit")
            return

        self.t = Toplevel(self.root)
        self.t.attributes('-fullscreen', True)
        self.t.wm_title("Edit Window")
        label3 = tk.Label(self.t, text=string, font=self.font3)
        label3.grid(row = 1, column = 1, columnspan=3)
        label1 = tk.Label(self.t, text="PWM")
        label1.grid(row = 2, column = 1, columnspan=1)
        label2 = tk.Label(self.t, text="Time")
        label2.grid(row = 3, column = 1, columnspan=1)
        label3 = tk.Label(self.t, text="                                                             ")
        label3.grid(row = 5, column = 1, columnspan=5)
        self.s3 = Scale(self.t, from_=0, to=10, orient=HORIZONTAL, resolution=0.1, width=30)
        self.s4 = Scale(self.t, from_=4000, to=8000, orient=HORIZONTAL, resolution=250, width=30)
        button = tk.Button(self.t, width="10", text="OK",font=self.font2, bg="blue", fg="yellow", command=self.closeWindow)
        button.grid(row=4, column=2, sticky=E+W, columnspan=2)
        self.s3.grid(row=3, column=2, columnspan=4, sticky=N+S+W+E)
        self.s3.set(1.0)
        self.s4.grid(row=2, column=2, columnspan=4, sticky=N+S+W+E)
        self.s4.set(6000)

    def parse(self):
        string = self.listbox.get(self.listbox.curselection())
        value = string.split(",")
        channels = value[0].split(":")
        times = value[1].split(":")
        speeds = value[2].split(":")

    def closeWindow(self):
        string = self.listbox.get(self.listbox.curselection())
        value = string.split(",")
        channel = value[0].split(":")
        #print(channel)
        try:
            pos = self.listbox.curselection()
            text = (str(channel[0]) + ":" + str(channel[1]) + "," +" T :" + str(self.s3.get()) + "," + " S :" +  str(self.s4.get() ) )
            self.listbox.delete(pos[0])
            self.listbox.insert(pos[0], text)
        except:
            messagebox.showerror("Error", "No Action Selected\nPlease Select an Item In \n the Queue to Edit")
        self.t.withdraw()
        #self.listbox.selection_set(0, 0)

    def deleteQueue(self):
        end = self.listbox.size()
        self.listbox.delete(0, end)

    def showScales(self):
        if   self.buttonID == 0:
            self.s2.grid(row=6, column=2, columnspan=3, sticky=N+S+W+E)
            self.s2.set(6000)
            self.label2.grid(row=6, column=1)
            self.s1.set(1.0)
        elif self.buttonID == 1:
            self.s1.grid(row=7, column=2, columnspan=3, sticky=N+S+W+E)
            self.s1.set(1.0)
            self.s2.grid(row=6, column=2, columnspan=3, sticky=N+S+W+E)
            self.s2.set(6000)
            self.label2.grid(row=6, column=1)
            self.label1.grid(row=7, column=1, )
        elif self.buttonID == 2:
            self.s1.grid(row=7, column=2, columnspan=3, sticky=N+S+W+E)
            self.s1.set(1.0)
            self.s2.grid(row=6, column=2, columnspan=3, sticky=N+S+W+E)
            self.s2.set(6000)
            self.label2.grid(row=6, column=1)
            self.label1.grid(row=7, column=1, )
        elif self.buttonID == 3:
            self.s2.grid(row=6, column=2, columnspan=3, sticky=N+S+W+E)
            self.s2.set(6000)
            self.label2.grid(row=6, column=1)
            self.s1.set(1.0)
        elif self.buttonID == 4:
            self.s2.grid(row=6, column=2, columnspan=3, sticky=N+S+W+E)
            self.s2.set(6000)
            self.label2.grid(row=6, column=1)
            self.s1.set(1.0)

    def removeScales(self):
        try:
            self.s2.grid_forget()
        except:
            pass
        try:
            self.s1.grid_forget()
        except:
            pass
        try:
            self.label1.grid_forget()
        except:
            pass
        try:
            self.label2.grid_forget()
        except:
            pass

    def drawStuff(self):
        self.c.delete("all")
        self.c.create_image(10,50,anchor=NW, image=self.imgForBack)
        self.c.create_image(10, 105,anchor=NW, image=self.imgTurnR)
        self.c.create_image(10, 160,anchor=NW, image=self.imgTurnB)
        self.c.create_image(10, 215,anchor=NW, image=self.imgTurnH)
        self.c.create_image(10, 270,anchor=NW, image=self.imgTiltH)
        self.c.create_text(330, 30,font=self.font1, text="Drop Box", fill="#777777")
        self.c.create_text(80, 30,font=self.font1, text="Actions:", fill="#777777")
        self.c.create_rectangle(160, 50, 500, 300, width=5, fill="#444444")

    def mousePressed(self, event):
        self.deltaX1 = event.x - 10
        if (event.x > self.x and event.x < self.x + 145) and (event.y > self.y and event.y < self.y + 45):
            self.buttonID = 1
            self.imgID = self.imgForBack
            self.flag1 = True
            self.deltaY1 = event.y - 50
            self.actionString = "For/Back  :"
        elif (event.x > self.x and event.x < self.x + 145) and (event.y > 105 and event.y < 150):
            self.buttonID = 2
            self.imgID = self.imgTurnR
            self.flag1 = True
            self.deltaY1 = event.y - 105
            self.actionString = "Turn Robot:"
        elif (event.x > self.x and event.x < self.x + 145) and (event.y > 160 and event.y < 205):
            self.buttonID = 0
            self.imgID = self.imgTurnB
            self.flag1 = True
            self.deltaY1 = event.y - 160
            self.actionString = "Turn Body :"
        elif (event.x > self.x and event.x < self.x + 145) and (event.y > 215 and event.y < 260):
            self.buttonID = 3
            self.imgID = self.imgTurnH
            self.flag1 = True
            self.deltaY1 = event.y - 215
            self.actionString = "Turn Head :"
        elif (event.x > self.x and event.x < self.x + 145) and (event.y > 270 and event.y < 305):
            self.buttonID = 4
            self.imgID = self.imgTiltH
            self.flag1 = True
            self.deltaY1 = event.y - 270
            self.actionString = "Tilt Head :"
    def mouseDragged(self, event):
        if self.flag1 == True:
            self.drawStuff()
            self.c.create_image(event.x-self.deltaX1,event.y-self.deltaY1,anchor=NW, image=self.imgID)


    def mouseRelease(self, event):
        if self.flag1 == True:
            self.flag1 = False
            self.drawStuff()
            if (event.x > 160 and event.x < 600) and (event.y > 50 and event.y < 300):
                self.dropBoxFlag = True
                self.x = event.x - 22
                self.y = event.y -23
                self.c.create_image(273, 60,anchor=NW, image=self.imgID)
                self.printSettings()
                self.x = 10
                self.y = 50
                self.showScales()

    def printSettings(self):
        if self.buttonID == 1:
            self.c.create_text(328, 125,font=self.font3, text="Forward Backward Settings:", fill="#777777")
            self.c.create_text(328, 160,font=self.font2, text="PWM = 4000 => Full Speed Forward", fill="#777777")
            self.c.create_text(328, 180,font=self.font2, text="PWM = 6000 => Stop:", fill="#777777")
            self.c.create_text(328, 200,font=self.font2, text="PWM = 8000 => Full Speed Backwards", fill="#777777")
            self.c.create_text(328, 220,font=self.font2, text="Time = Time (sec) to Drive forward / backwards", fill="#777777")
        elif self.buttonID == 2:
            self.c.create_text(328, 125,font=self.font3, text="Turn Settings:", fill="#777777")
            self.c.create_text(328, 160,font=self.font2, text="PWM = 4000 => Fast Right Turn", fill="#777777")
            self.c.create_text(328, 180,font=self.font2, text="PWM = 6000 => No Turn:", fill="#777777")
            self.c.create_text(328, 200,font=self.font2, text="PWM = 8000 => Fast Left turn", fill="#777777")
            self.c.create_text(328, 220,font=self.font2, text="Time = Time (sec) to Turn Left / Right", fill="#777777")
        elif self.buttonID == 0:
            self.c.create_text(328, 125,font=self.font3, text="Turn Body Settings:", fill="#777777")
            self.c.create_text(328, 160,font=self.font2, text="PWM = 4000 => Turn Body Far Left", fill="#777777")
            self.c.create_text(328, 180,font=self.font2, text="PWM = 6000 => Face Body Forward", fill="#777777")
            self.c.create_text(328, 200,font=self.font2, text="PWM = 8000 => Turn Body Far Right", fill="#777777")
            self.c.create_text(328, 220,font=self.font2, text="Time = Time (sec) to Turn Body", fill="#777777")
        elif self.buttonID == 3:
            self.c.create_text(328, 125,font=self.font3, text="Turn Head Settings:", fill="#777777")
            self.c.create_text(328, 160,font=self.font2, text="PWM = 4000 => Turn Head Far Left", fill="#777777")
            self.c.create_text(328, 180,font=self.font2, text="PWM = 6000 => Head Face Forward", fill="#777777")
            self.c.create_text(328, 200,font=self.font2, text="PWM = 8000 => Turn Head Far Right", fill="#777777")
            self.c.create_text(328, 220,font=self.font2, text="Time = Time (sec) to Turn Head", fill="#777777")
        elif self.buttonID == 4:
            self.c.create_text(328, 125,font=self.font3, text="Tilt Head Settings:", fill="#777777")
            self.c.create_text(328, 160,font=self.font2, text="PWM = 4000 => Tilt Head far Up", fill="#777777")
            self.c.create_text(328, 180,font=self.font2, text="PWM = 6000 => Tilt Head to Center", fill="#777777")
            self.c.create_text(328, 200,font=self.font2, text="PWM = 8000 => Tilt Head for Down", fill="#777777")
            self.c.create_text(328, 220,font=self.font2, text="Time = Time (sec) to Tilt Head", fill="#777777")

    def removeAction(self):
        self.dropBoxFlag = False
        self.drawStuff()
        self.x = 10
        self.y = 50
        self.s1.set(1.0)
        self.s2.set(6000)

    def addToQueue(self):
        if self.dropBoxFlag == True:
            string = (self.actionString + str(self.buttonID) + "," +" T :" + str(self.s1.get()) + "," + " S :" + str(self.s2.get()))
            self.listbox.insert(END, string)
            self.drawStuff()
            self.dropBoxFlag = False
            self.x = 10
            self.y = 50
            self.s1.set(1.0)
            self.s2.set(6000)
            self.removeScales()
        else:
            messagebox.showerror("Error", "No Action Selected\nPlease Place an Action\nin the Drop Box")
    def moveUp(self):
        try:
            pos = self.listbox.curselection()
            if pos[0] == 0:
                messagebox.showerror("Error", "Selection is Already at The Top")
                return
            text = self.listbox.get(pos[0])
            self.listbox.delete(pos[0])
            self.listbox.insert(pos[0]-1, text)
        except:
            messagebox.showerror("Error", "No Action Selected\nPlease Select an Item In \n the Queue to Move")

    def moveDown(self):
        try:
            pos = self.listbox.curselection()
            last = self.listbox.size()
            if pos[0] == last-1:
                messagebox.showerror("Error", "Selection is Already at The Bottom")
                return
            text = self.listbox.get(pos[0])
            self.listbox.delete(pos[0])
            self.listbox.insert(pos[0]+1, text)
        except:
            messagebox.showerror("Error", "No Action Selected\nPlease Select an Item In \n the Queue to Move")


    def fun(self):
        self.drawStuff()
        self.x = 10
        self.y = 10
        print("Button is pushed")

    def removeQueue(self):
        try:
            selection = self.listbox.curselection()
            self.listbox.delete(selection[0])
        except:
            messagebox.showerror("Error", "No Action Selected\nPlease Select an Item In \n the Queue to Remove")

    def runQueue(self):
        size = self.listbox.size()
        queue = self.listbox.get(0, size)
        q1 = Run.Run(queue, size, self.root)
        try:
            _thread.start_new_thread(q1.runQueue, ())
        except:
            print ("Error: unable to start thread")
        try:
            _thread.start_new_thread(self.wait, (q1,))
        except:
            print ("Error: unable to start thread wait")

    def wait(self, q1):
        test = 0
        while (test != 1):
            test = q1.getComplete()
            pass
        q1.setComplete()
        self.drawStuff()

def __main__():

    root = tk.Tk()
    gui = GuiTest(root)
    root.mainloop()



__main__()
