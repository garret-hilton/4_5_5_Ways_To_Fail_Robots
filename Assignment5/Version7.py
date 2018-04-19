# 4_5_5_Ways_To_Fail_Robots

# Labs for CSCI - 455 Robotics - Embedded Systems
# Assignment 5
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
import Server
import Space
import random
import time
import Maestro

class Gui():
    def __init__(self, r, c=None):

        #self.init = start1
        #if self.init == True:
        #    self.makeMap()
        self.messageRecieved = False
        self.queueLoop = True
        self.orientation = "null"
        self.init = False
        self.client = c
        self.root = r
        self.position = 0
        self.fightFlag = 0
        #self.root.attributes('-fullscreen', True)
        self.speed = .8
        self.timeToWait = 5
        self.x = 10
        self.y = 50
        self.deltaX1 = 0
        self.deltaY1 = 0
        self.buttonID = 0
        self.font1 = font.Font(family="Times",size=30, weight="bold", slant="italic")
        self.font2 = font.Font(family="Times",size=12, weight="bold", slant="italic")
        self.font3 = font.Font(family="Times",size=20, weight="bold", slant="italic")
        self.font4 = font.Font(family="Courier",size=11, weight="bold")
        self.canvasW = 510
        self.canvasH = 330
        self.c = tk.Canvas(self.root, bg="#333333", width = self.canvasW, height=self.canvasH)
        self.c.bind('<B1-Motion>', self.mouseDragged)
        self.c.bind('<ButtonPress-1>', self.mousePressed)
        self.c.bind('<ButtonRelease-1>', self.mouseRelease)
        self.drawStuff()
        r.title("TangoBot")
        self.c.grid(row=1, column=1, rowspan=5, columnspan=5)
        self.server = Server.Server()
        self.startServer()
        self.makeMap()
        button = tk.Button(self.root, width="15", text="Start Game", font=self.font2, bg="blue", fg="yellow", command=self.startGame)
        button.grid(row=6, column=5)
        #self.checkQueueFlag()

    def checkQueueFlag(self):
        try:
            _thread.start_new_thread(self.lookForQueue, ())
            print("New Queue Flag Checker Started")
        except:
            print ("Error: unable to get queue")

    def lookForQueue(self):
        while(self.queueLoop):
            test = self.server.getQueue()
            if (test != 'null'):
                #print(test)
                if (False == self.checkValidMove(test)):
                    self.queueLoop = False
                    print("Invalid Message#" + test + "#" )
                else:
                    if (self.fightFlag == 0):
                        self.movePlayer(test)
                        self.queueLoop = False
                        self.server.setQueueFlag()
                        self.messageRecieved = True
                    else:
                        self.fightRun(test)
                        self.queueLoop = False
                        self.server.setQueueFlag()
                        self.messageRecieved = True
                if((test != "north") or (test != "south") or (test != "east") or (test != "west") or (test != "run") or (test != "fight")):
                    self.messageRecieved = True
            else:
                pass
                #print("Null Message")
                #print(test)
            self.queueLoop = True

    def fightRun(self, message):
        if (message == "run"):
            chance = random.randint(1,4)
            if change ==4:
                print("failed to run")
            else:
                rand = random.randint(0,8)
                self.position = random
        else:
            print("Fighting")


    def resetAllServos(self):
        control = Maestro.Controller()
        control.setTarget(0, 6000)
        control.setTarget(3, 6000)
        control.setTarget(4, 6000)

    def startGame(self):

        self.playerHealth = 100
        self.keyFound = False
        self.playerPosition = self.map[self.startPos]
        self.position = self.startPos
        directions = self.playerPosition.getDir()
        if directions[0] == True:
            self.orientation = 'North'
        elif directions[1] == True:
            self.orientation = 'Sorth'
        elif directions[2] == True:
            self.orientation = 'West'
        elif directions[3] == True:
            self.orientation = 'East'
        print("You are facing " + self.orientation)
        self.gameOver = False
        self.position = self.startPos
        print(self.playerPosition.getObject())
        print(self.playerPosition.getPaths())
        #message = self.playerPosition.getPaths()
        #self.server.tts(message)
        print("Player Position = " + str(self.position))
        while self.gameOver == False:
            self.messageRecieved = False
            self.playerPosition = self.map[self.position]
            message = self.playerPosition.getPaths()
            self.server.tts(message)
            time.sleep(3)
            if (self.fightFlag == 1):
                self.checkQueueFlag()
                self.server.stt()
            else:
                self.checkQueueFlag()
                self.server.stt()
            while(self.messageRecieved == False):
                pass
            self.checkEndGame()
        self.setQueueLoop = False
        print(self.position)
        print("You Win or Lose")
        #self.server.disconnect()

    def checkEndGame(self):
        print(self.map[self.position].getPrintValue())
        if (self.map[self.position].getPrintValue() == "E"):
            self.gameOver = True
        else:
            self.gameOver = False

    def checkValidMove(self, message):
        validMoves = self.map[self.position].getDir()
        print(validMoves)
        if ((message == "north") and (validMoves[0] == True)):
            return True
        elif ((message == "south") and (validMoves[1] == True)):
            return True
        elif ((message == "west") and (validMoves[2] == True)):
            return True
        elif ((message == "east") and (validMoves[3] == True)):
            return True
        elif ((message == "fight") or (message == "run")):
            return True
        else:
            return False

    def movePlayer(self, message):
        #control = Maestro.Controller()
        if(message == "north"):
            if(self.orientation == "North"):
                self.orientation = "North"
                self.position = self.position - 3
                #control.setTarget(0, 5000)
                time.sleep(1)
                #control.setTarget(0, 6000)
            elif(self.orientation == "South"):
                self.orientation = "North"
                self.position = self.position - 3
                #control.setTarget(2, 5000)
                time.sleep(2.2)
                #control.setTarget(2, 6000)
                #control.setTarget(0, 5000)
                time.sleep(1)
                #control.setTarget(0, 6000)
            elif(self.orientation == "West"):
                self.orientation == "North"
                self.position = self.position - 3
                #control.setTarget(2, 5000)
                time.sleep(1.1)
                #control.setTarget(2, 6000)
                #control.setTarget(0, 5000)
                time.sleep(1)
                #control.setTarget(0, 6000)
            elif(self.orientation == "East"):
                self.orientation == "North"
                self.position = self.position - 3
                #control.setTarget(2, 7000)
                time.sleep(1.3)
                #control.setTarget(2, 6000)
                #control.setTarget(0, 5000)
                time.sleep(1)
                #control.setTarget(0, 6000)
        elif(message == "south"):
            if(self.orientation == "North"):
                self.orientation = "South"
                self.position = self.position + 3
                #control.setTarget(2, 5000)
                time.sleep(2.2)
                #control.setTarget(2, 6000)
                #control.setTarget(0, 6000)
            elif(self.orientation == "South"):
                self.orientation = "South"
                self.position = self.position + 3
                #control.setTarget(0, 5000)
                time.sleep(1)
                #control.setTarget(0, 6000)
            elif(self.orientation == "West"):
                self.orientation == "South"
                self.position = self.position + 3
                #control.setTarget(2, 7000)
                time.sleep(1.3)
                #control.setTarget(2, 6000)
                #control.setTarget(0, 5000)
                time.sleep(1)
                #control.setTarget(0, 6000)
            elif(self.orientation == "East"):
                self.orientation == "South"
                self.position = self.position + 3
                #control.setTarget(2, 5000)
                time.sleep(1.1)
                #control.setTarget(2, 6000)
                #control.setTarget(0, 5000)
                time.sleep(1)
                #control.setTarget(0, 6000)
        elif(message == "west"):
            if(self.orientation == "North"):
                self.orientation = "West"
                self.position = self.position - 1
                #control.setTarget(2, 7000)
                time.sleep(1.3)
                #control.setTarget(2, 6000)
                #control.setTarget(0, 5000)
                time.sleep(1)
                #control.setTarget(0, 6000)
            elif(self.orientation == "South"):
                self.orientation = "West"
                self.position = self.position - 1
                #control.setTarget(2, 5000)
                time.sleep(1.1)
                #control.setTarget(2, 6000)
                #control.setTarget(0, 5000)
                time.sleep(1)
                #control.setTarget(0, 6000)
            elif(self.orientation == "West"):
                self.orientation == "West"
                self.position = self.position - 1
                #control.setTarget(0, 5000)
                time.sleep(1)
                #control.setTarget(0, 6000)
            elif(self.orientation == "East"):
                self.orientation == "West"
                self.position = self.position - 1
                #control.setTarget(2, 7000)
                time.sleep(2.3)
                #control.setTarget(2, 6000)
                #control.setTarget(0, 5000)
                time.sleep(1)
                #control.setTarget(0, 6000)
        elif(message == "east"):
            if(self.orientation == "North"):
                self.orientation = "East"
                self.position = self.position + 1
                #control.setTarget(2, 5000)
                time.sleep(1.1)
                #control.setTarget(2, 6000)
                #control.setTarget(0, 5000)
                time.sleep(1)
                #control.setTarget(0, 6000)
            elif(self.orientation == "South"):
                self.orientation = "East"
                self.position = self.position + 1
                #control.setTarget(2, 7000)
                time.sleep(1.3)
                #control.setTarget(2, 6000)
                #control.setTarget(0, 5000)
                time.sleep(1)
                #control.setTarget(0, 6000)
            elif(self.orientation == "West"):
                self.orientation == "East"
                self.position = self.position + 1
                #control.setTarget(2, 5000)
                time.sleep(2.2)
                #control.setTarget(2, 6000)
                #control.setTarget(0, 5000)
                time.sleep(1)
                #control.setTarget(0, 6000)
            elif(self.orientation == "East"):
                self.orientation == "East"
                self.position = self.position + 1
                #control.setTarget(0, 5000)
                time.sleep(1)
                #control.setTarget(0, 6000)
        else:
            print("Invalid Message")
        if ((self.map[self.position].getPrintValue == "H") or (self.map[self.position].getPrintValue == "W") or (self.map[self.position].getPrintValue == "K")):
            self.fightFlag = 1
        else:
            self.fightFlag = 0
        print("Position after move")
        print(self.position)
        #self.resetAllServos()


    def makeMap(self):
        self.test = "hello"
        num = [1, 2, 3, 6, 7, 8, 11, 12, 13]
        self.s1 = Space.Space(num[0])
        p = ["0","0","0","E"]
        self.s1.setPaths(p)
        self.s2 = Space.Space(num[1])
        p = ["0","S","W","E"]
        self.s2.setPaths(p)
        self.s3 = Space.Space(num[2])
        p = ["0","S","W","0"]
        self.s3.setPaths(p)
        self.s6 = Space.Space(num[3])
        p = ["0","S","0","E"]
        self.s6.setPaths(p)
        self.s7 = Space.Space(num[4])
        p = ["N","S","W","0"]
        self.s7.setPaths(p)
        self.s8 = Space.Space(num[5])
        p = ["N","0","0","0"]
        self.s8.setPaths(p)
        self.s11 = Space.Space(num[6])
        p = ["N","0","0","0"]
        self.s11.setPaths(p)
        self.s12 = Space.Space(num[7])
        p = ["N","0","0","E"]
        self.s12.setPaths(p)
        self.s13 = Space.Space(num[8])
        p = ["0","0","W","0"]
        self.s13.setPaths(p)
        self.map = [self.s1, self.s2, self.s3, self.s6, self.s7, self.s8, self.s11, self.s12, self.s13]
        self.placeObjects()
        pass

    def placeObjects(self):
        self.placeStartEnd()
        self.placeWeakBadGuy()
        self.placeHardBadGuy()
        self.placeKey()
        self.placeRegen()
        self.printMap()
        self.printMapGui()


    def placeStartEnd(self):
        start = random.randint(1,4)
        done = False
        while done == False:
            end = random.randint(1,4)
            if end != start:
                done = True
        if start == 1:
            self.s1.setObject("Start")
            self.s1.setPrintValue("S")
            self.startPos = 0
        elif start == 2:
            self.s3.setObject("Start")
            self.s3.setPrintValue("S")
            self.startPos = 2
        elif start == 3:
            self.s11.setObject("Start")
            self.s11.setPrintValue("S")
            self.startPos = 6
        elif start == 4:
            self.s13.setObject("Start")
            self.s13.setPrintValue("S")
            self.startPos = 8
        if end == 1:
            self.s1.setObject("End")
            self.s1.setPrintValue("E")
        elif end == 2:
            self.s3.setObject("End")
            self.s3.setPrintValue("E")
        elif end == 3:
            self.s11.setObject("End")
            self.s11.setPrintValue("E")
        elif end == 4:
            self.s13.setObject("End")
            self.s13.setPrintValue("E")
        print("Placed Start and End")

    def printMap(self):
        print(self.s1.getPrintValue() + "-" + self.s2.getPrintValue() + "-" + self.s3.getPrintValue() )
        print("  | |")
        print(self.s6.getPrintValue() + "-" + self.s7.getPrintValue() + " " + self.s8.getPrintValue() )
        print("| |  ")
        print(self.s11.getPrintValue() + " " + self.s12.getPrintValue() + "-" + self.s13.getPrintValue() )

    def placeKey(self):
        done = False
        print("Placing Key")
        while done == False:
            key = random.randint(0,8)
            if self.map[key].getObject() == "Bad Guy Hard":
                self.map[key].setKey()
                self.map[key].setPrintValue("K")
                done = True
                print("Key Placed")
        #print("Key is in Space ")
        #print(self.map[key].getNum())
        #print(self.map[key].getObject())
    def placeWeakBadGuy(self):
        done = False
        count = 0
        print("Placing Weak Bad Guys")
        while done == False:
            badguy = random.randint(0,8)
            if self.map[badguy].getObject() == "null":
                self.map[badguy].setObject("Bad Guy Weak")
                self.map[badguy].setPrintValue("W")
                self.map[badguy].setHealth(50)
                self.map[badguy].setDMG(5)
                count += 1
                if count == 4:
                    done = True
                    print("Weak Bad Guys Placed")

    def placeHardBadGuy(self):
        done = False
        count = 0
        print("Placing Hard Bad Guys")
        while done == False:
            badguy = random.randint(0,8)
            if self.map[badguy].getObject() == "null":
                self.map[badguy].setObject("Bad Guy Hard")
                self.map[badguy].setPrintValue("H")
                self.map[badguy].setHealth(100)
                self.map[badguy].setDMG(20)
                count += 1
                if count == 2:
                    done = True
                    print("Hard Bad Guys Placed")
    def placeRegen(self):
        done = False
        print("Placing Regen")
        while done == False:
            regen = random.randint(0,8)
            if self.map[regen].getObject() == "null":
                self.map[regen].setObject("Regen")
                self.map[regen].setPrintValue("R")
                done = True
                print("Regen Placed")

    def stt(self):
        self.server.stt()

    def startServer(self):
        self.server.startServer()

    def closeWindow(self):
        pass


    def drawStuff(self):
        self.c.delete("all")
        self.c.create_rectangle(160, 50, 500, 300, width=5, fill="#444444")


    def mousePressed(self, event):
        self.deltaX1 = event.x - 10
        if (event.x > self.x and event.x < self.x + 145) and (event.y > self.y and event.y < self.y + 45):
            pass
        elif (event.x > self.x and event.x < self.x + 145) and (event.y > 105 and event.y < 150):
            pass


    def mouseDragged(self, event):
        pass



    def mouseRelease(self, event):
        pass

    def printMapGui(self):
        line1 = self.s1.getPrintValue() + "-" + self.s2.getPrintValue() + "-" + self.s3.getPrintValue()
        line2 = "  | |"
        line3 = self.s6.getPrintValue() + "-" + self.s7.getPrintValue() + " " + self.s8.getPrintValue()
        line4 = "| |  "
        line5 = self.s11.getPrintValue() + " " + self.s12.getPrintValue() + "-" + self.s13.getPrintValue()
        self.c.create_text(328, 140,font=self.font4, text=line1, fill="#777777")
        self.c.create_text(328, 160,font=self.font4, text=line2, fill="#777777")
        self.c.create_text(328, 180,font=self.font4, text=line3, fill="#777777")
        self.c.create_text(328, 200,font=self.font4, text=line4, fill="#777777")
        self.c.create_text(328, 220,font=self.font4, text=line5, fill="#777777")


    def move(self):
        #self.setQueueLoop()
        pass

    def Fight(self):
        #self.setQueueLoop()
        pass

    def wait(self, q1):
        test = 0
        while (test != 1):
            test = q1.getComplete()
            pass
        q1.setComplete()
        print('Made it here')
        self.drawStuff()
        queueLoop = True
        self.setQueueLoop(queueLoop)
        self.checkQueueFlag()

def __main__():

    root = tk.Tk()
    start1 = True
    gui = Gui(root)
    root.mainloop()



__main__()
