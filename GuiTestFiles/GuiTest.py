import time
import tkinter as tk
import _thread

class GuiTest():
    def __init__(self, r, c=None):
        self.client = c
        self.root = r
        #self.flag = True
        self.speed = .8
        self.timeToWait = 5
        self.flag = False
        self.x = 5
        self.y = 5
        r.title("TangoBot")
        r.bind('<Up>', self.arrow)
        r.bind('<Left>', self.arrow)
        r.bind('<Down>', self.arrow)
        r.bind('<Right>', self.arrow)
        #r.bind('<Button>', self.mouseClick)
        self.canvasW = 800
        self.canvasH = 410
        self.c = tk.Canvas(self.root, bg="#333333", width = self.canvasW, height=self.canvasH)
        self.c.bind('<B1-Motion>', self.mouseDragged)
        self.c.bind('<ButtonPress-1>', self.mousePressed)
        self.c.bind('<ButtonRelease-1>', self.mouseRelease)
        self.c.create_oval(5, 5, 45, 45, fill="#FFFF00")
        self.c.bind('<Motion>', self.motion)

        self.c.pack()

        #lab = tk.Label(root, text="Hello Tkinter!")

        #lab.pack()

        button = tk.Button(self.root, width="15", text="print", bg="blue", fg="yellow", command=self.fun)
        button.pack(side = tk.RIGHT)
        button2 = tk.Button(self.root, width="15", text="Second", bg="blue", fg="yellow", command=self.fun)
        button2.pack(side = tk.BOTTOM)

    def timer(self):
        temp = self.timeToWait
        time.sleep(self.timeToWait)
        print("Timer for %f seconds has ended" % temp)

    def mousePressed(self, event):
        if (event.x > self.x and event.x < self.x + 45) and (event.y > self.y and event.y < self.y + 45):
            self.flag = True

    def mouseDragged(self, event):
        if self.flag == True:
            self.c.delete("all")
            self.c.create_oval(event.x - 22, event.y-22, event.x+23, event.y+23, fill="#FFFF00")

    def mouseRelease(self, event):
        if self.flag == True:
            self.flag = False
            self.x = event.x - 22
            self.y = event.y -23
            print("Released at:\n    x: %f" % self.x)
            print("\n    y: %f" %  self.y)

    def arrow(self, key):
        #print("Arrow up")
        #print(key)
        #print(key.keycode)
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
    def fun():
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
