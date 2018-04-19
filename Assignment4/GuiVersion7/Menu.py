import time, sys
import tkinter as tk
import Maestro
import _thread
from tkinter import font, Menu, filedialog


class FileMenu():

    def __init__(self, root, listbox):
        self.root = root
        self.listbox = listbox
        self.menuBar = Menu(self.root)
        self.root.config(menu=self.menuBar)
        self.fileMenu = Menu(self.menuBar, tearoff=0)
        self.fileMenu.add_command(label="Open", command=self.openFile)
        self.fileMenu.add_command(label="Save", command=self.saveFile)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit", command=self.exitGui)
        self.menuBar.add_cascade(label="File", menu=self.fileMenu)
        self.editmenu = Menu(self.menuBar, tearoff=0)
        self.editmenu.add_command(label="DeleteQueue", command=self.deleteQueue)
        self.editmenu.add_command(label="Reset Servos", command=self.resetAllServos)
        self.menuBar.add_cascade(label="Edit", menu=self.editmenu)
     
    def resetAllServos(self):
        control = Maestro.Controller()	
        control.setTarget(0, 6000)
        control.setTarget(3, 6000)
        control.setTarget(4, 6000)
		
    def deleteQueue(self):
        end = self.listbox.size()
        self.listbox.delete(0, end)

    def openFile(self):
        print("Open Something")

    def saveFile(self):
        size = self.listbox.size()
        queue = self.listbox.get(0, size)
        string = ""
        try:
            for i in range (size):
                string += queue[i]
                if(i != size):
                    string += ";"
                print(string)
            filename = filedialog.asksaveasfilename(initialdir = "/home", title="Select File",initialfile="queue1", filetypes=(("text files","*.txt"),("all files","*.*")))
            file = open(filename, mode="w")
            file.write(string)
            file.close()
        except:
            pass

    def exitGui(self):
        sys.exit()
        print("Exit Gui")

    def aboutGui(self):
        print("About Gui")

    def helpGui(self):
        print("helpGui")
