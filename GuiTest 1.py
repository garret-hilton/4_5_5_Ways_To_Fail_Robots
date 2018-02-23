import time
import tkinter as tk
import _thread

def timer():
    time.sleep(5)
    print("Timer for 5 seconds has ended")

def arrow(key):
    #print("Arrow up")
    #print(key)
    #print(key.keycode)
    if key.keycode==114:
        wait = 5
        print("Right")
        try:
            _thread.start_new_thread(timer, ())
        except:
           print ("Error: unable to start thread")
    elif key.keycode==111:
        print("Up")
    elif key.keycode==116:
        print("Down")
    elif key.keycode==113:
        print("Left")
def mouseClick(event):
    print(event)
def fun():
    print("Button is pushed")

def motion(event):
  print("Mouse position: (%s %s)" % (event.x, event.y))
  return


print("Hello\n")

win = tk.Tk()
win.bind('<Up>', arrow)
win.bind('<Left>', arrow)
win.bind('<Down>', arrow)
win.bind('<Right>', arrow)
win.bind('<Button>', mouseClick)
myCan = tk.Canvas(win, bg="#333333", width="500", height="500")
myCan.bind('<Motion>', motion)

myCan.pack()
print("1")
lab = tk.Label(win, text="Hello Tkinter!")

lab.pack()

button = tk.Button(win, width="15", text="print", bg="blue", fg="yellow", command=fun)
button.pack(side = tk.RIGHT)
button2 = tk.Button(win, width="15", text="Second", bg="blue", fg="yellow", command=fun)
button2.pack(side = tk.BOTTOM)
print("End of Loop")
win.mainloop()
