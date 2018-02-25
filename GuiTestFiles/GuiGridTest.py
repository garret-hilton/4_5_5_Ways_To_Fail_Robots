# 4_5_5_Ways_To_Fail_Robots

# Labs for CSCI - 455 Robotics - Embedded Systems

# The work is this repository belongs to Garret Hilton and Meshal Albaiz. Any
# use of this work without citation for academic purposes at Montana State
# University will be considered academic misconduct and plagiarism. The authors
# claim no liability for improper use of work contained in this repository.
# Use at your own risk.

import time
import tkinter as tk
from tkinter import *
from tkinter import font
import _thread

root = tk.Tk()
c = tk.Canvas(root, width=650, height=400, bg="#333333").grid(row=1, column=1, rowspan=2, columnspan=5)
listbox = tk.Listbox(root, bg="#999999")
listbox.grid(row=1, column=6, sticky=N+S)
scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL)
scrollbar.grid(row=1,column=7, sticky=N+S)
label1=tk.Label(root, text="Set Time")
label1.grid(row=3, column=1)
label2=tk.Label(root, text="Set Speed")
label2.grid(row=3, column=3)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
e1 = tk.Entry(root)
e2 = tk.Entry(root)
e1.grid(row=3, column=2)
e2.grid(row=3, column=4)
button = tk.Button(root, width="15", text="Enter", bg="blue", fg="yellow", command=print("ButtonPress"))
button.grid(row=3, column=5)
#root.scrollbar(command=root.listbox.yview)
#root.config_listbox(yscrollcommand=root.scrollbar.set)
#listbox = Listbox(root, yscrollcommand=scrollbar.set, bg="#999999").grid(row=1, column=2)
root.mainloop()
