# 4_5_5_Ways_To_Fail_Robots

# Labs for CSCI - 455 Robotics - Embedded Systems

# The work is this repository belongs to Garret Hilton and Meshal Albaiz. Any
# use of this work without citation for academic purposes at Montana State
# University will be considered academic misconduct or plagiarism. The authors
# claim no liability for improper use of work contained in this repository.
# Use at your own risk.

import time
import Maestro
import sys, termios, tty

def getKey(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            inKey = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

        # inKey = raw_input("Enter key: ")
        return inKey


def mainControl(self):
        input = "*" # create random input value
        waist = 6000 # set all parameters to 6000 initially
        htilt = 6000
        hturn = 6000
        movement = 6000
        while input != "q": # while input is not q for quit
                input = x.getKey() # get keyboard input
                if input == "1": # if 1 then turn waist to left by incrementing by 250 each time
                        waist += 250
                        x.setTarget(0, waist)
                elif input == "2": # if 2 then turn waist to right by decrementing by 250 each time
                        waist -= 250
                        x.setTarget(0, waist)
                elif input == "3": # if 3 then turn head to left by incrementing by 250 each time
                        hturn += 250
                        x.setTarget(3, hturn)
                elif input == "4": # if 4 then turn head to right by decrementing by 250 each time
                        hturn -= 250
                        x.setTarget(3, hturn)
                elif input == "5": # if 5 then tilt head up by incrementing by 250 each time
                        htilt += 250
                        x.setTarget(4, htilt)
                elif input == "6": # if 6 then tilt head down by decrementing by 250 each time
                        htilt -= 250
                        x.setTarget(4, htilt)
                elif input == "s": # if s then move backwards by incrementing by 250 each time
                        movement += 250
                        x.setTarget(1, movement)
                elif input == "w": # if w then move forward by decrementing by 250 each time
                        movement -= 250
                        x.setTarget(1, movement)
                elif input == "a":  # if a then move left by incrementing by 1000 for 0.7 seconds
                        x.setTarget(2, 7000)
                        time.sleep(0.7)
                        x.setTarget(2, 6000) # reset to 6000 after turning
                elif input == "d": # if d then move left by decrementing by 1000 for 0.7 seconds
		                  x.setTarget(2, 5000)
                        time.sleep(0.7)
                        x.setTarget(2, 6000)   # reset to 6000 after turning
                else: # if any other input then reset all servos and motors to 6000
                        x.setTarget(0, 6000)
                        x.set(1, 6000)
                        x.set(2, 6000)
                        x.setTarget(3, 6000)
                        x.setTarget(4, 6000)
                        print("quitting") # technically we only quit if q is hit, any other button would reset the servos without quitting

x = Controller() # create instance x
x.mainControl() # loop for movement until q is hit
