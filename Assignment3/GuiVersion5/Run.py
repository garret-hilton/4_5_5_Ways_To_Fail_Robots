import time
import tkinter as tk
import Maestro
import _thread
from tkinter import font

#class Run(queue, size):
class Run():

    def __init__(self, queue, size, c):
        self.c = c
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

        while (self.done == False):
            if self.refresh == True:
                self.c.delete("all")
                self.c.create_text(380, 125,font=self.font3, text=self.fullQueue[self.index], fill="#777777")
                self.refresh = False
        self.done = False

    def executeCommands(self):
        #control = Maestro.Controller()
        for i in range(self.queueSize):
            self.refresh = True
            self.index = i
            self.c.delete("all")
            self.c.create_text(380, 125,font=self.font3, text=self.fullQueue[i], fill="#777777")
            #control.setTarget(self.queue[i][0], self.queue[i][2])
            time.sleep(self.queue[i][1])
        self.done = True
        print("Ran Queue")
        self.complete = 1

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
