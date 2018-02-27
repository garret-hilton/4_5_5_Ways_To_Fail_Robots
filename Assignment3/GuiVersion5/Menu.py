import time
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
        #self.filename

    def openFile(self):
        print("Open Something")

    def saveFile(self):
        size = self.listbox.size()
        queue = self.listbox.get(0, size)
        string = ""
        for i in range (size):
            string += queue[i]
            if(i != size):
                string += ";"
        print(string)
        filename = filedialog.asksaveasfilename(initialdir = "/", title="Select File", filetypes=(("text files","*.txt"),("all files","*.*")))
        file = open(filename, mode="w")
        file.write(string)
        file.close()

    def exitGui(self):
        print("Exit Gui")

    def aboutGui(self):
        print("About Gui")

    def helpGui(self):
        print("helpGui")
