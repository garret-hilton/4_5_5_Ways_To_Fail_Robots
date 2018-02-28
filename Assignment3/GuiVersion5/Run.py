import time
import tkinter as tk
import Maestro
import _thread
from tkinter import font

#class Run(queue, size):
class Run():

    def __init__(self, queue, size, c, root):
        self.root = root
        self.b = c
        self.canvasW = 800
        self.canvasH = 510
        self.c = tk.Canvas(self.root, bg="#333333", width = self.canvasW, height=self.canvasH)
        self.c.grid(row=1, column=1, rowspan=7, columnspan=7)
        self.fullQueue = queue
        self.queueSize = size
        self.done = False
        self.refresh = False
        self.complete = 0
        columns = 3
        rows = self.queueSize
        self.index = 0
        self.done = False
        self.font3 = font.Font(family="Times",size=20, weight="bold", slant="italic")
        self.queue = [0] * rows
        for i in range (rows):
            self.queue[i] = [0] * columns
        print(self.queue)
        self.parse()
        print(self.queue)

    def startAnimation(self):
        x = 100
        inc = 25
        midRow = int(self.canvasH/2)
        midCol = int(self.canvasW/2)
        while (self.done == False):
            x = x + inc
            if self.refresh == True:
                self.c.delete("all")
                self.c.create_text(450, 490,font=self.font3, text=self.fullQueue[self.index], fill="#ffffff")
                self.root.update()
                self.refresh = False
            if x == 300:
                inc = -25
            elif x == 100:
                inc = 25
            self.c.create_oval(5, 5, midCol-5, self.canvasH-40, fill="#000000") #left eye
            self.c.create_oval(midCol+5, 5, self.canvasW, self.canvasH-40, fill="#000000") #right eye
            self.c.create_oval(x, 220, x+100, 320, fill="#ffffff")
            self.c.create_oval(x+457, 220, x+557, 320, fill="#ffffff")
            #self.root.update()
            time.sleep(0.1)
        self.done = False

    def executeCommands(self):
        #control = Maestro.Controller()
        for i in range(self.queueSize):
            self.refresh = True
            self.index = i
            #control.setTarget(self.queue[i][0], self.queue[i][2])

            time.sleep(self.queue[i][1])
            if (self.queue[i][0] == 1 or self.queue[i][0] == 2):
                pass
                #control.setTarget(self.queue[i][0], self.queue[i][6000])
        self.done = True
        print("Ran Queue")
        self.complete = 1
        self.c.grid_remove()

    def getComplete(self):
        if self.complete == 1:
            return 1
        else:
            return 0

    def setComplete(self):
        self.complete = 0

    def runQueue(self):
        try:
            _thread.start_new_thread(self.executeCommands, ())
        except:
            print ("Error: unable to start thread")
        try:
            _thread.start_new_thread(self.startAnimation, ())
        except:
            print ("Error: unable to start thread")



    def parse(self):
        for i in range (self.queueSize):
            string = self.fullQueue[i]
            value = string.split(",")
            channels = value[0].split(":")
            self.queue[i][0] = int(channels[1])
            times = value[1].split(":")
            self.queue[i][1] = float(times[1])
            speeds = value[2].split(":")
            self.queue[i][2] = int(speeds[1])

def __main__():
    print("in main of run")
