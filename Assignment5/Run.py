import time
import tkinter as tk
import Maestro
import Server
import _thread
from tkinter import font


class Run():

    def __init__(self, queue, size, root, server):
        self.server = server
        self.root = root
        self.canvasW = 800
        self.canvasH = 460
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
        self.font3 = font.Font(family="Times",size=30, weight="bold", slant="italic")
        self.queue = [0] * rows
        self.message = "none"
        for i in range (rows):
            self.queue[i] = [0] * columns
        self.parse()

    def startAnimation(self):
        x = 140
        inc = 6
        midRow = int(self.canvasH/2)
        midCol = int(self.canvasW/2)
        while (self.done == False):
            x = x + inc
            if self.refresh == True:
                self.c.delete("all")
                self.c.create_text(400, 430,font=self.font3, text=self.fullQueue[self.index], fill="orange2")
                self.root.update()
                self.refresh = False
            if x == 212:
                inc = -6
            elif x == 68:
                inc = 6
            self.c.create_oval(5, 50, midCol-5, self.canvasH-90, fill="#ffffff") #left eye
            self.c.create_oval(midCol+5, 50, self.canvasW, self.canvasH-90, fill="#ffffff") #right eye
            self.c.create_oval(x-25, 195, x+125, 345, fill="blue2") # left color
            self.c.create_oval(x+400, 195, x+550, 345, fill="blue2") # right color
            self.c.create_oval(x, 220, x+100, 320, fill="#000000") # left pupil
            self.c.create_oval(x+425, 220, x+525, 320, fill="#000000") # right eye
            self.c.update()
            time.sleep(0.001)
        self.done = False

    def executeCommands(self):
        #control = Maestro.Controller()
        for i in range(self.queueSize):
            self.refresh = True
            self.index = i
            if (self.queue[i][0] != 5 and self.queue[i][0] != 1 and self.queue[i][0] != 2):
                #control.setTarget(self.queue[i][0], self.queue[i][2])
                time.sleep(self.queue[i][1])
            if (self.queue[i][0] == 1 or self.queue[i][0] == 2):
                pass
                #control.setTarget(self.queue[i][0], 6000)
                time.sleep(0.2)
            elif(self.queue[i][0] == 5):
                if self.queue[i][1] == 1:
                    self.message = "Hello World"
                elif self.queue[i][1] == 2:
                    self.message = "Kill all Humans"
                elif self.queue[i][1] == 3:
                    self.message = "Give me an A"
                elif self.queue[i][1] == 4:
                    self.message = "I'll be Back!"
                elif self.queue[i][1] == 5:
                    self.message = "Nothing Here"
                elif self.queue[i][1] == 6:
                    self.message = "Goodbye"
                self.server.tts(self.message)
                time.sleep(1);
            #control.setTarget(self.queue[i][0], 6000)
        self.done = True
        print("Ran Queue")
        self.complete = 1
        self.c.grid_remove()
        #self.resetAllServos()

    def resetAllServos(self):
        control = Maestro.Controller()
        control.setTarget(0, 6000)
        control.setTarget(3, 6000)
        control.setTarget(4, 6000)
        pass

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
